#!python
'''HashFS; Virtual file system module
This HashFS module works on top of an underlying regular file system
'''

import hashlib
import logging
import pathlib
import shutil
import tempfile
import uuid

from .exceptions import *
from . import io as hashfs_io
from . import utils as hashfs_utils

import simplifiedapp

LOGGER = logging.getLogger(__name__)


class BasicHashFS:
	'''The simplest HashFS version
	This approach works by "encoding" each file's size and one hash sum on the path (directories and file names). It's extremely vocal about file structure, so it's not intended to be modified via regular means (file explorer, command line). This class should always be used instead.

	The logic is as follow:
	- The whole path to a file, if concatenated (removing the separating "/" or "\") will contain the size of the file in bytes and a hash sum of the content
	- Such values will live in separate folders/files (no folder or file will contain size data AND hash data at the same time)
	- To accomodate for big file systems the size part of the path can be split in different directories. Each depth level will be a directory named after 3 digits from the size (except for the first one that will contain "the rest" of the digits). A 5GB file residing on a "size_depth=4" filesystem will live in "root/5/368/709/120/...". The same file residing on a "size_depth=2" filesystem will live in "root/5368709/120/...". The minimum "size_depth" is 1, and it should always be an integer number.
	- On the hash side of things the directory length is configurable on creation time, with the "hash_dir_size" parameter (it defaults to 4)
	- There's also the "hash_depth" parameter that does for the hash the same thing that "size_depth" does for the size (defaults to 3).
	- The rest of the hash that hasn't been consumed by the directory names up to this point are used as the name of the final file.
	- The multiplication of "hash_dir_size" and "hash_depth" should yield a number smaller than the length of the hashes used (32 for md5, 40 for sha1, 128 for sha512, etc.)

	The filesystem creation proces adds a single file to the tree called the "zero file". It's basically THE empty file, which is a known quantity (size 0, some "initial" hash). By parsing the path to such file is possible to retrieve the parameters that were used on creation, which are then used to configure the class for further operations (no need to "remember" which parameters should be used).
	'''

	MAX_DEPTH_SEARCH = 50
	LIVE_STREAMS_PREFIX = '.hashfs-live-'

	def __init__(self, fs_root, live_dir = None):

		LOGGER.debug('Starting HashFS based on: %s', fs_root)
		self._root = pathlib.Path(fs_root)
		self._size_depth, self._hash_algorithm, self._hash_length, self._hash_dir_length, self._hash_depth = self._detect_filesystem_parameters(self._root)
		if live_dir is None:
			self._live_dir_path = self._root
		else:
			self._live_dir_path = pathlib.Path(live_dir)

	def __del__(self):
		'''Del magic
		Cleanup tasks, leave a clean file system behind.
		'''

		if hasattr(self, 'live_dir'):
			try:
				self.live_dir.rmdir()
			except OSError:
				LOGGER.warning("Live directory (%s) is not empty. It seems some operations didn't complete sucessfully", self.live_dir)
			else:
				LOGGER.debug('Live directory deleted successfully')

	def __getattr__(self, name):
		'''Getattr magic
		Lazy feature instantiation.
		'''

		if name == '_hash_file_stem_size':
			value = self._hash_length - self._hash_dir_length * self._hash_depth
		elif name == 'live_dir':
			value = pathlib.Path(tempfile.mkdtemp(prefix = self.LIVE_STREAMS_PREFIX, dir = self._live_dir_path))
		else:
			raise AttributeError(name)

		LOGGER.debug('Setting self.%s to: %s', name, value)
		setattr(self, name, value)
		return value

	@classmethod
	def _detect_filesystem_parameters(cls, fs_root):
		'''Detect filesystem parameters
		Uses the path to the zero file to detect the parameters of the file sytem. Returns a tuple with the values:
		(size_depth, hash_algo, hash_length, hash_dir_size, hash_depth)
		'''

		zero_file = cls._get_zero_file_path(fs_root)
		zero_file = zero_file.relative_to(fs_root)

		zero_string = ''.join(zero_file.parts)
		zero_hashes = cls.zero_hashes()
		algorithm, zero_hash = None, None
		for algo_name, algo_zero in zero_hashes.items():
			if zero_string[-len(algo_zero):] == algo_zero:
				algorithm, zero_hash = algo_name, algo_zero
				zero_hash_length = len(zero_hash)
				break
		if algorithm is None:
			raise ZeroFileError('Algorithm is not supported on this system')
		else:
			LOGGER.debug('Detected algorithm: %s', algorithm)

		hash_parts, hash_char_count = [], 0
		reverse_zero_parts = list(zero_file.parts)
		reverse_zero_parts.reverse()
		for part in reverse_zero_parts:
			hash_parts.append(part)
			hash_char_count += len(part)
			if hash_char_count > zero_hash_length:
				raise ZeroFileError('Invalid zero file structure')
			elif hash_char_count == zero_hash_length:
				break
		hash_depth = len(hash_parts) - 1
		LOGGER.debug('Detected hash_depth: %d', hash_depth)

		if len(hash_parts) > 1:
			hash_dir_size = len(hash_parts[1])
			for part in hash_parts[1:]:
				if len(part) != hash_dir_size:
					raise ZeroFileError('Inconsistent directory length in hashes')
			LOGGER.debug('Detected hash_dir_size: %d', hash_dir_size)
		else:
			hash_dir_size = None
			LOGGER.debug('No hash_dir_size detected since hash_depth=1 (no hash directories, all in files)')

		size_parts = reverse_zero_parts[len(hash_parts):]
		if len(size_parts) > 1:
			for part in size_parts[:-1]:
				if len(part) != 3:
					raise ZeroFileError('Invalid directory length in sizes')
		size_depth = len(size_parts)
		LOGGER.debug('Detected size_depth: %d', size_depth)

		return size_depth, algorithm, zero_hash_length, hash_dir_size, hash_depth

	@classmethod
	def _get_zero_file_path(cls, fs_root):
		'''Get the path for the zero file
		A valid filesystem must have a zero file, which would live in the all zero size path and must not have any siblings (no more than 1 hash for a zero). This method finds the path to such file.
		'''

		LOGGER.debug('Looking for a zero file on: %s', fs_root)
		fs_root = pathlib.Path(fs_root)
		if not fs_root.is_dir():
			raise NotADirectoryError("File system root isn't usable")

		zero_target = fs_root / '0'
		if not zero_target.is_dir():
			raise ZeroFileError('Zero file is missing')

		for none in range(cls.MAX_DEPTH_SEARCH):
			next_child = zero_target / '000'
			if next_child.is_dir():
				zero_target = next_child
			else:
				break
		LOGGER.debug('Got all the zero size directories so far: %s', zero_target)

		for none in range(cls.MAX_DEPTH_SEARCH):

			childs = list(zero_target.iterdir())

			if len(childs) != 1:
				raise ZeroFileError('Invalid zero file structure')

			if childs[0].is_file():
				zero_target = childs[0]
				LOGGER.debug('Found the zero file: %s', zero_target)
				return zero_target
			elif childs[0].is_dir():
				zero_target = childs[0]
			else:
				raise ZeroFileError('Invalid zero file structure')

	def _place_stream(self, stream):
		'''Place a stream
		Move a completed stream to the right location on the file tree
		'''

		LOGGER.debug('Placing the stream: %s', stream)
		try:
			destination_path = self.get_stream_path(stream = stream)
			destination_dir = destination_path.parent
			destination_file = destination_path.name
		except StreamNotFoundError:
			pass
		else:
			if not (set(destination_path.suffixes) ^ set(stream._file_path.suffixes)):
				LOGGER.info('Skipping the placement of an existing file: %s', destination_path)
				stream._file_path.unlink()
				stream._file_path = destination_path
				return stream._file_path
			else:
				LOGGER.debug('Removing file with different suffixes: %s', destination_path)
				destination_path.unlink()
		destination_dir, destination_file = self.build_path(stream = stream)
		destination_path = destination_dir / ''.join([destination_file] + stream._file_path.suffixes)
		LOGGER.debug('Creating directory structure: %s', destination_dir)
		destination_dir.mkdir(parents = True, exist_ok = True)
		LOGGER.debug('Moving file: %s -> %s', stream._file_path, destination_path)
		stream._file_path = stream._file_path.rename(destination_path)
		return stream._file_path

	def build_path(self, stream = None, size = None, hash_ = None):
		'''Build a path
		Builds a path from the details provided based on the file system configuration. This would be a "pure" path (on pathlib parlance) which might not exist at all.
		'''

		if stream is None:
			if (size is None) or (hash_ is None):
				raise HashFSParametersError("Can't build a path out of thin air")
			elif len(hash_) != self._hash_length:
				raise HashFSParametersError('Not a valid {} hash: {}'.format(self._hash_algorithm, hash_))
			LOGGER.debug('Building path for details: %s | %s', size, hash_)
		else:
			LOGGER.debug('Building path for stream: %s', stream)
			size, hash_ = stream['size'], stream[self._hash_algorithm]

		size_part, path_parts = str(size), []
		for level in range(self._size_depth):
			path_parts.append(size_part[-3:].zfill(3))
			size_part = size_part[:-3]
		path_parts.reverse()
		path_parts[0] = str(int(path_parts[0]))

		for level in range(self._hash_depth):
			path_parts.append(hash_[:self._hash_dir_length])
			hash_ = hash_[self._hash_dir_length:]

		return pathlib.Path(self._root, *path_parts), hash_

	@classmethod
	def create(cls, fs_root, size_depth = 3, hash_algo = 'sha256', hash_dir_size = 4, hash_depth = 2, overwrite = False):
		'''Create a new file system
		Creates a new SimpleHashFS file system on the specified root. It will fail if the root directory is not empty unless the "overwrite" flag is provided.
		'''

		hashfs_utils.type_check(int, size_depth = size_depth, hash_dir_size = hash_dir_size, hash_depth = hash_depth)
		hashfs_utils.int_range_check(range_min = 1, size_depth = size_depth, hash_dir_size = hash_dir_size)
		hashfs_utils.int_range_check(range_min = 0, hash_depth = hash_depth)

		root = pathlib.Path(fs_root)
		if root.exists():
			if not overwrite:
				raise FileExistsError("File system root already exists (and not overwriting)")
			elif not root.is_dir():
				raise NotADirectoryError("File system root isn't usable")
		else:
			root.mkdir()

		zero_hashes = cls.zero_hashes()
		if hash_algo.lower() not in zero_hashes:
			raise HashFSParametersError('The hash algorithm is not supported: {}'.format(hash_algo.lower()))

		hash_0 = zero_hashes[hash_algo]
		if hash_dir_size * hash_depth >= len(hash_0):
			raise HashFSParametersError('Invalid combination of algorithm "{}" ({} characters) with hash_dir_size={} and hash_depth={} ({} characters)'.format(hash_algo, len(hash_0), hash_dir_size, hash_depth, hash_dir_size * hash_depth))

		LOGGER.debug('Filesystem creation input validated.')

		current_path_level = root / '0'
		current_path_level.mkdir(exist_ok = overwrite)
		for size_level in range(size_depth - 1):
			current_path_level = current_path_level / '000'
			current_path_level.mkdir(exist_ok = overwrite)

		for level in range(hash_depth):
			current_path_level = current_path_level / hash_0[:hash_dir_size]
			current_path_level.mkdir(exist_ok = overwrite)
			hash_0 = hash_0[hash_dir_size:]

		current_path_level = current_path_level / hash_0
		current_path_level.touch(exist_ok = overwrite)

		LOGGER.debug('Zero file structure created: %s', current_path_level)

		return cls(fs_root)

	def delete_stream(self, stream = None, size = None, hash_ = None):
		'''Delete stream
		Delete an existing stream in the file system. It leverages the get_stream_path function. Returns a list with the file and all the directories removed.
		'''

		stream_path = self.get_stream_path(stream = stream, size = size, hash_ = hash_)
		LOGGER.debug('Deleting stream: %s', stream_path)
		stream_path.unlink()
		result = [stream_path]
		current_dir = stream_path.parent
		LOGGER.debug('Looking for empty directories to delete starting with: %s', current_dir)
		for none in stream_path.parts:
			if not list(current_dir.iterdir()):
				LOGGER.debug('Deleting empty directory: %s', current_dir)
				current_dir.rmdir()
				result.append(current_dir)
				current_dir = current_dir.parent
			else:
				break
		return result

	def get_stream_path(self, stream = None, size = None, hash_ = None):
		'''Get a stream path
		Get a the path to the stream matching the details provided.
		'''

		stream_dir, stream_file_name = self.build_path(stream = stream, size = size, hash_ = hash_)
		pattern = stream_file_name + '*'
		LOGGER.debug('Looking for "%s" in: %s', pattern, stream_dir)
		stream_paths = list(stream_dir.glob(pattern))
		if not stream_paths:
			raise StreamNotFoundError('No stream found with such details')
		if len(stream_paths) > 1:
			raise StreamNotFoundError('Too many files with the same size/hash: {}'.format(stream_paths))

		LOGGER.debug('Got that single hit: %s', stream_paths[0])
		return stream_paths[0]

	def import_file(self, path):
		'''Import a single file
		Import an existing file into the file system.
		'''

		path = pathlib.Path(path)
		if not path.is_file():
			raise FileNotFoundError('Not a valid file: {}'.format(path))
		LOGGER.debug('Importing file: %s', path)

		with path.open(mode = 'rb') as source_file:
			destination = self.new_stream(extra_mode = 'b', suffixes = path.suffixes)
			with destination as destination_file:
				shutil.copyfileobj(source_file, destination_file)

		return destination._file_path, destination

	def import_tree(self, tree_root):
		'''Import a subtree
		Import files into the file system. If the root points to a file only that file will be inported; if it's a directory all it's children will be imported recursively.
		'''

		result = {}
		tree_level = pathlib.Path(tree_root)
		if tree_level.is_dir():
			LOGGER.debug('Importing subtree: %s', tree_level)
			for child in tree_level.iterdir():
				try:
					result.update(self.import_tree(child))
				except FileExistsError as error_:
					LOGGER.info('Imported skipped for %s; File already exists: %s', child, error_)
				except Exception:
					LOGGER.exception('Import failed for: %s', child)
		else:
			stream_path, stream_details = self.import_file(tree_level)
			result[stream_path] = stream_details
		return result

	def new_stream(self, *args, extra_mode = '', suffixes = (), **kwargs):
		'''New stream
		Create a fresh stream object on "x" mode (exclusive write) that will be stored on the filesystem on close.
		'''

		LOGGER.debug('Creating a new stream with: %s | %s', args, kwargs | {'extra_mode' : extra_mode, 'suffixes' : suffixes})
		return hashfs_io.FileWrapperStream(*args, file_path = self.live_dir / ''.join([str(uuid.uuid4())] + list(suffixes)), mode = 'x' + extra_mode, hash_names = [self._hash_algorithm], close_callback = self._place_stream, **kwargs)

	def parse_path(self, path, concrete = False):
		'''Parses a path
		Accepts a system path to a file and parses the size and hash values out of it. It checks that the path is actually valid in the current filesystem context. If the "concrete" flag is passed it checks if the file actually exists. Any error will raise a ValueError exception.
		'''

		path = pathlib.Path(path)
		try:
			path = path.relative_to(self._root)
		except ValueError:
			raise HashFSParametersError('Path is not part of the current file system: {}'.format(path))

		size = path.parts[:self._size_depth]
		for size_part in size[1:]:
			if len(size_part) != 3:
				raise StreamPathError('Size section of wrong length ({}): {}'.format(len(size_part), size_part))
			elif not size_part.isdecimal():
				raise StreamPathError('Size section with non decimal characters: {}'.format(size_part))
		size = int(''.join(size))

		hash_parts = path.parts[self._size_depth:-1]
		if len(hash_parts) != self._hash_depth:
			raise StreamPathError('Invalid depth on the hash structure: {}'.format(pathlib.Path(*hash_parts)))
		for hash_part in hash_parts:
			if len(hash_part) != self._hash_dir_length:
				raise StreamPathError('Hash section of wrong length ({}): {}'.format(len(hash_part), hash_part))

		if path.suffixes:
			hash_file_stem = path.name[:-len(''.join(path.suffixes))]
		else:
			hash_file_stem = path.name
		if len(hash_file_stem) != self._hash_file_stem_size:
			raise StreamPathError('Hash file name/stem of wrong length ({}): {}'.format(len(hash_file_stem), hash_[-1]))

		if concrete and not (self._root / path).is_file():
			raise StreamPathError('Not a file: {}'.format(path))

		hash_ = ''.join(hash_parts + (hash_file_stem,))

		return size, hash_

	def stream_allocation_table(self):
		'''Build Stream Allocation Table
		Create the mapping of (size, hash) : relative_file_path containing all the files in the file system.
		'''

		existing_files = []
		for path in self._root.rglob('*'):
			if path.is_file():
				existing_files.append(path)

		sat = {}
		for path in existing_files:
			try:
				size, hash_ = self.parse_path(path)
			except StreamPathError:
				LOGGER.warning('File outside the SAT: %s', path)
			if not size:
				LOGGER.debug('Ignoring zero file: %s', path)
				continue
			sat[(size, hash_)] = str(path.relative_to(self._root))

		return sat

	@staticmethod
	def zero_hashes():
		'''Zero hashes
		Get the list of the "zero value" of every hash algorithm supported on the current system (barring the variable output ones, aka SHAKE).
		'''

		LOGGER.debug('Building the list of zero hashes')
		zeroes = {}
		for hash_algo in hashlib.algorithms_available:
			if hash_algo.lower().startswith('shake'):
				LOGGER.debug('Ignoring variable output SHAKE algorithms')
				continue
			zeroes[hash_algo.lower()] = hashlib.new(hash_algo).hexdigest()

		return zeroes

if __name__ == '__main__':
	simplifiedapp.main()

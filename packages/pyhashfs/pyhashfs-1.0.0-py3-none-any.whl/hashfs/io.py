#!python
'''HashFS.IO; Stream access
These classes implement different ways to access the streams on the underlying storage.
'''

import abc
import collections.abc
import hashlib
import logging
import os
import pathlib
import shutil
import zlib

import simplifiedapp

LOGGER = logging.getLogger(__name__)


class AbstractBaseStream(collections.abc.MutableMapping):
	'''Basic stream structure
	The actual content of the class are about handling the stream's metadata (sums & hashes). The actual handling of the stream's content should be handled by the child classes.

	ToDo:
	- Make stream reads reusable.
	'''

	_is_open = None

	def __delitem__(self, name):
		'''Delete item magic
		Used to delete the right value from either of the 2 internal dicts.
		'''

		if name in self._sums:
			return self._sums.__delitem__(name)
		elif name in self._hashes:
			return self._hashes.__delitem__(name)

		raise KeyError(name)

	def __enter__(self):
		'''Context initialization
		Initialize the stream based on provided values.
		'''

		if self._is_open is None:
			self.open(*self._open_arg_and_kwargs[0], **self._open_arg_and_kwargs[1])

		return self

	def __exit__(self, exc_type, exc_value, traceback):
		'''Context termination
		Complete the stream based on several aspects.
		'''

		self.close()

		if exc_type is not None:
			raise NotImplementedError('Handle exceptions in context')

	def __getattr__(self, name):
		'''Getattr magic
		Forward attribute resolution to the inner _stream object.
		'''

		if name == '_stream':
			raise AttributeError(name)

		return getattr(self._stream, name)

	def __getitem__(self, name):
		'''Get item magic
		Used to get the right value from either of the 2 internal dicts.
		'''

		if self._is_open is None:
			raise RuntimeError('No stream has been opened, nothing to sum up')
		elif self._is_open:
			raise NotImplementedError('The stream is still open and partial sums are not supported yet')

		if name in self._sums:
			return self._sums[name]
		elif name in self._hashes:
			return self._hashes[name].hexdigest()

		raise KeyError(name)

	def __init__(self, *args, mode = 'wb', no_sums = False, extra_sums = False, hash_names = (), close_callback = None, **kwargs):
		'''Init magic
		Initialize the stream based on provided values.
		'''

		super().__init__()

		LOGGER.debug('Initializing a "%s" instance', self.__class__.__name__)

		self._close_callback = close_callback
		self._is_live, self._is_synchronous = self.parse_mode(mode)
		LOGGER.debug('Stream is live | synchronous?: %s | %s', self._is_live, self._is_synchronous)

		if no_sums:
			self._sums, self._hashes = {}, {}
		else:
			self._sums = {'size' : 0}
			if extra_sums:
				self._sums.update({'adler32' : 1, 'crc32' : 0})
			self._hashes = {hash_name : hashlib.new(hash_name) for hash_name in hash_names}

		self._open_arg_and_kwargs = [args, kwargs | {'mode' : mode}]

	def __iter__(self):
		'''Iter magic
		Just returning the regular dict iter of the merge of the 2 internal dicts.
		'''

		return {key : value for key, value in self.items()}.__iter__()

	def __len__(self):
		'''Length magic
		This is a merge of dicts, so the length is the sum of them.
		'''

		return len(self.keys())

	def __repr__(self):
		'''Repr magic
		Recreate a regular __repr__ behavior using the custom items() method.
		'''

		return repr({key : value for key, value in self.items()})

	def __setitem__(self, name, value):
		'''Set item magic
		Prevent the modification of the stream metadata.
		'''

		raise NotImplementedError('Stream metadata is read only')

	def _close(self, *args, **kwargs):
		'''Actual close
		Actually implement the close functionality of the stream's underlying object. By default expects the underlying object to have a close method.
		'''

		LOGGER.debug('Actual stream close. Just calling the close() method on it.')
		return self._stream.close(*args, **kwargs)

	@abc.abstractmethod
	def _open(self):
		'''Actual open
		Actually implement the open functionality of the stream's underlying object.
		'''

		pass

	def _read(self, *args, **kwargs):
		'''Actual read
		Actually implement the read functionality of the stream's content. By default expects the underlying object to have a read method.
		'''

		LOGGER.debug('Actual stream read. Just calling the read() method on it with: %s | %s', args, kwargs)
		return self._stream.read(*args, **kwargs)

	def _write(self, b, *args, **kwargs):
		'''Actual write
		Actually implement the write functionality of the stream's content. By default expects the underlying object to have a write method.
		'''

		LOGGER.debug('Actual stream write. Just calling the write() method on it with: %s | %s', ('[{} bytes]'.format(len(b)),) + args, kwargs)
		return self._stream.write(b, *args, **kwargs)

	@classmethod
	def calculate_stream(cls, *args, **kwargs):

		LOGGER.debug('Calculating the sums for stream with: %s | %s', args, kwargs)
		kwargs['mode'] = 'rt'
		stream = cls(*args, **kwargs)
		stream.open(*stream._open_arg_and_kwargs[0], **stream._open_arg_and_kwargs[1])
		stream.close()
		return stream


	def close(self, *args, **kwargs):
		'''Close stream
		Close the underlying stream and make the sums available
		'''

		if self._is_open is None:
			raise RuntimeError('No stream has been opened, nothing to close')
		elif self._is_open:
			self._is_open = False
			LOGGER.debug('Closing stream: %s', self._stream)
		else:
			LOGGER.warning('Closing an already closed stream. This might fail depending on the underlying implementation')

		close_result = self._close(*args, **kwargs)

		if (not self._is_synchronous) and (len(self._sums) + len(self._hashes)):

			orignal_stream, original_is_synchronous, original_open_arg_and_kwargs = self._stream, self._is_synchronous, self._open_arg_and_kwargs

			LOGGER.debug('Reading the non-synchronous stream again to calculate sums: %s', self._stream)
			self._is_open, self._is_synchronous, self._open_arg_and_kwargs[1]['mode'] = None, True, 'rb'
			with self as stream_obj:
				with open(os.devnull, mode = 'wb') as dev_null:
					shutil.copyfileobj(stream_obj, dev_null)

			self._stream, self._is_synchronous, self._open_arg_and_kwargs = orignal_stream, original_is_synchronous, original_open_arg_and_kwargs

		if self._close_callback is not None:
			LOGGER.debug('Calling the close callback: %s', self._close_callback)
			self._close_callback(self)

		return close_result

	def items(self):
		'''Items magic
		Override the builtin items using the custom keys method.
		'''

		return [(key, self[key]) for key in self.keys()]

	def keys(self):
		'''Keys magic
		Expose the hashes dict keys along the current sums.
		'''

		return list(self._sums.keys()) + list(self._hashes.keys())

	def open(self, *args, **kwargs):
		'''Open stream
		Open the underlying stream and make the sums available
		'''

		if self._is_open is None:
			self._is_open = True
			self._open_arg_and_kwargs = [args, kwargs]
			LOGGER.debug('Opening stream with: %s | %s', args, kwargs)
			self._stream = self._open(*args, **kwargs)
			return self._stream
		elif self._is_open:
			raise NotImplementedError('Re-opening a stream mid way is not supported (it would break the sums in many ways)')
		elif not self._is_open:
			raise NotImplementedError('The stream is already closed. These objects are not reusable')

	@staticmethod
	def parse_mode(mode):
		'''Parse the mode
		Processes the mode string and returns: live, synchronous

		If "live" is True means that the stream content is being changed by some kind of write operation, probably. Otherwise is a pure read operation meaning that the stream content is static.

		If "synchronous" is True it means that it would be a linear read/write of binary content (the data being written matches the final data on the storage), which allows for the sum to happen during the regular read/write operations. Otherwise it would have to wait until the stream is closed to read the binary content synchronously again and get the sums (higher cost, which grows linearly with the stream size).
		'''

		LOGGER.debug('Parsing mode: %s', mode)

		mode = set(mode)

		read_or_write = {'r', 'w', 'x', 'a'} & mode
		if not read_or_write:
			read_or_write = {'r'}
		elif len(read_or_write) > 1:
			raise ValueError("Pick one of create(x)/read(r)/write(w)/append(a) mode.")
		LOGGER.debug('Mode is x/r/w/a?: %s', read_or_write)
		updating = True if '+' in mode else False
		LOGGER.debug('Mode is updating?: %s', updating)

		binary_or_text = {'b', 't'} & mode
		if not binary_or_text:
			LOGGER.warning('Inferring stream will be in binary mode since none was specified (binary or text/encoded)')
		if len(binary_or_text) > 1:
			raise ValueError("Pick binary (b) or text (t) mode, can't do both at the same time.")
		LOGGER.debug('Mode is b/t?: %s', binary_or_text)

		if ('r' in read_or_write) and not updating:
			if 'b' in binary_or_text:
				return False, True
			else:
				return False, False

		if ({'w', 'x'} & read_or_write) and ('b' in binary_or_text) and not updating:
			return True, True
		else:
			return True, False

	def read(self, *args, **kwargs):
		'''Synchronous hash read
		Calculate sums and hashes while the reading happens.
		'''

		if self._is_open is None:
			raise RuntimeError('No stream has been opened, nothing to read from')
		elif not self._is_open:
			raise NotImplementedError('The stream is already closed. Operation not supported at this point')

		data = self._read(*args, **kwargs)

		if self._is_synchronous:
			LOGGER.debug('Updating sums on read')
			if 'size' in self._sums:
				self._sums['size'] += len(data)
			if 'adler32' in self._sums:
				self._sums['adler32'] = zlib.adler32(data, self._sums['adler32'])
			if 'crc32' in self._sums:
				self._sums['crc32'] = zlib.crc32(data, self._sums['crc32'])

			for hash_sum in self._hashes.values():
				hash_sum.update(data)

		return data

	def write(self, b, *args, **kwargs):
		'''Synchronous hash write
		Calculate sums and hashes while the writting happens.
		'''

		if self._is_open is None:
			raise RuntimeError('No stream has been opened, nothing to write into')
		elif not self._is_open:
			raise NotImplementedError('The stream is already closed. Operation not supported at this point')

		if self._is_synchronous:
			LOGGER.debug('Updating sums on write')
			if 'size' in self._sums:
				self._sums['size'] += len(b)
			if 'adler32' in self._sums:
				self._sums['adler32'] = zlib.adler32(b, self._sums['adler32'])
			if 'crc32' in self._sums:
				self._sums['crc32'] = zlib.crc32(b, self._sums['crc32'])

			for hash_sum in self._hashes.values():
				hash_sum.update(b)

		return self._write(b, *args, **kwargs)


class FileWrapperStream(AbstractBaseStream):
	'''Stream in a file
	Wrap a file on an existing filesystem and treat it as a stream.

	ToDo:
	- Make stream reads reusable.
	'''

	def _open(self, file_path, *args, **kwargs):
		'''Open the file
		Store the opened underlying file.
		'''

		self._file_path = pathlib.Path(file_path)
		LOGGER.debug('Opening file "%s" with: %s | %s', self._file_path, args, kwargs)
		return self._file_path.open(*args, **kwargs)


if __name__ == '__main__':
	simplifiedapp.main()

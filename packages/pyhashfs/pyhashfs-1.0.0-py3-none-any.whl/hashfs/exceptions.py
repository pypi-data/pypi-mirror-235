#!python
'''HashFS; Exceptions
Exception tree for the HashFS module
'''

######################## Root ######################

class HashFSError(Exception):
	'''Base exception for the HashFS module'''

	pass


class HashFSParametersError(ValueError, HashFSError):
	'''Error with the provided parameter'''

	pass


class StreamNotFoundError(HashFSError):
	'''The requested stream wasn't found'''

	pass


####################### BasicHash #########################

class BasicHashFSError(HashFSError):
	'''Base exception for the BasicHashFS version'''

	pass


class StreamPathError(BasicHashFSError):
	'''Error with the path to a stream'''

	pass


class ZeroFileError(BasicHashFSError):
	'''Error with the zero file on a BasicHashFS'''

	pass

#!python
'''HashFS; Utils
Utility functions for the HashFS module
'''

import logging

import simplifiedapp

from .exceptions import HashFSParametersError

LOGGER = logging.getLogger(__name__)

def fsck(*args, n = False, c = False, v = False):
	'''Filesystem check
	Check the file system for known errors.

	Supported parameters:
	- n = Make no changes to the filesystem; just perform a dry run
	- c = Check file sums; the whole file system would have to be read, very expensive.
	- v = Be verbose; increase the internal logging level

	ToDo:
	- Find empty directories
	- Find invalid directory names (wrong length, wrong characters)
	- Confirm file sums (look for corrupted/invalid content)
	- Implement the parameters
	'''

	raise NotImplementedError('FSCK is not implemented yet')

def int_range_check(range_min = None, range_max = None, **kwargs):
	'''Integer range check
	Check that the provided integers (in the form of var_name=var_value) are withing the range requested. Raise an exception on error.
	'''

	if range_min is not None:
		for var_name, var_value in kwargs.items():
			if var_value < range_min:
				raise HashFSParametersError('The "{}" value should be equal or greater than {}'.format(var_name, range_min))

	if range_max is not None:
		for var_name, var_value in kwargs.items():
			if var_value > range_max:
				raise HashFSParametersError('The "{}" value should be equal or lesser than {}'.format(var_name, range_max))

def type_check(type_, **kwargs):
	'''Variable type checks
	Check that the provided variables (in the form of var_name=var_value) are of certain type. Raise an exception on error.
	'''

	for var_name, var_value in kwargs.items():
		if not isinstance(var_value, type_):
			raise HashFSParametersError('The "{}" value MUST be an of type {}'.format(var_name, type_))

if __name__ == '__main__':
	simplifiedapp.main()

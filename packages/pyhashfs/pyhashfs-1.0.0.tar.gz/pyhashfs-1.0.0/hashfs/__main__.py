#!python
'''pyHashFS, A python implementation of HashFS
A hash file system (HashFS) is a content addressable file system, where the content (files) are identified by its metadata, as in hash sums (and other sums) instead of the classic file name (including the path). By using inmutable and directly related information to identify a file (content) some application problems are rendered moot, like file duplication.

This implementation uses the hashlib standard module extensively, to calculate the different sums. It also has support for adler32 and crc32 sums via the zlib standard module.

This is the executable script
'''

import simplifiedapp

from . import *

simplifiedapp.main()

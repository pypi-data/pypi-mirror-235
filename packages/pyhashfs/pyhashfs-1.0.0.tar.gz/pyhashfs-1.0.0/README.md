# pyHashFS - A python implementation of HashFS

A **hash file system** (HashFS) is a content addressable file system, where the content (files) are identified by its metadata, as in hash sums (and other sums) instead of the classic file name (including the path). By using inmutable and directly related information to identify a file (content) some application problems are rendered moot, like file duplication.

This implementation uses the `hashlib` standard module extensively, to calculate the different sums. It also has support for `adler32` and `crc32` sums via the `zlib` standard module.

## overlay.BasicHashFS

This is a very simple implementation of the HashFS concept. It works as an overlay for an existing and underlying filesystem, and it manages directories and files on it using the `pathlib` standard module. This version is extremely vocal about directory and file structures and names. It's not meant to be used over existing content but to be left alone in some subdirectory.

This version uses 2 sums: the file **size** and **a hash sum** defined on filesystem creation (any of the ones supported by `hashlib` on the system doing the creation). The size number and the hash string are *encoded* on the directory and final file names. The path to a file, stripped of the directory separators, would contain the size and hash. The class has all the logic needed to parse such encoding and to put streams (files) where they need to go.

This module leverages the `simplifiedapp` module, which allows to use the code in the command line. Assuming there's a virtual environment with this module installed there (in `venv`) and activated:

You can create a new file sytem by running `python -m hashfs BasicHashFS test_fs create test_fs`

You could import some files (just everything on the virtual environment in this case) with `python -m hashfs BasicHashFS test_fs import_tree venv`

You can get the list of everything on the file system with `python -m hashfs BasicHashFS test_fs stream_allocation_table`

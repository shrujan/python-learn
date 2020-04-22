


import shutil
shutil.copy('hello.txt', 'target.txt')
'''
shutil.copy2(src, dst) 
Similar to shutil.copy(), but metadata is copied as well in fact,
this is just shutil.copy() followed by copystat().
'''

shutil.copytree('c:/ASL_June','C:/Python_testing66')
'''
Recursively copy an entire directory tree rooted at src.
The destination directory, named by dst, must not already exist; it will be
created as well as missing parent directories. Permissions and times of
directories are copied with copystat(), individual files are copied using
shutil.copy2().
'''

#shutil.rmtree('C:/Python_testing2')
'''
Delete an entire directory tree
'''

'''
shutil.move(src, dst)
Recursively move a file or directory (src) to another location (dst).

If the destination is a directory or a symlink to a directory,
then src is moved inside that directory.

The destination directory must not already exist. If the destination
already exists but is not a directory, it may be overwritten

'''


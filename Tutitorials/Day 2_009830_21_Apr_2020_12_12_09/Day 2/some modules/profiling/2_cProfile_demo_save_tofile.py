import cProfile
import re
cProfile.run('re.compile("foo|bar")', 'restats') #'restats' is a file name
"""
Instead of printing the output at the end of the profile run,
you can save the results to a file by specifying a filename to the run() function:
"""

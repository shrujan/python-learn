# -*- coding: cp1252 -*-


#1_cProfile_demo.py
import cProfile
import re
cProfile.run('re.compile("foo|bar")')

"""
cProfile and profile provide deterministic profiling of Python programs.
A profile is a set of statistics that
describes how often and for how long various parts of the program executed.
These statistics can be formatted
into reports via the pstats module.
cProfile is recommended for most users; it’s a C extension with reasonable overhead that
makes it suitable for
profiling long-running programs.

"""


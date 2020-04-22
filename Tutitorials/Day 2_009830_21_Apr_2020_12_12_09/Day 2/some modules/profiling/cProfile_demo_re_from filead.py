import pstats
p = pstats.Stats('restats')
p.strip_dirs().sort_stats(-1).print_stats()

"""
The pstats.Stats class reads profile results from a file and formats them in various ways.

The file cProfile can also be invoked as a script to profile another script. For example:


python -m cProfile [-o output_file] [-s sort_order] myscript.py

5
-o writes the profile results to a file instead of to stdout

-s specifies one of the sort_stats() sort values to sort the output by. This only applies when -o is not supplied.

The pstats module’s Stats class has a variety of methods for manipulating and printing the data saved into a profile results file:

"""

"""
You might try the following sort calls:
The first call will actually sort the list by function name, and the second call will print out the statistics.
"""
import pstats
p = pstats.Stats('restats')
p.sort_stats('name')
p.print_stats()

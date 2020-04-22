"""
If you were looking to see what functions were looping a lot, and taking a lot of time, you would do:

"""
import pstats
p = pstats.Stats('restats')
p.sort_stats('time').print_stats(10)

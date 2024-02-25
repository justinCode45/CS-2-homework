import pstats
from pstats import SortKey

p = pstats.Stats('output.pstats')

p.sort_stats(SortKey.CUMULATIVE).print_stats(30)
p.sort_stats(SortKey.TIME).print_stats(30)
"""
Itertools
"""

import itertools as it

"asdfsafd"[2:4]


g = (i for i in range(10))
# print(g[2:5])

# Aus einem Iterator was rausschneiden.
print(list(it.islice(g, 2, 5)))

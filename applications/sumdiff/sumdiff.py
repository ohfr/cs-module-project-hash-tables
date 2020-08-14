"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

from itertools import permutations
#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)




def f(x):
    return x * 4 + 6

# Your code here
combos = list(permutations(q, 4))

lookup = {}

def findAll(combo):
    if combo in lookup:
        return lookup[combo]
    else:
        v = f(combo[0]) + f(combo[1])



    
    
for item in combos:
    findAll(item[0],item[1], item[2], item[3])

#Intermediate Python itertools
from itertools import product, permutations

a = [1, 2, 3, 4]
b = [3, 4]
prod = product(a, b)
print(list(prod))

perms = permutations(a)
print(len(list(perms)))
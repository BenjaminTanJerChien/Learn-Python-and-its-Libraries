#Intermediate Python Sets 

intSet = set()
mySet = {1, 2, 3, 4, 4, 5, 6, 7, 7, 7, 7}
'''cannot take duplicates
   mutable 
   '''

print(mySet)
'''.add() , .remove(), .discard(), clear , pop()'''

odds = {1, 3, 5, 7, 9, 11}
evens = {0, 2, 4, 6, 8, 10}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes) #or intersection_update to chnage the set
print(i)

'''.diffrence()'''
'''.update() adds them tgt'''
'''.issubset() // .isdisjoint()'''
'''frozenset = immutable version of a set'''
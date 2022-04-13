#Intermediate Python Tuples

'''tuple is immutable '''

myTuple = ("max", 889, "test")
alsoTuple = "max", 889, "test"
notTuple = ("max")

print(myTuple[1])

for i in myTuple:
    print(i)

if "max" in myTuple:
    print("yes")
else:
    print("no")

print(myTuple.count("max"))
print(myTuple.index("max"))

'''very similar to a list but it's just not mutable and more effecient'''

name, age, type = myTuple
print(name)
print(age)
print(type)

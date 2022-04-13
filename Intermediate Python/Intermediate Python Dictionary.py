#intermediate python Dictionary 

an_example_dict = {"key" : "value"}
myDict = {"name" : "Benjamin Tan", "age" : 20, "gender" : "male", "boosted" : True}
myDictalso = dict(name="Joash Tan", age=19, gender="male", boosted=True)

print(myDict["name"])
print(myDictalso)

for key in myDict:
    print(key)


for key in myDict.values():
    print(key)


'''can use .copy() / dict(oriDict) to make a copy'''

myDict.update(an_example_dict)
print(myDict)
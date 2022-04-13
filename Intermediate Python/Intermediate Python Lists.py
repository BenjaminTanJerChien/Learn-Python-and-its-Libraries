#Intermediate Python Lists 
'''list is created of a square bracket
it can contain mutilple types of data and duplicates of said data
'''

myList = ["banana", "Cherry", "apple"]

print(myList)

for i in myList:
    print(i)

if "banana" in myList:
    print("yes")

print(len(myList))

myList.append("Lemon")
print(myList)

myList.insert(1, "blueberry")
print(myList)

myList.pop()
print(myList)

myList.remove("apple")
print(myList)

myList.reverse()
print(myList)


myList.sort()
print(myList)

myList.clear()
print(myList)

newList = [0] * 5
otherList = [1, 2, 3, 4, 5]
addedList = newList + otherList
print(addedList)

print(addedList[3:])


'''copy can be made with .copy(), list() or [:]'''

ascendingList = [1, 2, 3, 4, 5]
b = [i*i for i in ascendingList]
print(b)
#Intermediate Python Strings
string = "This is a normal string"
print(string)
char = string[-5:]
print(char)
rev = string[::-1]
print(rev)
stripped = string.strip()
print(stripped)
print(string.startswith("This"))
print(string.endswith("string"))
print(string.find("n")) # -1 if the item is not found
print(string.count("a"))
print(string.replace("a normal", "an unusual"))
new_list = string.split()
print(new_list)
print('-'.join(new_list))
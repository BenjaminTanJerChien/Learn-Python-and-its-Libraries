
x = input("Roman Numeral: ")

def romanToInt(roman):
    roman_hashmap = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    total = 0
    for i in range(len(roman)):
        if i + 1 < len(roman) and roman_hashmap[roman[i]] < roman_hashmap[roman[i + 1]]:
            total -= roman_hashmap[roman[i]]
        else:
            total += roman_hashmap[roman[i]]
    return total

print(romanToInt(x))

#Intermediate Python Collections
from collections import Counter, namedtuple, deque
string = "aaaabbbbbddddcccddd"
mycounter = Counter(string)
print(mycounter.most_common(2)[0])

point = namedtuple('Point', 'x,y')
pt = point(1, -4)
print(pt)

d = deque()
d.append(1)
d.appendleft(2)
print(d)

for i in d:
    print(i)
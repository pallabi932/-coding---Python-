a=[1, 10, 2]
b=a
c= a.copy()b.append(3)c.append(5)print (a)
print(b)
print(c)

import copy
a=[[1, 2], [3, 4]]
b=copy.deepcopy(a)
b(0).append(10)
print(a)
print (b)

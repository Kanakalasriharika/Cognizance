
from numpy import *
p=array([])
q=int(input('First Number:'))
r=int(input('Last Number:'))
for x in range(q,r):
    p=append(p,x)
    for x in range(5):
        p=append(p,0)
p=append(p,r)
print(p)

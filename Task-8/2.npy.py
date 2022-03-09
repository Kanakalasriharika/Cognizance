#consider two random array A and B, check if they are equal or not
import numpy as np
x = np.array([1 ,0, 1, 0 ,1, 0])
y = np.array([1 ,0, 1, 1 ,0 ,1])
array_len=len(x)
for a in range(array_len):
    if x[a] == y[a] :       
        result=0
    else :
        result=1
if result==0:
    
    print("They are equal ")
else :
    
    print("They are not equal ")

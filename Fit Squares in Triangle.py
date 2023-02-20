# solution as follows

import math

t = int(input())
for i in range(t):
    b = int(input())
    s = math.floor(b//2)
    #remember that /' returns a decimal value
    print(((s-1)*(s))//2)   

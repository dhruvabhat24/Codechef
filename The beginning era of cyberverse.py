# Solution as follows

import math

t=int(input())
for _ in range(t):
    N,K=map(int,input().split())
    #math.ceil rounds up to the nearest integer.
    #math.floor rounds down to the nearest integer
    print(math.floor(K/N))

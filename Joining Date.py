# Solution as follows

import math

t = int(input())
for i in range(t):
    a,b=map(int, input().split())
    print(math.ceil(a/5)-math.ceil(b/5))

# Solution as follows

t = int(input())
for i in range(t):
    N, M = map(int,input().split())
    
    #There are 2 conditions given in the problem
    #1. All friends get equal candies -> hence N % M = 0
    #2. Each friend gets even number of candies
    if (N%M == 0) and ((N//M)%2 == 0):
        print('Yes')
    else:
        print('No')

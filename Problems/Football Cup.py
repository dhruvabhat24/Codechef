# Solution as follows

t=int(input())
for i in range(t):
    X, Y = map(int,input().split())
    #The 1st condition was insufficient
    if X==Y and (X>0 or Y>0):
        print('YES')
    else:
        print('NO')
    

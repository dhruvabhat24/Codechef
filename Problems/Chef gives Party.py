# Solution as follows

t = int(input())
for i in range(t):
    N,X,K = map(int,input().split())
    #Incorrect syntax
    if(N*X <= K):   
        print("YES")
    else:
        print("NO")

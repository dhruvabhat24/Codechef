# Solution as follows

t = int(input())
for i in range(t):
    n,k=map(int, input().split())
    p=list(map(int, input().split()))

    l=[]
    for i in p:
        if(i>k):
            l.append(k)
        else:
            l.append(i)
    
    #Logical condition was incorrect
    print(sum(p) - sum(l))

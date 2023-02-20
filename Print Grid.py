# Solution as follows

for t in range(int(input())):
    n,m = map(int, input().split())
    if(n%2!= 0 and m%2!=0):
        print(n+m-1)
    elif(n%2!= 0 and m%2==0):
        print(m)
    elif(n%2== 0 and m%2!=0):
        print(n)
    #if none of the above conditions are met, we need to execute the following condition
    else:
        print(0)
    

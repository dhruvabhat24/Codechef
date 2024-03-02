# Solution as follows

t = int(input())            
for i in range(t):          
    A, C = map(int, input().split())
    
    #Borrow the solution template from the sub-components
    if A%2 == 0 and C%2 == 0:
        B = (A + C)//2
        print(B)
    elif A%2 != 0 and C%2 != 0:
        B = (A + C)//2
        print(B)
    else:
        print(-1)

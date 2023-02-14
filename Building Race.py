# Solution as follows

t = int(input())
for i in range(t):
    A, B, X, Y = map(int,input().split())
    
    #Time taken for Chef to get to the ground floor = A / X minutes
    #Time taken for Chefina to get to the ground floor = B / Y minutes
    if A/X > B/Y:
        print('Chefina')
    elif A/X < B/Y:
        print('Chef')
    else:
        print('Both')

# Solution as follows

t = int(input())
for i in range(t):
    W, X, Y, Z = map(int,input().split())
    
    #Condition 1: Check if ingredient can be weighed by all 3 weight together
    if W == (X + Y + Z):
        print('YES')
    #Condition 2: Check if ingredient can be weighed by any 2 weights
    elif (W == (X + Y)) or (W == (X + Z)) or (W == (Y + Z)):
        print('YES')
    #Condition 3: Check if ingredient can be weighed by any 1 weight
    elif (W == X) or (W == Y) or (W == Z):
        print('YES')
    #Condition 4: If neither of the 3 conditions above is met
    else:
        print('NO')

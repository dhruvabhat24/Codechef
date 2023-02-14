# Solution as follows

X = 3
Y = 4
Z = 12
print('The animal on the farm is', 'ANY')

X = 3
Y = 5
Z = 13
print('The animal on the farm is', 'NONE')

X = 3
Y = 5
Z = 10
print('The animal on the farm is', 'DUCK')

X = 3
Y = 5
Z = 9
print('The animal on the farm is', 'CHICKEN')
## solving sub components
#Solution as follows
X = 3
Y = 4
Z = 12
if (Z%X == 0) and (Z%Y == 0):
    print('Z is divisible by both X and Y')
elif (Z%X == 0):
    print('Z is divisible only by X')
elif (Z%Y == 0):
    print('Z is divisible only by Y')
else:
    print('Z is divisible by neither X nor Y')

X = 3
Y = 5
Z = 13
if (Z%X == 0) and (Z%Y == 0):
    print('Z is divisible by both X and Y')
elif (Z%X == 0):
    print('Z is divisible only by X')
elif (Z%Y == 0):
    print('Z is divisible only by Y')
else:
    print('Z is divisible by neither X nor Y')
    ## Complete problem
    # Solution as follows

t = int(input())            
for i in range(t):          
    X, Y, Z = map(int, input().split())
    
    #Borrow the template from our sub-component
    if (Z%X == 0) and (Z%Y == 0):   
        print('ANY')
    elif (Z%X == 0):
        print('CHICKEN')
    elif (Z%Y == 0):
        print('DUCK')
    else:
        print('NONE')

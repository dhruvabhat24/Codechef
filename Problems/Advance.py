# Solution as follows

t=int(input())
for i in range(t):
    #We need to declare the type of variable
    X, Y = map(int, input().split())
    #The original code also had a logical error
    if Y>=X and Y<=(X+200):
        print('YES')
    else:
        print('NO')

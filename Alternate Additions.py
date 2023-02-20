# Solution as follows

t = int(input())
for i in range(t):
    A, B = map(int, input().split())
    
    diff = B - A
    
    if (B - A)%3 == 0:
        print('YES')
    elif (B - A)%3 == 1:
        print('YES')
    else:
        print('NO')

# Solution as follows

t=int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a%3==0 or b%3==0:
        print(0)
    else:
        if abs(a-b)%3==0:
            #Expected output for this condition is switched
            print(1)
        else:
            print(2)

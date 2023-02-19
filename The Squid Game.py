# Solution as follows

t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int,input().split()))
    
    total_prize = sum(A)
    max_prize = total_prize - min(A)
    
    print(max_prize)

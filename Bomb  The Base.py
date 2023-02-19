# Solution as follows
#Find the index of the highest element where A[i] < X

t = int(input())
for i in range(t):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    i = 0
    attack_house = 0
    
    while i < N:
        #Find the index of the highest element where A[i] < X
        if A[i] < X:            
            #Lists are 0 indexed. So we add 1
            attack_house = i + 1    
        i = i + 1
    
    print(attack_house)

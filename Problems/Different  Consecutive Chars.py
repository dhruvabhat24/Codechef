# Solution as follows

t = int(input())
for i in range(t):
    N = int(input())
    S = input()
    
    i = 0
    count = 0
    
    while i < (N-1):
        #Count the indices where adjacent elemnts are the same
        if S[i] == S[i+1]:
            count = count + 1
        i = i + 1
    
    print(count)
        
    
    
    

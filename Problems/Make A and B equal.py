# Solution as follows

t = int(input())
for i in range(t):
    A, B = map(int,input().split())
    
    #Decare variables for lower and higher of the 2 numbers
    minAB = min(A,B)
    maxAB = max(A,B)
    flag = 0
    
    while minAB <= maxAB:
        #condition is met, hence set flag = 1
        if minAB == maxAB:  
            flag = 1
            break
        else:
            #update the minimum value as per the problem statement
            minAB = minAB*2 
        
    if flag == 1:
        print('YES')
    else:
        print('NO')

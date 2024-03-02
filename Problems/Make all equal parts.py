# Solution as follows

t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int,input().split()))
    
    #sorting the array because we want to find most frequent element
    A = sorted(A)                       
    count = 1
    highest_count = 1
    i = 0
    while i<(N-1):
        if A[i] == A[i+1]:
            #Increases count whenever adjacent elements are equal
            count = count + 1           
            if highest_count < count:      
                #Updates the global counter 
                highest_count = count
        #If adjacent elements are not equal, resets count to 1
        else:                           
            count = 1
        i = i + 1
    
    print(N - highest_count)

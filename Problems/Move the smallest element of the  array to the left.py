# Solution as follows

t = int(input())
for i in range(t):
    A = list(map(int,input().split()))
    N = len(A)
    
    # We first find the smallest element, and which index it is in.
    minElement = A[0]
    minElementIndex = 0
    i = 1
    while i < N:
        if A[i] < minElement:
            # If we find an element smaller than the previous smallest, we update
            minElement = A[i]
            minElementIndex = i
        i = i + 1
    
    #We are starting the operation from index of the smallest element
    i = minElementIndex
    while i > 0:
        #Swap the A[i] and A[i-1]
        A[i],A[i-1] = A[i-1], A[i]      
        i = i - 1
    
    print(*A)

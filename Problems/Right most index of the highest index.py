# Solution as follows

t = int(input())
for i in range(t):
    A = list(map(int, input().split()))
    # length of the array A
    n = len(A)      
    # Initialise the rightmost index to 0
    right = 0       
    # Initilise the largest value to -100. The smallest element in A is -100
    large = -100    
    
    i = 0
    while i<n:
        # Here - we need to check if A[i] '=' large so that we can update the variable 'right'
        if A[i] >= large:       
            large = A[i]
            right = i
        i = i + 1
    
    print(large, right)

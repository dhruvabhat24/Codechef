# Solution as follows

t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    
    #Note that initialising small = 0 and large = 0 will be wrong.
    #If the smallest value in the array is larger than small - then our answer will be incorrect.
    #Can you think of a similar case why large = 0 will be wrong?
    small = A[0]
    large = A[0]
    
    i = 0
    #Loop through all elements of the array
    while i<len(A):         
        #If any element is higher that the largest element found so far, replace its value
        if A[i] > large:    
            large = A[i]
        #If any element is smaller that the smallest element found so far, replace its value
        if A[i] < small:    
            small = A[i]
        i = i + 1
    
    print(small, large)

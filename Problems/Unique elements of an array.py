# Solution as follows

t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int,input().split()))
    
    unique = []
    freq = []
    
    # set() returns the unique elements in a list
    unique = list(set(A))       
    # sort the list unique in an ascending order
    unique.sort()               
    
    for i in unique:
        # count() returns the count of an element in a list
        freq.append(A.count(i)) 
        
    # print(*list) returns only the values
    print(*unique)              
    print(*freq)

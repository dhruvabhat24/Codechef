# Solution as follows

t = int(input())
for i in range(t):
    N = int(input())
    A = []
    for i in range(N):
        A.append(i+1)
    #print the array A
    print(A)                
    #print only the elements from array A
    print(*A)               
    #print the array A sorted in descending order
    A.sort(reverse = True)
    print(A)                

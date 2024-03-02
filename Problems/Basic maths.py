# Solution as follows

t = int(input())
for i in range(t):
    n = int(input())
    
    #declare an empty list to hold all divisors
    divisors = []
    i = 1
    while i <= n:
        #check if n is divisible by each i
        if n%i == 0:            
            #append each i to the list which meets this condition
            divisors.append(i)
        i = i + 1
    
    print(*divisors)
    

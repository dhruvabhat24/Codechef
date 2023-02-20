# Solution as follows

t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    
    #create a list to hold divisors of A and B
    divisors_AandB = []             
    i = 1
    while i <= min(A,B):
        #i needs to divide both A and B
        if A%i == 0 and B%i == 0:   
            #append the integer to the list
            divisors_AandB.append(i)
        i = i + 1
    
    #gcd is the greatest common divisor
    gcd = max(divisors_AandB)       
    #math property
    lcm = (A*B)//(gcd)              
    
    print(gcd, lcm)

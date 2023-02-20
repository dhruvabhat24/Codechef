# Solution as follows

t = int(input())
for i in range(t):
    t1, t2, r1, r2 = map(int,input().split())
    
    #proportionality constants for planet 1 and planet 2
    planet1 = (t1**2)/(r1**3)   
    planet2 = (t2**2)/(r2**3) 
    
    if planet1 == planet2:
        print('Yes')
    else:
        print('No')

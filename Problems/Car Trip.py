# Solution as follows

t=int(input())
for j in range(t):
    X=int(input())
    if X<=300:
        #Minimum rental is 10 per km for 300 kms 
        print(300*10)
    else:
        print(X*10)
    

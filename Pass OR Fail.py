# Solution as follows

t = int(input())
for i in range(t):
    N, X, P = map(int,input().split())
    
    #Equation for calculating Chef's score
    score = X*3 + (-1)*(N-X)
    
    #Check conditions for Chef's score
    if score >= P:
        print('PASS')
    else:
        print('FAIL')

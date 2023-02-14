# Solution as follows

N = 10
M = 10
print('The number of extra shoes that Chef has to buy is 10')

N = 5
M = 10
print('The number of extra shoes that Chef has to buy is 5')

N = 15
M = 10
print('The number of extra shoes that Chef has to buy is 20')
#sub ccomponents
#Solution as follows

N = 10
M = 10
if N <= M:
    print('We need to buy',N,'shoes')
else:
    print('We need to buy',(2*N-M),'shoes')


N = 15
M = 10
if N <= M:
    print('We need to buy',N,'shoes')
else:
    print('We need to buy',(2*N-M),'shoes')

#complete
# Solution as follows

t = int(input())
for i in range(t):
    N, M = map(int, input().split())
    
    #Borrow the template from the sub-problem
    if N <= M:          
        print(N)
    else:
        print(2*N-M)

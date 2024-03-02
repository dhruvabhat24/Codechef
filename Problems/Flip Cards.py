# Solution as follows

N = 10
X = 3
print('The number of cards we need to flip is 3')

N = 10
X = 7
print('The number of cards we need to flip is 3')

N = 10
X = 4
print('The number of cards we need to flip is 4')

N = 10
X = 6
print('The number of cards we need to flip is 4')
#solving sub Components
#Solution as follows

N = 10
X = 4
option1 = X
option2 = N-X
print(min(option1, option2))


N = 10
X = 6
option1 = X
option2 = N-X
print(min(option1, option2))
 

#complete 
# Solution as follows

t = int(input())
for i in range(t):
    N, X = map(int,input().split())
    
    #Borrow the template from the sub-problem
    option1 = X         
    option2 = N-X
    print(min(option1,option2))

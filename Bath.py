# Solution as follows

X = 15
Y = 1
print('The maximum number of people that can take a bath is 7')

X = 15
Y = 2
print('The maximum number of people that can take a bath is 3')

X = 15
Y = 3
print('The maximum number of people that can take a bath is 2')

X = 15
Y = 4
print('The maximum number of people that can take a bath is 1')
#sub components
# Solution as follows

X = 15
Y = 1
#count of completely filled buckets
buckets_filled = X//Y        
people = buckets_filled//2
print(people)

X = 15
Y = 3
buckets_filled = X//Y
people = buckets_filled//2
print(people)
#complete
# Solution as follows

t = int(input())
for i in range(t):
    X, Y = map(int,input().split())
    
    #borrow the code from the sub-problem
    count = X//Y        
    people = count//2
    print(people)

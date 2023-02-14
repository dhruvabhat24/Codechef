# Solution as follows

X = 18
print('minimum number of problems Chef marked incorrect are 0')

X = 19
print('minimum number of problems Chef marked incorrect are 2')

X = 20
print('minimum number of problems Chef marked incorrect are 1')

X = 7
print('minimum number of problems Chef marked incorrect are 2')
#solving sub components
#Solution as follows

X = 30
if X%3 == 0:
    print('Number of questions incorrctly solved is 0')
elif (X+1)%3 == 0:
    print('Number of questions incorrctly solved is 1')
else:
    print('Number of questions incorrctly solved is 2')
    
X = 34
if X%3 == 0:
    print('Number of questions incorrctly solved is 0')
elif (X+1)%3 == 0:
    print('Number of questions incorrctly solved is 1')
else:
    print('Number of questions incorrctly solved is 2')
#Complete problem
# Solution as follows

t = int(input())            
for i in range(t):          
    X = int(input())
    
    #Borrow the template from the sub-component, replace the relevant output
    if X%3 == 0:        
        print(0)        
    elif (X+1)%3 == 0:
        print(1)
    else:
        print(2)

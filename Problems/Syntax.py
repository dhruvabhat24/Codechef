t = int(input())
for i in range(t):
    #Accept 1 integer as input.
    N = int(input())        
    #Check if N is less than or equal to 100
    if N<=100:
        print('Good')
    #2nd condition in the problem
    elif N>100 and N<=200:
        print('Better')
    #3rd condition in the problem
    else:                   
        print('Best')

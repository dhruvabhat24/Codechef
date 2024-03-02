# Solution as follows

X = 18
Y = 3
print("Minimum moves required to reach stair",X,"is 6")

X = 19
Y = 3
print("Minimum moves required to reach stair",X,"is 7")

X = 2
Y = 3
print("Minimum moves required to reach stair",X,"is 2")
#sub components
# Solution as follows

X = 19
Y = 3
if X%Y == 0:            
    print("Count of moves is",X//Y)
else:
    print("Count of moves is",(X//Y) + (X%Y))

X = 20
Y = 3
if X%Y == 0:            
    print("Count of moves is",X//Y)
else:
    print("Count of moves is",(X//Y) + (X%Y))
#Complete
# Solution as follows

t = int(input())
for i in range(t):
    X, Y = map(int,input().split())
    
    #Borrowing the template from the sub-problem
    if X%Y == 0:        
        print(X//Y)
    else:
        print((X//Y) + (X%Y))

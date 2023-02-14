# Solution as follows

t = int(input())
for i in range(t):
    X = int(input())
    
    #Condition 1: Minimum coins if amount can be provided by only rupees 10 coins
    if X%10 == 0:
        print(X//10)
    #Condition 2: Minimum coins if amount can be provided by multiple rupees 10 coins and only 1 rupees 5 coin
    elif X%5 == 0:
        print((X//10) + 1)
    #Condition 3: If neither of the 2 conditions above can be met    
    else:
        print(-1)

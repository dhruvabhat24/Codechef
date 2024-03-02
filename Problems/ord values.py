# Solution as follows

t = int(input())
for i in range(t):
    S = input()
    A = []
    
    for i in S:
        #Converts a character into its ASCII value
        A.append(ord(i))    
    
    print(*A)

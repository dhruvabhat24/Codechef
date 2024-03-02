# Solution as follows

t = int(input())
for i in range(t):
    S = str(input())
    A = ""
    #Use for loop to loop through every character of S
    for i in S:
        #Adds the character to the end of A
        A = A + i
    
    B = ""
    #Use for loop to loop through every character of S
    for i in S:
        #Adds the character to the start of B
        B = i + B
    
    print(A)
    print(B)

# Solution as follows

t = int(input())
for i in range(t):
    S = input()
    T = input()
    
    M = ""
    i = 0
    while i < len(S):
        #If the i element in S and T are the same, then the i element in M is G
        if S[i] == T[i]:
            M = M + 'G'
        #If the i element in S and T are not the same, then the i element in M is B
        else:
            M = M + 'B'
        i = i + 1
    
    print(M)

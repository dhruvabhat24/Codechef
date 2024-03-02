# Solution as follows

t = int(input())
for i in range(t):
    S = str(input())
    
    string_Length = len(S)
    i = 0
    flag = 0
    while i < (string_Length-2):
        #if any element is a vowel, and its next 2 elements are vowels, then our condition is met
        if S[i]=='a' or S[i]=='e' or S[i]=='i' or S[i]=='o' or S[i]=='u':
            if S[i+1]=='a' or S[i+1]=='e' or S[i+1]=='i' or S[i+1]=='o' or S[i+1]=='u':
                if S[i+2]=='a' or S[i+2]=='e' or S[i+2]=='i' or S[i+2]=='o' or S[i+2]=='u':
                    flag = 1
                    break
        i = i + 1
    
    if flag == 1:
        print('Happy')
    else:
        print('Sad')

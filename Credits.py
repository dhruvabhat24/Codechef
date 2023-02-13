t = int(input())
for i in range(t):
    X, Y, Z = map(int, input().split())
    Total_Credits = 4*X + 2*Y + 0*Z
    #Even spelling mistakes in variables matter!
    print(Total_Credits)        

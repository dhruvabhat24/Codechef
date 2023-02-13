# Solution as follows

t = int(input())           
for i in range(t):
    #Accept 4 integers as input
    X1,Y1,X2,Y2 = map(int,input().split())
    #Cost of style 1 as per the problem statement
    Cost_style1 = X1 + Y1
    #Cost of style 2 as per the problem statement
    Cost_style2 = X2 + Y2
    if Cost_style1 < Cost_style2:
        #We need to print the cheaper option
        print(Cost_style1)             
    else:
        #This condition will handle the case if Cost_style2 is cheaper
        #This condition will also handle the case if both options cost the same
        print(Cost_style2)

# Solution as follows

t = int(input())
for i in range(t):
    n = int(input())
    #list to hold all integers of the number
    final_ans = []          
    
    while n>0:
        #insert the last digit of n the start of the list
        final_ans.insert(0, (n%10))     
        #update n as n//10 - removes the last digit of n
        n = n//10           
    
    print(*final_ans)

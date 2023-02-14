# Solution as follows

X = 12
print("Mario's size after eating",X,"mushrooms is NORMAL")

X = 13
print("Mario's size after eating",X,"mushrooms is HUGE")

X = 14
print("Mario's size after eating",X,"mushrooms is SMALL")
# sub Components
# Solution as follows

X = 12
if X%3 == 0:            
    print("NORMAL")
elif (X-1)%3 == 0:
    print("HUGE")
#else condition here is sufficient.
#We do not need to write {elif (X-2)%3 == 0} since this is the only condition remaining
else:
    print("SMALL")

X = 13
if X%3 == 0:            
    print("NORMAL")
    #complete
    # Solution as follows

t = int(input())
for _ in range(t):
    X = int(input())
    
    #borrow the template from the sub-component
    if X%3 == 0:            
        print("NORMAL")
    elif (X-1)%3 == 0:
        print("HUGE")
    else:
        print("SMALL")

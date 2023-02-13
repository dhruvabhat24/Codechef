# if, else statement and indentation
a = 13
b = 15
if a >= b:
    #do not forget the indentation!!!
    print(a, 'is greater than or equal to', b)        
else:
    #do not forget the indentation!!!
    print(a, 'is lesser than', b)

# lets add the elif statement
a = 14
b = 14
if a > b:
    print(a, 'is greater than', b)
elif a == b:
    print(a, 'is equal to', b)
else:
    print(a, 'is lesser than', b)

# Solution as follows

X = 90
Y = 40
print('Given X and Y, the total watchtime of the movie is 70')

X = 80
Y = 80
print('Given X and Y, the total watchtime of the movie is 40')

X = 60
Y = 10
print('Given X and Y, the total watchtime of the movie is 55')

X = 60
Y = 50
print('Given X and Y, the total watchtime of the movie is 35')
#complete 
# Solution as follows
# Remember - there is no t in this problem

X, Y = map(int,input().split())

#declare a variable watchtime to store the solution
watchtime = (X - Y) + (Y//2)     

print(watchtime)

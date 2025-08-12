x,y = input("Enter X,Y: ").split(',')
x,y = int(x), int(y)
arr = [[i*j for j in range(y)] for i in range(x)]
print(arr)

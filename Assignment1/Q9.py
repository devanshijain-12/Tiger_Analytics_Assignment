data = []
while True:
    line = input("Enter name,age,score : ")
    if not line:
        break
    data.append(tuple(line.split(',')))
data.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))
print(data)

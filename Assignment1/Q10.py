import math
x = y = 0
while True:
    move = input("Enter move : ")
    if not move:
        break
    direction, steps = move.split()
    steps = int(steps)
    if direction == "UP": y += steps
    elif direction == "DOWN": y -= steps
    elif direction == "LEFT": x -= steps
    elif direction == "RIGHT": x += steps
dist = round(math.sqrt(x**2 + y**2))
print(dist)

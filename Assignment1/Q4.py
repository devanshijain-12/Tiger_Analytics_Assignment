result = []
for num in range(1000,3001):
    alleven = True
    strnum = str(num)
    for char in strnum:
        digit = int(char)
        if digit%2!=0:
            alleven = False
            break
    if alleven:
        result.append(num)
print(result)

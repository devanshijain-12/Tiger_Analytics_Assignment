s = input("Enter binary string: ")
ones = [i for i, ch in enumerate(s) if ch == '1']
count = 0
for i in range(len(ones)):
    for j in range(i+1, len(ones)):
        count += 1
print(count)

print("18a. Number-Star Pattern")
n = int(input("Enter rows: "))
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=' ' if j == i-1 else ' * ')
        num += 1
    print()
print()


print("18b. Diamond Star Pattern")
n = int(input("Enter rows: "))
for i in range(1, n+1):
    print(" "*(n-i) + "* " * i)
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "* " * i)
print()


print("18c. Number-Star Pyramid + Reverse")
n = int(input())
num = 1
nums = []
for i in range(1, n+1):
    row = []
    for j in range(i):
        row.append(str(num))
        num += 1
    nums.append(row)
for row in nums:
    print(' * '.join(row))
for row in reversed(nums[:-1]):
    print(' * '.join(row))
print()


print("18d. Pattern ‘G’")
rows = int(input("Enter rows: "))
for i in range(rows):
    if i == 0:
        print(" *** ")
    elif i == rows//2:
        print(" * ***")
    elif i == rows-1:
        print("  * * *")
    elif i > rows//2:
        print(" *     *")
    else:
        print(" *")
print()


print("18e. 0-1 Pattern")
n = int(input("Enter odd number: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == n//2:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
print()

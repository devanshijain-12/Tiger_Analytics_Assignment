case = int(input("1: first to last, 2: last to first: "))
s = input("Enter string: ")
times = int(input("Enter rotations: "))
for _ in range(times):
    if case == 1:
        s = s[1:] + s[0]
    else:
        s = s[-1] + s[:-1]
    print(s)

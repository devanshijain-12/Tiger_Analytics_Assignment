n = int(input("Enter number: "))
if sum(i for i in range(1, n) if n % i == 0) == n:
    print("Perfect number")
else:
    print("Not Perfect number")

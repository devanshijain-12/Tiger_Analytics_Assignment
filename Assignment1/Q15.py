from math import comb
n = int(input("Enter total stops: "))
m = int(input("Enter stops to make: "))
print(comb(n-m+1, m))

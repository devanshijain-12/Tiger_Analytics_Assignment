num = int(input("Enter number: "))
power = len(str(num))
numcopy = num
sum = 0
while (num>0):
    digit = num%10
    sum+= digit**power
    num = num//10
if (sum == numcopy):
    print("Armstrong number")
else:
    print("Not Armstrong number")

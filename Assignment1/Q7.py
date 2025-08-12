balance = 0
while True:
    entry = input("Enter transaction : ")
    if not entry:
        break
    t, amt = entry.split()
    amt = int(amt)
    if t == 'D':
        balance += amt
    elif t == 'W':
        balance -= amt
print(balance)

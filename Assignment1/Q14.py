valid_currency = list(map(int, input("Enter valid currencies: ").split(',')))
money = int(input("Enter money: "))
for c in sorted(valid_currency, reverse=True):
    if money >= c:
        count = money // c
        money %= c
        print(f"{c}-{count}")

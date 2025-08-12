text = input("Enter text: ")
letters = 0
digits = 0
for c in text:
    if (c.isalpha()):
        letters+=1
    elif (c.isdigit()):
        digits+=1
print("LETTERS", letters)
print("DIGITS", digits)

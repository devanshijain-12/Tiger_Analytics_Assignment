email = input("Enter email: ")
if email.count('@') == 1:
    name, domain = email.split('@')
    if all(c.islower() or c.isdigit() or c in '._' for c in name):
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")

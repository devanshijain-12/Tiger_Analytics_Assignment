s = input("Enter string: ")
import re
pairs = []
for m in re.finditer(r"([a-zA-Z])(\d+)([a-zA-Z])", s):
    if sum(int(d) for d in m.group(2)) == 9:
        pairs.append((m.group(1), m.group(3)))
for a, b in pairs:
    print(f"{a},{b}")

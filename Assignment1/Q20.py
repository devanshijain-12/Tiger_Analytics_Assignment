ideal = {"Sugar level":15, "Blood pressure":32, "Heartbeat rate":71, "weight":65, "fat percentage":10}
patient = {}
for key in ideal:
    val = int(input(f"{key}: "))
    patient[key] = val

for k, v in patient.items():
    print(f"{k}:{v}")

diff = {k: patient[k] - ideal[k] for k in ideal}
print(diff)

for k, v in diff.items():
    if v < 0:
        print(f"{k} {v}")
        print(f"{k} is {-v} less than the ideal value")
    elif v > 0:
        print(f"{k} {v}")
        print(f"{k} is {v} more than the ideal value")
    else:
        print(f"{k} is equal to the ideal value")

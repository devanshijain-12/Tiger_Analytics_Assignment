scoreA = scoreB = 0
while scoreA < 5 and scoreB < 5:
    a = input("Player A: ")
    b = input("Player B: ")
    if a == b:
        print("DRAW")
    elif (a == "Stone" and b == "Scissor") or \
         (a == "Paper" and b == "Stone") or \
         (a == "Scissor" and b == "Paper"):
        print("Player A wins")
        scoreA += 1
    else:
        print("Player B wins")
        scoreB += 1

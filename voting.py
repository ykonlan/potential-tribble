
candidates = {"KABAL": 0, "REIKO": 0, "NOOB": 0}
while True:
    vofor = input("Enter your preferred candidate or enter 'exit' to quit or finish voting\nCandidates are Kabal, Reiko and Noob\n").upper()
    if vofor in candidates.keys():
        candidates[vofor] += 1
        print("Your vote has been recorded successfully")
    elif vofor == "EXIT":
        for x,y in candidates.items():
            print(f"{x}:{y}")
        break
    else:
        print("Enter valid vote")


#tip calculator

bill = int(input("Total bill amount: "))
service = input("Level of service (good, bad, or fair): ")
service = service.lower()

if service == "good":
    tip = bill * .20
    total = bill + tip
    print("Tip amount: ", tip)
    print("Total amount: ", total)
elif service == "bad":
    tip = bill * .10
    total = bill + tip
    print("Tip amount: ", tip)
    print("Total amount: ", total)
elif service == "fair":
    tip = bill * .15
    total = bill + tip
    print("Tip amount: ", tip)
    print("Total amount: ", total)

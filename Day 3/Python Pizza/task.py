print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

cost = 0
if size == "S":
    cost += 15
elif size == "M":
    cost += 20
elif size == "L":
    cost += 25
else:
    IOError("Wrong Size Selected")

if pepperoni == "Y":
    if size == "S":
        cost += 2
    elif size in ["M", "L"]:
        cost += 3

if extra_cheese == "Y":
    cost += 1

print("Your final bill is: ${}.".format(cost))
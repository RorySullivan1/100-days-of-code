aged = False
age = 0
while not aged:
    user_input = input("How old are you?")
    try:
        age = int(user_input)
        aged = True
    except ValueError:
        print(f"The input is invalid! Input integer for age! Given: {user_input}")

if age > 18:
    print("You can drive! and die for your country...")
if age > 21:
    print("Now you can drink...")

user = input("Greeting: ")

if user.startswith("Hello"):
    print("$0")
elif user.startswith("H"):
    print("$20")
else:
    print("$100")
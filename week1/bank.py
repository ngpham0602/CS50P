def main():
    user = input("Greeting: ")

    greet = greeting(user)

    print(user)
    
def greeting(user):
    if user.startswith("Hello"):
        print("$0")
    elif user.startswith("H"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
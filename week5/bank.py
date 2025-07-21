def greeting(user):
    if user.startswith("Hello"):
        return "$0"
    elif user.startswith("H"):
        return "$20"
    else:
        return "$100"

def main():
    user = input("Greeting: ")

    print(greeting(user))

if __name__ == "__main__":
    main()
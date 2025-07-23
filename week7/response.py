import validators

user = input("What's your email: ")
if validators.email(user):
    print("Valid")
else:
    print("Invalid")
import inflect

p = inflect.engine()

name = []

while True:
    try:
        user: str = input("Name: ")

        name.append(user)

    except EOFError:
        sentence = p.join((name))

        print(f"\nAdieu, adieu to {sentence}")
        break



import random


while True:
    try:
        user: int = int(input("Level: "))
        if user > 0:
            break
    except ValueError:
        continue


correct = random.randint(1, user)

while True:
    try:
        guess: int = int(input("Guess: "))

        if guess > correct:
            print("Too large!")
        elif guess < correct:
            print("Too small")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
import random


def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            user = int(input("Level: "))
            if user in [1, 2, 3]:
                return user
            else:
                continue
        except Exception:
            continue




def generate_integer(level):
        number: int = 0
        correct: int = 0

        while number < 10:
            if level == 1:   
                x = random.randint(1, 10)
                y = random.randint(1, 10)
            elif level == 2:
                x = random.randint(10, 99)
                y = random.randint(10, 99)
            elif level == 3:
                x = random.randint(100, 999)
                y = random.randint(100, 999)
            try:
                for attemps in range(3):    
                    question = f"{x} + {y}"
                    calculate = int(input(f"{question} = "))
                    if calculate == (x + y):
                        correct = correct + 1
                        number = number + 1
                        break 
                    else:
                        print("EEE")
                else:
                    print(f"{x} + {y} = {x + y}")
                    number = number + 1
            except ValueError:
                continue
        print(f"Correct answer: {correct}")


if __name__ == "__main__":
    main()
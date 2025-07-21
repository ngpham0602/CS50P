def convert(user):
    vowel = ""
    for c in user:
        if c.lower() not in 'iaeou':
            vowel += c
    return vowel

def main():
    user = input("Input: ")
    print(convert(user))


if __name__ == "__main__":
    main()


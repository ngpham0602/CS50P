vowel = ""

user = input("Input: ")

for c in user:
    if c.lower() not in 'iaeou':
        vowel += c
print(vowel)

    
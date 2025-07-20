user = input()
camelCase = []

for char in user:
    if char.isupper():
        camelCase.append('_')
        camelCase.append(char.lower())
    else:
        camelCase.append(char)

print(''.join(camelCase))
user = input("Expression: ").strip()
x, y, z = user.split()
x = int(x)
z = int(z)
if y == '+':
    print(float(x + z))
elif y == '-':
    print(float(x - z))
elif y == '*':
    print(float(x * z))
elif y == '/':
    if z == 0:
        print("Error")
    else:
        print(round(float(x / z), 1))
else:
    print("Error")
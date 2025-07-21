d: dict = {
    'apple': '130',
    'avocado': '50',
    'sweet cherries': '100',
}
#Many more

while True:
    user = input("Your fruit: ").lower().strip()

    for fruit in d:
        if user in fruit:
            print(f"Calories: {d[user]}")

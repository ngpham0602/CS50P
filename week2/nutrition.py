d: dict = {
    'apple': '130',
    'avocado': '50',
    'sweet cherries': '100',
}

for fruit in d:
    user = input("Your fruit: ").lower().strip()
    if user in fruit:
        print(f"Calories: {d[user]}")

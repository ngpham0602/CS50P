if __name__ == "__main__":
    d: dict[str, str] = {  # dict[str, str] is a type hint for a dictionary with string keys and string values
        'apple': '130',
        'avocado': '50',
        'sweet cherries': '100',
    }
    #Many more

    while True:
        user = input("Your fruit: ").lower().strip()
        for fruit in d:
            print(f"Calories: {d.get(fruit, 'Unknown calories')}")  # no need to check if fruit is in d, get will return None if not found
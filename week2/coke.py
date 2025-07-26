if __name__ == "__main__":
    due: int = 50

    print(f"Amount Due: {due}")

    coin: list[int] = [25, 10, 5]

    while due > 0:
        user = int(input("Insert Coin: "))
        if user in coin:
            due = due - user
            if due >= 0:
                print(f"Amount Due: {due}".replace('-', ''))
            else:
                print(f"Change Owed: {due}".replace('-', ''))

    
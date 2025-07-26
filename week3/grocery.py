if __name__ == "__main__":
    bag: dict = {}
    while True:
        try:
            user = input().strip().upper()
            bag[user] = bag.get(user, 0) + 1

            if user not in bag:
                bag[user] = bag.get(user, 0) + 1

        except EOFError:
            for user in sorted(bag):
                print(f"{bag[user]} {user}")
            break
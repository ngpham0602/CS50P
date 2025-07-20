def main():
    user = input()
    user = convert(user)
    print(user)


def convert(emoji):
    emoji = emoji.replace(':)', '🙂').replace(':(', '🙁')
    return emoji

main()
def convert(emoji: str) -> str:
    emoji = emoji.replace(':)', '🙂').replace(':(', '🙁')
    return emoji

if __name__ == '__main__':
    user = input()
    user = convert(user)
    print(user)
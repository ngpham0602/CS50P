import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    ums = re.findall(r"\bum?\b", s, re.IGNORECASE)
    for um in ums:
        count = count + 1
    return count



if __name__ == "__main__":
    main()
import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> str | None:
    part = re.findall(r'src="(.*?)"', s)
    for url in part:
        if "youtube.com" in url:
            part2 = re.findall(r"embed/([a-zA-Z0-9_-]+)", s)
            return f"https://youtu.be/{part2[0]}"
        else:
            return None



if __name__ == "__main__":
    main()
import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    m = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if not m:
        return False
    
    parts = m.groups()

    for part in parts:
        if not 0 <= int(part) <= 255:
            return False
        if len(part) > 1 and part.startswith("0"):
            return False
    return True


if __name__ == "__main__":
    main()
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = str(s)
    for c in s:
        if c in '., ':
            return 0
        if c.isdigit():
            if c != '0':
                return 1
            else:
                return 0
    if len(s) <= 6 and len(s) >= 2 and s[:2].isalpha() and s[-1].isdigit():
        return 1
    else:
        return 0
 




main()
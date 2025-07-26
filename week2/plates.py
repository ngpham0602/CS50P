def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s: str) -> int:
    found_digit = False
    s = str(s)
    for c in s:
        if c in ",. ":
            return 0
        if c.isdigit():
            if not found_digit:
                if c == '0':
                    return 0
                found_digit = True
    if len(s) <= 6 and len(s) >= 2 and s[:2].isalpha() and s[-1].isdigit():
        return 1
    else:
        return 0
 

if __name__ == "__main__":
    main()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    found_digit = False
    s = str(s)
    for c in s:
        if c in ",. ":
            return "Invalid"
        if c.isdigit():
            if not found_digit:
                if c == '0':
                    return "Invalid"
                found_digit = True
    if len(s) <= 6 and len(s) >= 2 and s[:2].isalpha() and s[-1].isdigit():
        return "Valid"
    else:
        return "Invalid"
 



if __name__ == "__main__":
    main()
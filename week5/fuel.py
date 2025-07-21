def main():
    while True:
        try:    
            user = input()

            result = convert(user)

            print(result)

            break
        except Exception:
            print("Invalid output, try again")

        

def convert(s):
    first, second = s.split('/')
    first = int(first)
    second = int(second)
    if first < 0 or second <= 0:
        raise ZeroDivisionError("The first/second number cannot be negative or 0")
    if first > second:
        raise ValueError("The first number cannot be higher than the second number")
    if first == second:
        return "F"
    elif first == 0:
        return 'E'
    percentage = round((first / second) * 100)
    return f"{percentage}%"
exit

if __name__ == "__main__":   
    main()

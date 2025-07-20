def main():
    user = input("What time is it? (am/pm) ")
    user = convert(user)
    print(user)



def convert(time):
    try:
        time = time.strip()
        if time.endswith("am") or time.endswith("pm"):
            time = time[:-2].strip()
        else:
            raise ValueError("Invalid time format")
    except ValueError:
        return "Invalid time format"
    hours, minutes = time.split(":") 
    hours = int(hours)
    minutes = int(minutes)
    if (hours >= 7 and hours < 8) and (minutes >= 0 and minutes <= 59) or (hours == 8 and minutes == 0):
        return "breakfast time"
    elif hours >= 12 and hours < 13 and (minutes >= 0 and minutes <= 59) or (hours == 13 and minutes == 0):
        return "lunch time"
    elif hours >= 18 and hours < 19 and (minutes >= 0 and minutes <= 59) or (hours == 19 and minutes == 0):
        return "dinner time"
    else:
        return "not meal time"


if __name__ == "__main__":
    main()
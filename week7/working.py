import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    try:
        time1, time2 = s.split(" to ")
        time1 = time1.strip()
        time2 = time2.strip()
        time1is_pm = False
        time2is_pm = False
        if (time1.endswith("AM") or time1.endswith("PM")) and (time2.endswith("AM") or time2.endswith("PM")):
            if time1.endswith("PM"):
                time1is_pm = True
            if time2.endswith("PM"): 
                time2is_pm = True
            time1 = time1[:-2].strip()
            time2 = time2[:-2].strip()
        else:
            raise ValueError("Invalid time format")
    except ValueError:
        return "Invalid time format"
    if ":" not in time1:
        hours1 = int(time1)
        minutes1 = 0
    else:
        hours1, minutes1 = time1.split(":")
        hours1 = int(hours1)
        minutes1 = int(minutes1)
    if time1is_pm and hours1 != 12:
        hours1 += 12
    elif not time1is_pm and hours1 == 12:
        hours1 = 0
    if ":" not in time2:
        hours2 = int(time2)
        minutes2 = 0
    else: 
        hours2, minutes2 = time2.split(":")
        hours2 = int(hours2)
        minutes2 = int(minutes2)
    if time2is_pm and hours2 != 12:
        hours2 += 12
    elif not time2is_pm and hours2 == 12:
        hours2 = 0 
    if (hours1 >= 1 and hours1 <= 23) and (minutes1 >= 0 and minutes1 <= 59):
        pass
    elif (hours1 >= 1 and hours1 <= 23) and (minutes1 >= 0 and minutes1 <= 59):
        pass
    else:
        return "Invalid time format"
    
    return f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}"
    

if __name__ == "__main__":
    main()
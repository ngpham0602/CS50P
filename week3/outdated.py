months: list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            user = input("Date: ")

            user = convert(user)

            print(user)

            break
        except Exception:
            continue

def convert(s: str) -> str:
    if "," in s:
        month_date, year = s.split(",")
        month, date = month_date.split(" ")
        month = months.index(month) + 1
        date = int(date)
        year = int(year)
        if (month < 1 or month > 12) or (date < 1 or date > 30):
            raise ValueError("Enter a appropriate value")
        
        
        elif (month == 'February' and date > 29):
            raise ValueError("February don't have more than 29 days!")

    elif "/" in s:
        month, date, year = s.split("/")
        month = int(month)
        date = int(date)
        year = int(year)
        if (month < 1 or month > 12) or (date < 1 or date > 30):
            raise ValueError("Enter a appropriate value")
        
        elif (month == 2 and date > 29):
            raise ValueError("February don't have more than 29 days!")
        

    return f"{year:04d}-{month:02d}-{date:02d}"

main()
        
        

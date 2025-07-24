from datetime import date
import inflect

p = inflect.engine()


def main():
    print(convert(input("Date of Birth: ")))

def convert(s: str) -> str:
    try:
        if "-" in s:
            year, month, day = s.split("-")
            year = int(year)
            month = int(month)
            day = int(day)
            put = date(year, month, day)
            today = date.today()

            delta = today - put
            total = delta.days * 1440
            words = p.number_to_words(total).replace(" and", "").replace(",", "")
            return f"{words} minutes"
        else:
            return "Invalid date"
    except ValueError:
        return "The year/month/day is out of range"


        


if __name__ == "__main__":
    main()
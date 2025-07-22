import sys
import csv
from tabulate import tabulate

try:
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
    elif sys.argv[1].endswith(".csv"):
        food = []
        system, menu = sys.argv
        menu = sys.argv[1]
        with open(menu, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                food.append(row)
            print(tabulate(food, headers="keys", tablefmt="grid"))
    else:
        print("Not a CSV file")



except FileNotFoundError:
    print("File not found")
    sys.exit()
import csv, sys

try:
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]

        new_file = []


        with open(file1, "r") as before:
            reader = csv.DictReader(before)
            for row in reader:
                name = row["name"]
                house = row["house"]
                last, first = name.split(", ")
                first = first.strip()
                last = last.strip()
                new_file.append({"first": first, "last": last, "house": house})

        with open(file2, "w") as after:
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in new_file:
                writer.writerow(row)
                
except FileNotFoundError:
    print("File not found")
    sys.exit()

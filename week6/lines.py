import sys
import os

try:
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
    else:
        system, filename = sys.argv
        if filename.endswith(".py"):
            sys.argv[1] = filename
            with open(filename, "r") as file:
                lines = file.readlines()
            
            count_lines = 0
            not_count_lines = 0

            for line in lines:
                stripped_line = line.strip()
                if stripped_line.startswith("#"):
                    not_count_lines = not_count_lines + 1
                elif stripped_line == "":
                    not_count_lines = not_count_lines + 1
                else:
                    count_lines = count_lines + 1

            print(count_lines)
            file.close()
        else:
            print("Wrong file")
            sys.exit()
except FileNotFoundError:
    print("File not exist")

from pyfiglet import Figlet
from os import sys

figlet = Figlet()

figlet.getFonts()

figlet.setFont(font=sys.argv[2])

user: str = input("Input: ")

print(figlet.renderText(user))
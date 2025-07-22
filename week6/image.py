import sys 
from PIL import Image, ImageOps


try:
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
    else:
        end = (".png", ".jpg", ".jpeg")
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        if "." not in file1 or "." not in file2:
            print("Invalid input")
        elif file1.rsplit(".", 1)[-1] != file2.rsplit(".", 1)[-1]:
            print("TWo files have different extension")
        else:
            shirt = Image.open("shirt.png")
            photo = Image.open(file1)
            width, height = shirt.size
            new_height = int(height * 1.4)
            new_size = (width, new_height)
            photo = photo.resize(new_size)
            photo = ImageOps.fit(photo, shirt.size)
            photo.paste(shirt, mask=shirt)
            photo.save(file2)
            photo.show()

except FileNotFoundError:
    print("File not found")
    sys.exit()


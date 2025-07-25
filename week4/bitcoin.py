from os import sys
import requests

url = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=5b8e0b93075a7cc28d635201c2ed2e588537ea24ffd0fe75ad0b5ba210ddf891")
data = url.json()


if __name__ == "__main__":
    try:
        quantity = sys.argv[1]
        quantity = float(quantity)
        price = quantity * float(data["data"]["priceUsd"])
        print(f"${price:,.4f}")
    except IndexError:
        print("Missing command-line argument")
    except ValueError:
        print("Command-line argument is not a number")

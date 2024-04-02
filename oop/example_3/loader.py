import json
from buyers import Buyer
from sellers import Seller


def load_data(path="inputs.json"):
    with open(path, "r") as f:
        data = json.load(f)

    buyers = []
    for buyer in data["buyers"]:
        buyers.append(
            Buyer(**buyer)
        )

    sellers = []
    for seller in data["sellers"]:
        sellers.append(
            Seller(**seller)
        )
    return buyers, sellers

# online application that matches sellers with buyers based on some metric
from buyers import Buyer
from sellers import Seller
from match import Match

def find_seller(buyer: Buyer, sellers: list[Seller]):
    diffs = []
    for seller in sellers:
        for seller_product_metric in seller.get_product_metrics():
            if buyer.wish_list == seller_product_metric.product:
                diffs.append(
                    abs(
                        seller_product_metric.metric - buyer.buyer_metric)
                )
    min_diff = min(diffs)
    idx = diffs.index(min_diff)
    return idx


def match(buyers: list[Buyer], sellers: list[Seller]):
    # strategy:
    # for each buyer, find the closest seller
    # match them together, pop the seller from the list
    #
    matches = []
    for buyer in buyers:
        if sellers:
            seller_idx = find_seller(buyer, sellers)
            match = Match(buyer, sellers[seller_idx])
            matches.append(match)
            sellers.pop(seller_idx)
        else:
            break

    # display matches
    for match in matches:
        print(match)

# online application that matches sellers with buyers based on some metric

def find_seller(buyer, sellers):
    diffs = []
    for seller in sellers:
        diffs.append(
            abs(seller["seller_metric"] - buyer["buyer_metric"])
        )
    min_diff = min(diffs)
    idx = diffs.index(min_diff)
    return idx


def match(buyers: list, sellers: list):
    # strategy:
    # for each buyer, find the closest seller
    # match them together, pop the seller from the list
    #
    matches = []
    for buyer in buyers:
        if sellers:
            seller_idx = find_seller(buyer, sellers)
            match = buyer.copy()
            match.update(sellers[seller_idx])
            matches.append(match)
            sellers.pop(seller_idx)
        else:
            break

    # display matches
    for match in matches:
        print(match)

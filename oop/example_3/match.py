from buyers import Buyer
from sellers import Seller

class Match:

    def __init__(self, buyer: Buyer, seller: Seller) -> None:
        self.buyer = buyer
        self.seller = seller

    def __repr__(self):

        return (
            f"buyer: {self.buyer.get_name()}, "
            f"seller: {self.seller.company}, "
            f"product: {self.buyer.wish_list}, "
            f"buyer_score: {self.buyer.buyer_metric}, "
            f"seller_score: {self.seller.get_score(self.buyer.wish_list)}, "
        )


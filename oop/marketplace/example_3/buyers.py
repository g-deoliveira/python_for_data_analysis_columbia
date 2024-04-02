

class Buyer:

    def __init__(
        self,
        first_name: str,
        last_name: str,
        member_since: str,
        date_of_birth: str,
        city_of_birth: str,
        country_of_birth: str,
        occupation: str,
        user_name: str,
        buyer_id: int,
        buyer_metric: int,
        wish_list: str):

        self.first_name = first_name
        self.last_name = last_name
        self.member_since = member_since
        self.date_of_birth = date_of_birth
        self.city_of_birth = city_of_birth
        self.country_of_birth = country_of_birth
        self.occupation = occupation
        self.user_name = user_name
        self.buyer_id = buyer_id
        self.buyer_metric = buyer_metric
        self.wish_list = wish_list

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        text = (
            f"first_name={self.first_name}",
            f"last_name={self.last_name}",
            f"member_since={self.member_since}",
            f"date_of_birth={self.date_of_birth}",
            f"city_of_birth={self.city_of_birth}",
            f"country_of_birth={self.country_of_birth}",
            f"occupation={self.occupation}",
            f"user_name={self.user_name}",
            f"buyer_id={self.buyer_id}",
            f"buyer_metric={self.buyer_metric}",
            f"wish_list={self.wish_list}",
        )
        return ", ".join(text)

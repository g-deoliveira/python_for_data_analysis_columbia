from dataclasses import dataclass

class Seller:

    def __init__(
        self,
        company: str,
        address: str,
        city: str,
        state: str,
        zip_code: str,
        product_metrics: dict[str, int],
    ):
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.pm = self._set_product_metrics(product_metrics)

    def _set_product_metrics(self, product_metrics):
        pm = []
        for prod, score in product_metrics.items():
            pm.append(
                ProductMetrics(
                    product=prod,
                    metric=score
                )
            )
        return pm

    def get_address(self):
        return f"{self.address} {self.city} {self.state} {self.zip_code}"

    def get_product_metrics(self):
        return self.pm

    def get_score(self, product):
        for pm in self.pm:
            if pm.product == product:
                return pm.metric

    def __repr__(self):
        text = [
            f"company={self.company}",
            f"address={self.address}",
            f"city={self.city}",
            f"state={self.state}",
            f"zip_code={self.zip_code}",
            f"product_metrics={self.pm}",
        ]
        return ", ".join(text)


@dataclass
class ProductMetrics:
    product: str
    metric: int

    def __repr__(self):
        return f"({self.product}, {self.metric})"

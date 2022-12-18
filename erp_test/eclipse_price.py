import random
from utils import UtilsServerIlx as Utils


class GetPricingEclipse:
    currency = ['EUR', 'USD', 'UAH']

    def create_rep_price_eclipse(self):
        response = {
            "productId": random.randint(100, 500),
            "branch": Utils.random_str(size=3),
            "pricingPerQuantity": random.randint(100, 500),
            "pricingUOM": "c",
            "productUnitPrice": {
                "value": '{:.8f}'.format(random.randint(1000, 2000) * 0.01),
                "currency": random.choice(self.currency)
            },
            "quantityBreaks": []
        }

        return response


if __name__ == '__main__':
    g = GetPricingEclipse()

    resp = g.create_rep_price_eclipse()

    print(resp)

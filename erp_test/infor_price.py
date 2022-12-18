import random
from utils import UtilsServerIlx as Utils


class GetPricingInfor:
    letters = ["A", "B", "C"]

    def create_rep_price_infor(self, unit_price, prod_number):
        letter = random.choice(self.letters)

        response = {
            "response": {
                "cErrorMessage": "",
                "price": unit_price,
                "discountAmount": random.randint(0, 10),
                "discountType": "%",
                "netAvailable": random.randint(0, 10),
                "specialCostType": "y",
                "priceCostPer": letter,
                "unitsPerStocking": '{:.2f}'.format(random.randint(10, 20) * 0.01),
                "specialConversion": random.randint(0, 10),
                "specialCostRecordNumber": random.randint(0, 10),
                "stockingQuantityOrdered": random.randint(0, 10),
                "unitConversion": random.randint(0, 10),
                "pricingRecordNumber": prod_number,
                "promotionalFlag": random.choice([True, False]),
                "priceOriginCode": f'{random.randint(1, 10)}',
                "unitsPerStockingText": letter,
                "extendedAmount": '{:.2f}'.format(random.randint(10, 20) * 0.01),
                "extendedDiscountAmount": random.randint(0, 10)
            }
        }

        return response


if __name__ == '__main__':
    g = GetPricingInfor()

    number = 13416891
    price = '{:.2f}'.format(random.randint(1000, 2000) * 0.01)

    resp = g.create_rep_price_infor(price, number)
    print(resp)




from pydantic import BaseModel
from typing import List


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code
        self.data = self.response_json.get('response')

    def assert_response_status(self, status_code):
        assert self.response_status == status_code

    def validate_response_schema(self, schema):
        schema.parse_obj(self.response_json)

    def validate_response_data(self, order_data):
        print(self.__str__())
        print(order_data)

        assert len(self.data) == len(order_data)

        next_ordered = list()
        for number in range(len(order_data)):
            ordered = self.data[number].get('items')[0].get('quantityOrdered')
            shipped = self.data[number].get('items')[0].get('quantityShipped')
            status = self.data[number].get('transactionType')
            stock_qtn = order_data[number].get('qnt')
            stock_status = order_data[number].get('status')

            print(ordered, shipped, status, stock_status, stock_qtn)

            assert shipped == stock_qtn

            if stock_status in ['Invoice']:
                assert status == 'DELIVERED'
            else:
                assert status == 'ORDERED'

            delta = ordered - shipped

            if delta > 0:
                next_ordered.append(delta)
            else:
                next_ordered.append(0)

            if number > 0:
                assert ordered == next_ordered[number - 1]

    def __str__(self):
        return f"Status code: {self.response_status}"\
               f"\nRequested url: {self.response.url}"\
               f"\nResponse body: {self.response_json}"


class Tag_items(BaseModel):
    dsku: int
    quantityShipped: int
    quantityOrdered: int


class Tag_response(BaseModel):
    id: str
    release: str
    transactionType: str
    items: List[Tag_items]
    poNumber: str


class Validator(BaseModel):
    response: List[Tag_response]













# {'response': [{'id': 'case2', 'release': '1', 'transactionType': 'DELIVERED', 'items': [{'dsku': '5', 'quantityShipped': 10, 'quantityOrdered': 100}], 'poNumber': 'CRIB 8/25/2021'}]}
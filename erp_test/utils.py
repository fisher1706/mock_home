import string
import random


class UtilsServerIlx:

    @staticmethod
    def get_generation(gen_id, status):
        return {
            "generationId": gen_id,
            "billToId": 12625,
            "priceBranch": "12",
            "shipBranch": "10",
            "glBranch": "12",
            "salesSource": "INS",
            "orderDate": "2021-08-25T05:00:00Z",
            "shipToId": 102235,
            "status": status,
            "invoiceNumber": 1,
            "shipDate": "2021-08-26T05:00:00Z",
            "requiredDate": "2021-08-25T05:00:00Z",
            "poNumber": "CRIB 8/25/2021",
        }

    @staticmethod
    def get_line(line_id, quantities):
        generations = []
        for index, item in enumerate(quantities):
            generations.append(UtilsServerIlx.get_line_generation(line_id, index + 1, item))
        return {
            "lineId": line_id,
            "productId": 5,
            "orderQty": 100,
            "taxableCode": 1,
            "generations": generations
        }

    @staticmethod
    def get_line_generation(line_id, generation_id, stock_qty):
        return {
            "generationId": generation_id,
            "labelPerQuantity": "",
            "lineId": line_id,
            "productId": 5,
            "stockQty": stock_qty,
            "nonstockQty": stock_qty - int(stock_qty / 2)
        }

    @staticmethod
    def create_generation(name_orders):
        generations = []
        for index, item in enumerate(name_orders):
            generations.append(UtilsServerIlx.get_generation(index + 1, item))

        return generations

    @staticmethod
    def create_data_order(data_orders, number=1):
        name_orders = [line.get("status") for line in data_orders if line.get("status")]
        qnt_orders = [line.get("qnt") for line in data_orders if line.get("qnt")]

        generations = UtilsServerIlx.create_generation(name_orders)
        lines = [UtilsServerIlx.get_line(number, qnt_orders)]

        print(generations)
        print(lines)

        return generations, lines

    @staticmethod
    def create_data_order_infor(data_order, online_field, resp):
        qty = data_order.get('qty')

        fields = [{'fieldName': k, 'fieldValue': v, 'seqNo': 1} for k, v in data_order.items()
                  if k in ['orderno', 'ordersuf', 'stage', 'custpo']]
        online_field.update({'qtyOrd': qty, 'qtyShip': qty, 'stkqtyord': qty, 'stkqtyship': qty})

        resp['response']['tFieldlist']['t-fieldlist'] = fields
        resp['response']['tOelineitemV3']['t-oelineitemV3'] = [online_field]

        return resp

    @staticmethod
    def random_str(size=16, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def create_resp_error(test_data, resp_data):
        diff = dict(set(test_data.items()) - set(resp_data.items()))
        resp = 'incorrect - data - for: '

        for i in diff.keys():
            resp += '{' + str(i) + '} '

        return f"{resp}"


if __name__ == '__main__':
    utils = UtilsServerIlx()

    x = utils.random_str()
    print(x)

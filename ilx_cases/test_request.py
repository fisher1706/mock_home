import requests

# import variables
from var import *
from response import Response, Validator
import pytest


# @pytest.mark.parametrize('case, data_case, url, auth_token', [
#     ('case2', variables.data_case_2, base_url, token),
#     ('case1', variables.data_case_1, base_url, token),
#     ('case8', variables.data_case_8, base_url, token)
# ])
# def test_response_ilx(case, data_case, url, auth_token):
#     headers = {'Authorization': auth_token}
#
#     resp = requests.get(url=generate_url(url, case=case), headers=headers, )
#     response = Response(resp)
#
#     response.assert_response_status(200)
#     response.validate_response_schema(Validator)
#     response.validate_response_data(data_case)


def generate_url(uri, **kwargs):
    for arg in kwargs:
        uri += '/' + str(kwargs[arg])
    return uri


# def assert_resp(resp_data, order_data):
#     # print(resp_data)
#     # print(var)
#
#     assert len(resp_data) == len(order_data)
#
#     next_ordered = list()
#     for inbox in range(len(order_data)):
#         ordered = resp_data[inbox].get('items')[0].get('quantityOrdered')
#         shipped = resp_data[inbox].get('items')[0].get('quantityShipped')
#         status = resp_data[inbox].get('transactionType')
#
#         stock_qtn = order_data[inbox].get('qnt')
#         stock_status = order_data[inbox].get('status')
#
#         print(ordered, shipped, status, stock_status, stock_qtn)
#
#         assert shipped == stock_qtn
#
#         if stock_status in ['Invoice']:
#             assert status == 'DELIVERED'
#         else:
#             assert status == 'ORDERED'
#
#         delta = ordered - shipped
#
#         if delta > 0:
#             next_ordered.append(delta)
#         else:
#             next_ordered.append(0)
#
#         if inbox > 0:
#             assert ordered == next_ordered[inbox - 1]

# def test(request):
#     print(f"request =========================== {request.__dict__}")
#     print(f"request =========================== {(request.config.__dict__)}")

def test(zapel):
    print(f"request =========================== {zapel.__dict__}")
    print(f"request =========================== {(zapel.config.__dict__)}")



if __name__ == '__main__':
    pass

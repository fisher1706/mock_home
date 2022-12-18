from __main__ import app

from flask import request

from erp_test.d1_price import GetPricingD1
from utils import UtilsServerIlx as ServUtils
from variables import *


@app.route('/external-api/test-full2/test-full2/syndicalist', methods=['GET'])
def vmi_list_sync():
    startIndex = request.args.get('startIndex')
    customerNumber = request.args.get('customerNumber')
    shipToNumber = request.args.get('shipToNumber')
    pageSize = request.args.get('pageSize')

    if startIndex is None or customerNumber is None or shipToNumber is None or pageSize is None:
        response = {
            "error": "error"
        }
        return response, 400
    else:
        response = {
            "results": [
                {
                    "dsku": "VIRTUAL 2",
                    "locationName1": "locationName",
                    "locationValue1": "value",
                    "csku": "VIRTUAL 2 updated2",
                    "min": 1,
                    "max": 101,
                    "id": "123"
                },
                {
                    "dsku": "BANANA DSKU",
                    "locationName1": "name",
                    "locationValue1": "value",
                    "csku": "Banana 98072376",
                    "min": 1,
                    "max": 99,
                    "id": "333"
                },
                {
                    "dsku": "APPLE DSKU",
                    "locationName1": "locationName 98072376",
                    "locationValue1": "value",
                    "csku": "Appl2",
                    "min": 1,
                    "max": 23,
                    "id": "234"
                },
                {
                    "dsku": "DERP",
                    "locationName1": "derp loc name 1",
                    "locationValue1": "loc value1",
                    "csku": "updated name derp(only 98072376)",
                    "min": 1,
                    "max": 11,
                    "id": "746837"
                },
                {
                    "dsku": "test",
                    "locationName1": "",
                    "locationValue1": "",
                    "csku": "ctest 98072376",
                    "min": 1,
                    "max": 11,
                    "id": "444"
                }

            ],
            "metadata": {
                "startIndex": int(startIndex),
                "pageSize": int(pageSize),
                "totalItems": 667
            }
        }
    return response, 200


@app.route('/external-api/test-full2/test-full2', methods=['GET'])
def get_full2():
    response = {
        "inbox": [
            "getPricing",
            "quoteOrders",
            "salesOrders",
            "vmilistsync",
            "searchProduct"
        ],
        "message": None,
        "code": 200
    }
    return response


@app.route('/external-api/test-full2/test-full2/SalesOrdersV2/<order_id>', methods=['GET'])
def get_order(order_id):
    response = {
        "updateKey": "BDE70949B9362887889DD492808EA2B3",
        "id": order_id
    }

    error_response = {
        "error": "error"
    }

    # generations = None
    # lines = None

    if order_id == "case1":
        generations, lines = ServUtils.create_data_order(data_case_1)
    elif order_id == "case2":
        generations, lines = ServUtils.create_data_order(data_case_2)
    elif order_id == "case3":
        generations, lines = ServUtils.create_data_order(data_case_3)
    elif order_id == "case4":
        generations, lines = ServUtils.create_data_order(data_case_4)
    elif order_id == "case5":
        generations, lines = ServUtils.create_data_order(data_case_5)
    elif order_id == "case6":
        generations, lines = ServUtils.create_data_order(data_case_6)
    elif order_id == "case7":
        generations, lines = ServUtils.create_data_order(data_case_7)
    elif order_id == "case8":
        generations, lines = ServUtils.create_data_order(data_case_8)
    elif order_id == "case10":
        generations, lines = ServUtils.create_data_order(data_case_10)
    elif order_id == "case11":
        generations, lines = ServUtils.create_data_order(data_case_11)
    else:
        return error_response, 400

    response.update({"generations": generations, "lines": lines})
    return response


@app.route('/external-api/test-full3/test-full3/sxapiOEGetSingleOrderV3', methods=['POST'])
def get_order_infor():

    response = {
        "response": {
            "cErrorMessage": "",
            "tFieldlist": {
                "t-fieldlist": [
                    {
                        "fieldName": "orderno",
                        "fieldValue": "21982806",
                        "seqNo": 1
                    },
                    {
                        "fieldName": "ordersuf",
                        "fieldValue": "03",
                        "seqNo": 1
                    },
                    {
                        "fieldName": "stage",
                        "fieldValue": "Pd",
                        "seqNo": 1
                    },
                    {
                        "fieldName": "custpo",
                        "fieldValue": "SRX VMI",
                        "seqNo": 1
                    },
                ]
            },
            "tOelineitemV3": {
                "t-oelineitemV3": [
                    {
                        "lineNo": 1,
                        "specNsType": "",
                        "prod": "ARINNMLT10",
                        "desc1": "ARL NMLT10 1\" NMLT PUSH",
                        "desc2": "IN CONN",
                        "unit": "EA",
                        "qtyOrd": 30,
                        "qtyShip": 30,
                        "price": 312,
                        "discAmt": 0,
                        "discType": "%",
                        "netOrd": 402.48,
                        "netAmt": 0,
                        "sortFld": "2",
                        "rushfl": False,
                        "botype": "y",
                        "promisedt": "2021-12-14",
                        "reqshipdt": "2021-12-14",
                        "ordertype": "",
                        "orderaltno": 0,
                        "tiedorder": "",
                        "bono": 2,
                        "stkqtyord": 30,
                        "stkqtyship": 30
                    },
                ]
            },
            "tOetaxsa": {
                "t-oetaxsa": [
                    {
                        "seqno": 1,
                        "locallabels": "State",
                        "taxcode": "IN",
                        "localdescrip": "IN - State",
                        "taxgroupnm": "STANDARD",
                        "taxamt": "14.72",
                        "taxsaleamt": "210.23"
                    }
                ]
            },
            "tOetaxar": {
                "t-oetaxar": []
            }
        }
    }

    if request.method == 'POST':
        print('post')
        # return request.form
        return response

    if request.method == 'GET':
        print('get')
        return request.form


@app.route('/external-api/test-full2/test-full2/price/fetch/', methods=['GET', 'POST'])
def price_d1():
    customer = request.args
    print(customer)
    # item = request.args['item']
    #
    # response = {'error': f'incorrect data for price_d1 - customer: {customer}, item: {item}'}
    response = {'error': f'incorrect data for price_d1 - customer:'}

    # for data in data_price_d1:
    #     if str(data['customer']) == "user_1" and str(data['item']) == "test_1":
    #         resp = GetPricingD1().create_resp_price_d1(item)
    #         return resp

    # return response, 400
    return response


@app.route('/external-api/test-full2/test-full2/sxapioefullordermntv6', methods=['GET', 'POST'])
def get_resp_infor_billing():
    data = request.get_json()
    print(data)


@app.route('/external-api/test-full2/test-full2/sxapiwtgetsingletransferorderv2', methods=['GET', 'POST'])
def get_infor_consignment_transfer():
    data = request.args
    print(data)

    response = {
            "cErrorMessage": "zapel",

            "tFieldlist": {
                "t-fieldlist": [
                    {
                        "wtno": 1,
                        "stage": "Ord",
                        "wtsuf": 2,
                        "transtype": "test",
                        "shipfmwhse": "",
                        "shiptowhse": ""
                    }
                ]
            },
            "tWtlineitemv2": {
                "t-wtlineitemv2": [
                    {
                        "bono": 1,
                        "unit": "test",
                        "duedt": "test",
                        "lineno": 2,
                        "netamt": 3,
                        "netord": 4,
                        "netrcv": 5,
                        "qtyord": 6,
                        "qtyrcv": 7,
                        "qtyship": 8,
                        "sortFld": "test",
                        "prodcost": 9,
                        "shipprod": "test",
                        "unitconv": 10,
                        "approvety": "test",
                        "ordertype": "test",
                        "proddesc": "test",
                        "proddesc2": "test",
                        "stkqtyord": 11,
                        "stkqtyrcv": 12,
                        "tiedorder": "test",
                        "nonstockty": "test",
                        "orderaltno": 13,
                        "stkqtyship": 14,
                        "prodinrcvfl": True,
                        "rcvunavailfl": True
                    }
                ]
            }
        }

    return response

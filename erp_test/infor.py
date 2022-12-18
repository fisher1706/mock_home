# response = {
#         "response": {
#             "cErrorMessage": "",
#             "tFieldlist": {
#                 "t-fieldlist": [
#                     {
#                         "fieldName": "orderno",
#                         "fieldValue": "21982806",
#                         "seqNo": 1
#                     },
#                     {
#                         "fieldName": "ordersuf",
#                         "fieldValue": "03",
#                         "seqNo": 1
#                     },
#                     {
#                         "fieldName": "stage",
#                         "fieldValue": "Pd",
#                         "seqNo": 1
#                     },
#                     {
#                         "fieldName": "custpo",
#                         "fieldValue": "SRX VMI",
#                         "seqNo": 1
#                     },
#                 ]
#             },
#             "tOelineitemV3": {
#                 "t-oelineitemV3": [
#                     {
#                         "lineNo": 1,
#                         "specNsType": "",
#                         "prod": "ARINNMLT10",
#                         "desc1": "ARL NMLT10 1\" NMLT PUSH",
#                         "desc2": "IN CONN",
#                         "unit": "EA",
#                         "qtyOrd": 30,
#                         "qtyShip": 30,
#                         "price": 312,
#                         "discAmt": 0,
#                         "discType": "%",
#                         "netOrd": 402.48,
#                         "netAmt": 0,
#                         "sortFld": "2",
#                         "rushfl": False,
#                         "botype": "y",
#                         "promisedt": "2021-12-14",
#                         "reqshipdt": "2021-12-14",
#                         "ordertype": "",
#                         "orderaltno": 0,
#                         "tiedorder": "",
#                         "bono": 2,
#                         "stkqtyord": 30,
#                         "stkqtyship": 30
#                     },
#                 ]
#             },
#             "tOetaxsa": {
#                 "t-oetaxsa": [
#                     {
#                         "seqno": 1,
#                         "locallabels": "State",
#                         "taxcode": "IN",
#                         "localdescrip": "IN - State",
#                         "taxgroupnm": "STANDARD",
#                         "taxamt": "14.72",
#                         "taxsaleamt": "210.23"
#                     }
#                 ]
#             },
#             "tOetaxar": {
#                 "t-oetaxar": []
#             }
#         }
#     }

class GenerateInforOrderStatusV2:
    resp = {
        "response": {
            "cErrorMessage": "",
            "tFieldlist": {
                "t-fieldlist": None
            },
            "tOelineitemV3": {
                "t-oelineitemV3": None
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

    online_field = {
        "lineNo": 1,
        "specNsType": "",
        "prod": "ARINNMLT10",
        "desc1": "ARL NMLT10 1\" NMLT PUSH",
        "desc2": "IN CONN",
        "unit": "EA",
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
    }

    data_infor = [
        {'orderno': 21982806, 'ordersuf': '03', 'stage': 'Pg', 'custpo': 'SRX VMI', 'num': 50},
        # {'orderno': 21982806, 'ordersuf': '03', 'stage': 'Pg', 'custpo': 'SRX VMI', 'num': 50},
        # {'orderno': 21982806, 'ordersuf': '03', 'stage': 'Pg', 'custpo': 'SRX VMI', 'num': 50},
        # {'orderno': 21982806, 'ordersuf': '03', 'stage': 'Pg', 'custpo': 'SRX VMI', 'num': 50},
        # {'orderno': 21982806, 'ordersuf': '03', 'stage': 'Pg', 'custpo': 'SRX VMI', 'num': 50},
        # {'orderno': 21982806, 'ordersuf': '03', 'stage': 'Pg', 'custpo': 'SRX VMI', 'num': 50},
        # {'orderno': 21982806, 'ordersuf': '03', 'stage': 'Pg', 'custpo': 'SRX VMI', 'num': 50},
        # {'orderno': 21982806, 'ordersuf': '03', 'stage': 'Pg', 'custpo': 'SRX VMI', 'num': 50},
    ]


def generate_fields(data, online_field, resp):
    qty = data.get('qty')

    fields = [{'fieldName': k, 'fieldValue': v, 'seqNo': 1} for k, v in data.items()
              if k in ['orderno', 'ordersuf', 'stage', 'custpo']]
    online_field.update({'qtyOrd': qty, 'qtyShip': qty, 'stkqtyord': qty, 'stkqtyship': qty})

    resp['response']['tFieldlist']['t-fieldlist'] = fields
    resp['response']['tOelineitemV3']['t-oelineitemV3'] = [online_field]

    return resp


if __name__ == '__main__':
    x = {'orderno': 21982806, 'ordersuf': '03', 'stage': 'Pg', 'custpo': 'SRX VMI', 'qty': 50}

data_case_1 = [
    {"trans": "XX-1", "qnt": 10, "status": "PickUpNow"},
]

data_case_2 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
]

data_case_3 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 20, "status": "PickUpNow"}
]

data_case_4 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 30, "status": "PickUpNow"},
    {"trans": "XX-3", "qnt": 50, "status": "PickUpNow"}
]

data_case_5 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 20, "status": "Invoice"},
    {"trans": "XX-3", "qnt": 50, "status": "Invoice"}
]

data_case_6 = [
    {"trans": "XX-1", "qnt": 110, "status": "Invoice"}
]

data_case_7 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 20, "status": "Invoice"},
    {"trans": "XX-3", "qnt": 50, "status": "Invoice"},
    {"trans": "XX-4", "qnt": 20, "status": "PickUpNow"}
]

data_case_8 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 20, "status": "Invoice"},
    {"trans": "XX-3", "qnt": 50, "status": "Invoice"},
    {"trans": "XX-4", "qnt": 20, "status": "Invoice"},
    {"trans": "XX-5", "qnt": 30, "status": "PickUpNow"}
]

data_case_10 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 20, "status": "Invoice"},
    {"trans": "XX-3", "qnt": 50, "status": "Invoice"},
    {"trans": "XX-4", "qnt": 60, "status": "Invoice"},
    {"trans": "XX-5", "qnt": 30, "status": "PickUpNow"}
]

data_case_11 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 20, "status": "Invoice"},
    {"trans": "XX-3", "qnt": 50, "status": "PickUpNow"},
    {"trans": "XX-4", "qnt": 60, "status": "PickUpNow"},
    {"trans": "XX-5", "qnt": 30, "status": "PickUpNow"}
]

data_case_12 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 20, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 50, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 60, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 30, "status": "PickUpNow"}
]

data_price_infor = [
    {"customerNumber": 100, "dsku": 200},
    {"customerNumber": 200, "dsku": 100}
]

data_orders_quote_infor = [
    {"orderId": "123", "transactionType": "QUOTED", "invNr": "11596160", "transType": "QU"},
    {"orderId": "456", "transactionType": "ORDERED", "invNr": "11596163", "transType": "SO"},
    {"orderId": "123", "transactionType": "QUOTED", "invNr": "11596160", "transType": "SO"},
]

data_quote_eclipse = [
    {"productId": "S011980089", "status": "QUOTED", "orderStatus": "Bid", "customer": "1234"},
    {"productId": "S011980089", "status": "ORDERED", "orderStatus": "Bid", "customer": "1238"},
    {"productId": "S011980089", "status": "QUOTED", "orderStatus": "Bid", "customer": "1234"},
]

data_price_d1 = [
    {"customer": "user_1", "item": "test_1"},
    {"customer": "user_2", "item": "test_2"},
    {"customer": "user_3", "item": "test_3"}
]


data_ifor_transfers = {'companyNumber': 1,
                       'singleLineNumber': 0,
                       'includeLineData': True,
                       'includeTotalData': False,
                       'includeHeaderData': True,
                       'lineSort': 'a',
                       'operatorPassword': 'logix2020',
                       'operatorInit': '2srx',
                       'cErrorMessage': '170678'
                       }

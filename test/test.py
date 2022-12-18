def create_resp_error(test_data, resp_data):
    diff = dict(set(test_data.items()) - set(resp_data.items()))
    resp = 'incorrect - data - for: '

    for i in diff.keys():
        resp += '{' + str(i) + '} '

    return f"{resp}"


if __name__ == '__main__':
    test_data = {'companyNumber': 1,
                 'singleLineNumber': 0,
                 'includeLineData': True,
                 'includeTotalData': False,
                 'includeHeaderData': True,
                 'lineSort': 'a',
                 'operatorPassword': 'logix2020',
                 'operatorInit': '2srx',
                 'cErrorMessage': '170678'
                 }

    resp_data = {'companyNumber': 1,
                 'singleLineNumber': 0,
                 'includeLineData': True,
                 'includeTotalData': False,
                 'includeHeaderData': True,
                 'lineSort': 'a',
                 'operatorPassword': 'logix2020',
                 'operatorInit': '2sr',
                 # 'cErrorMessage': '170678'
                 }

    x = dict(set(test_data.items()) - set(resp_data.items()))
    print(str(x.keys()))
    # assert str(x) == "['cErrorMessage']"



    # print(type(x))
    # print(x.keys())


import logging
from flask import Flask

app = Flask(__name__)

from erp import *

# logging.basicConfig(filename='flask.log', level=logging.DEBUG)
# logger = logging.getLogger('flask_server')
#
#
# @app.before_request
# def log_request_info():
#     logger.info(request.get_data())


@app.route('/<user>')
def home(user):
    order = user.split('&')[0].split('=')[1]
    quote = user.split('&')[1].split('=')[1]

    if order != '0' or quote != '0':
        return f"It works: {user}"
    else:
        return 'error', 400


@app.route('/external-api/test-full2/test-full2/', methods=['GET', 'POST'])
def get_fiix_new():
    print(f'request: {request}')
    print(f'json: {request.json}')
    print(f'data: {request.data}')
    print(f'environ: {request.environ}')
    print(f'headers: {request.headers}')
    print(f'path: {request.path}')
    print(f'args: {request.args}')
    print(f'authorization: {request.authorization}')

    response = {'message': 'it works'}

    return response


if __name__ == '__main__':
    app.run(debug=True)

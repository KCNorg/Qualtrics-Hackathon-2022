from flask import Flask, jsonify, request
from constans import reviews, info

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/types', methods=['GET', 'POST'])
def get_types():
    if request.method == 'POST':
        jdata = request.get_json()
        # result = get_result_from_kuba(jdata)
        # return result
    elif request.method == 'GET':
        jdata = dict()
        jdata['review'] = list(reviews.values())
        jdata['info'] = [dict(name=col_info['name'], values=col_info['values']) for col_info in info.values()]
        return jsonify(jdata)


if __name__ == '__main__':
    app.run()

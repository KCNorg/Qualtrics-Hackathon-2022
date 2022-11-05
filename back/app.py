from flask import Flask, jsonify
from constans import reviews, info

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/types', methods=['GET'])
def get_types():
    jdata = dict()
    jdata['review'] = list(reviews.values())
    jdata['info'] = [dict(name=col_info['name'], values=col_info['values']) for col_info in info.values()]
    return jsonify(jdata)


if __name__ == '__main__':
    app.run()

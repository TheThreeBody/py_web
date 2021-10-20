from flask import Flask, jsonify
from flask import request
from real_url.douyu import DouYu

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def root():
    return 'Hello Gunicorn'

@app.route('/douyu', methods=['get'])
def response_douyu():

    args = request.args.get("roomNo")
    form = request.form.get('data')
    roomNo = args
    douyu = DouYu(roomNo)
    data = {
        "stream" : douyu.get_real_url()
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()

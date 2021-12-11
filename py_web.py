# pip install flask flask-cors
from flask import Flask, jsonify
from flask import request
# 全局应用
from flask_cors import CORS
from flask_cors import cross_origin

from real_url.douyu import DouYu
from real_url.bilibili import BiliBili
from real_url.douyin import DouYin
from real_url.danmu import danmaku
import asyncio

from sukiya.sukiya import sukiya_coupon

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def root():
    return 'Hello Gunicorn'

@app.route('/douyu', methods=['get'])
@cross_origin()
def response_douyu():

    args = request.args.get("roomNo")
    form = request.form.get('data')


    roomNo = args
    douyu = DouYu(roomNo)
    data = {
        "stream" : douyu.get_real_url()
    }
    print("=========成功 生成 douyu房间号================")
    return jsonify(data)
#   return jsonify(args=args, form=form)

@app.route('/bilibili', methods=['get'])
@cross_origin()
def response_bilibili():

    args = request.args.get("roomNo")
    form = request.form.get('data')


    roomNo = args
    bilibili = BiliBili(roomNo)
    data = {
        "stream" : bilibili.get_real_url()
    }
    print("=========成功 生成 bilibili房间号================")
    return jsonify(data)

@app.route('/douyin', methods=['get'])
@cross_origin()
def response_douyin():
    roomNo = request.args.get("roomNo")
    douyin = DouYin(roomNo)
    data = {
        "stream" : douyin.get_real_url()
    }
    print("=========成功 生成 douyin直播流================")
    return jsonify(data)

@app.route('/danmu', methods=['get'])
@cross_origin()
def danmuQueue():
    q = asyncio.Queue()
    url = request.args.get("link")
    damuQ = danmaku.DanmakuClient(url, q)

@app.route('/sukiya', methods=['post'])
@cross_origin()
def sukiya():
    # print('values', request.args.lists())
    # link = request.args.get('link')
    form = request.form.get('data')
    discountNo = sukiya_coupon(form)
    data = {
        "discountNo":discountNo
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
    # 全局使用CORS跨域
    # CORS(app)
#     app.run(host="0.0.0.0", port=5800, debug=True)

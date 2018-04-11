# -*- coding: UTF-8 -*-
# auth: caowencheng<845982120@qq.com>
# date: 2018/4/6

from flask import Flask
import logging
app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return "index"


@app.route('/hello', methods=["POST"])
def hello():
    return "Hello"


if __name__ == '__main__':
    handler = logging.FileHandler('flask.log', encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    loggingFormat = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
    )
    handler.setFormatter(loggingFormat)
    app.logger.addHandler(handler)
    app.run("127.0.0.1", debug=False, port=3333, use_reloader=False)

import sys

from flask import Flask, request
from threading import Thread

from constants import *
from interface import main, get_serialized, set_movement2

app = Flask(__name__)

t = Thread(target=lambda: main(True))
t.start()


@app.route("/move")
def move():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    set_movement2(x, y)
    return get_serialized()


if __name__ == "__main__":
    app.run(HOST, PORT)

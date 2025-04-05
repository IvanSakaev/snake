import sys

from flask import Flask, request
from threading import Thread

from constants import *
from interface import main, set_movement

app = Flask(__name__)

t = Thread(target=main)
t.start()


@app.route("/move")
def move():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    print("got params:", x, y, file=sys.stderr)
    set_movement(x, y)
    return "Привет, мир! Flask работает!"


if __name__ == "__main__":
    app.run(HOST, PORT)

from flask import Flask, request
from threading import Thread

from interface import main, set_movement

app = Flask(__name__)

t = Thread(target=main)
t.start()


@app.route("/move")
def home():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    print(x, y)
    set_movement(x, y)
    return "Привет, мир! Flask работает!"


if __name__ == "__main__":
    app.run()

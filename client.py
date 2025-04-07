import requests
import time
from threading import Thread

from constants import *
from interface import main, get_movement1

time.sleep(1)
print("starting client...")

t = Thread(target=lambda: main(False))
t.start()

while True:
    player1_mouse_x, player1_mouse_y = get_movement1()
    requests.get("http://" + HOST + ":" + str(PORT) + "/move",
                 params={"x": player1_mouse_x, "y": player1_mouse_y})
    time.sleep(0.05)

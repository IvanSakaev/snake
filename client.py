import requests
import time
from threading import Thread

from constants import *
from interface import main, get_movement1, set_serialized

time.sleep(1)
print("starting client...")

t = Thread(target=lambda: main(False))
t.start()

while True:
    player1_mouse_x, player1_mouse_y = get_movement1()
    out = requests.get("http://" + HOST + ":" + str(PORT) + "/move",
                       params={"x": player1_mouse_x, "y": player1_mouse_y}).text
    set_serialized(out)
    # time.sleep(0.001)

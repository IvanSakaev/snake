import requests
import time
from math import sin, cos

from constants import *

time.sleep(1)
print("starting client...")

while True:
    for a in range(0, 3600):
        requests.get("http://" + HOST + ":" + str(PORT) + "/move", params={"x": int(sin(a/10) * 1000), "y": int(cos(a/10) * 1000)})
        time.sleep(0.05)

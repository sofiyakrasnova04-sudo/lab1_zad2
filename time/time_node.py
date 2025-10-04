#!/usr/bin/env python3
import time
from datetime import datetime

while True:
    now = datetime.now()
    print("Текущее время:", now.strftime("%H:%M:%S"))
    time.sleep(5)
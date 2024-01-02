from waiter import Wait
from datetime import datetime

START=datetime.strptime("2024-1-1 00:00", "%Y-%m-%d %H:%M")
END=datetime.strptime("2025-01-01 00:00", "%Y-%m-%d %H:%M")
newyear=Wait(START, END, "new year", "counting to next year")

newyear.play()
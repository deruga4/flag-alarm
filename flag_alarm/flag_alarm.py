from pydub import AudioSegment
from datetime import datetime, timedelta
import os
import time
import psutil

def get_next_xx30():
    current = datetime.now()
    if current.minute > 30:
        return datetime.strptime(f'{current.year}-{current.month}-{current.day} {current.hour + 1}:30', '%Y-%m-%d %H:%M')
    elif current.minute <= 30:
        return datetime.strptime(f'{current.year}-{current.month}-{current.day} {current.hour}:30', '%Y-%m-%d %H:%M')

now = datetime.now()

# Choose 6PM today as the time the alarm fires.
# This won't work well if it's after 6PM, though.
while True:
    alarm_time = datetime.combine(now.date(), get_next_xx30().time())

    print(f'Next alarm at {alarm_time}')

    time.sleep((alarm_time - now).total_seconds())
    # # Think of time.sleep() as having the operating system set an alarm for you,
    # # and waking you up when the alarm fires.
    if "Maplestory.exe" in (i.name() for i in psutil.process_iter()):
        playsound('../assets/Airporn.mp3')

    alarm_time += timedelta(hours=1)
import threading
import time
from repos import get_reps

def refresh():
    while True:
        get_reps()
        print("refresh repos")
        time.sleep(3600)

thread = threading.Thread(target=refresh, name='refresh')

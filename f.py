import time
import keyboard
import threading
import sys

def run():
    while True:
        keyboard.press_and_release('enter')
        time.sleep(0.1)
        keyboard.press_and_release('f')
        time.sleep(0.1)

# wait for f to start
print("Press F to start paying respects")
keyboard.wait('f')
print("Paying respects")
print("Press Esc to stop paying respects")

# start run thread
t = threading.Thread(target=run)
t.daemon = True
t.start()

# kill on esc
keyboard.wait('esc')
print("Done paying repsects")
sys.exit()

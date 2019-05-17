import time
from pynput.keyboard import Key, Listener

def on_press(key):
    print('KEY PRESSED: 	key code = {0}\t '.format(
        key), time.time())
#with controller.modifiers as modifiers:
 #   with_block()
def on_release(key):
    print('KEY RELEASED: 	key code = {0}'.format(
        key), time.time())
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
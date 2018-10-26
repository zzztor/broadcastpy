from pynput.mouse import Listener
from pynput.keyboard import Key, Listener as KeyboardListener

listening = True
events = []
mouseDown = False

def get_events():
    global events
    currentEvents = events
    events = []
    return currentEvents

def on_press(key):
    global listening
    global events
    if listening:
        events.append('keyboard {0} pressed'.format(key))

def on_release(key):
    global listening
    global events
    if listening:
        events.append('keyboard {0} release'.format(key))
    if key == Key.esc:
        listening = not listening

def on_move(x, y):
    global listening
    global events
    if listening:
        events.append('MouseMove {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    global listening
    global events
    if listening:
        events.append('{2} {0} {1} '.format( 'pressed' if pressed else 'released', (x, y),button))

# Collect events until released
def init_hook():
    with KeyboardListener(on_press=on_press, on_release=on_release) as keyboardListener, Listener(on_move=on_move,on_click=on_click) as listener:
        keyboardListener.join()
        listener.join()
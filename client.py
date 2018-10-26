import socket
import pyautogui
import time
import struct
import sys
import ctypes
import keyEvents

def string_to_array(str):
    return str.split('xxx')

test = 0

def emitMouseEvent(event):
    MOUSE_LEFTDOWN = 0x0002     # left button down 
    MOUSE_LEFTUP = 0x0004       # left button up 
    MOUSE_RIGHTDOWN = 0x0008    # right button down 
    MOUSE_RIGHTUP = 0x0010      # right button up 
    MOUSE_MIDDLEDOWN = 0x0020   # middle button down 
    MOUSE_MIDDLEUP = 0x0040     # middle button up 
    if (event[0] == 'MouseMove'):
        x = int(event[1].replace('(','').replace(',','').replace(')',''))
        y = int(event[2].replace('(','').replace(',','').replace(')',''))
        ctypes.windll.user32.SetCursorPos(x, y)
    else:
        button = event[0].replace('Button.','')
        if (event[1] == "pressed"):
            if (button == 'left'):
                ctypes.windll.user32.mouse_event(MOUSE_LEFTDOWN, 0, 0, 0,0)
            else:
                ctypes.windll.user32.mouse_event(MOUSE_RIGHTDOWN, 0, 0, 0,0)
        else:
            if (button == 'left'):
                ctypes.windll.user32.mouse_event(MOUSE_LEFTUP, 0, 0, 0,0)
            else:
                ctypes.windll.user32.mouse_event(MOUSE_RIGHTUP, 0, 0, 0,0)
                
def emitKeyboardEvent(event):

    VK_LSHIFT = 0xA0
    Q_Key  = 0x51
    Key_1 = 0x31
    Key_2 = 0x32
    Key_3 = 0x33
    Key_4 = 0x34
    
    key = event[0].split("'")
    if (len(key)>1):
        key = key[1]
    else:
        key = key[0].split(".")[1]
    if (event[1] == 'pressed'):
        if (key == 'q'):
            keyEvents.PressKey(Q_Key)
        elif (key == '1'):
            keyEvents.PressKey(Key_1)
        elif (key == '2'):
            keyEvents.PressKey(Key_2)
        elif (key == '3'):
            keyEvents.PressKey(Key_3)
        elif (key == '4'):
            keyEvents.PressKey(Key_4)
        elif (key == 'shift'):
            keyEvents.PressKey(VK_LSHIFT)
    elif (event[1] == 'release'):
        if (key == 'q'):
            keyEvents.ReleaseKey(Q_Key)
        elif (key == '1'):
            keyEvents.ReleaseKey(Key_1)
        elif (key == '2'):
            keyEvents.ReleaseKey(Key_2)
        elif (key == '3'):
            keyEvents.ReleaseKey(Key_3)
        elif (key == '4'):
            keyEvents.ReleaseKey(Key_4)
        elif (key == 'shift'):
            keyEvents.ReleaseKey(VK_LSHIFT)


def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)
    
def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = ''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

TCP_IP = '192.168.1.33'
TCP_PORT = 5005
BUFFER_SIZE = 5120
MESSAGE = "Hello World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
time.sleep( 2 )
##start = time.time()
while 1:
##    done = time.time()
##    elapsed = done - start
##    print(elapsed)
##    start = time.time()
    data = recv_msg(s)
    if data:
        events = string_to_array(data)
        for event in events:
            eventSplitted = event.split(' ')
            if (eventSplitted[0] == 'keyboard'):
                eventSplitted.pop(0)
                emitKeyboardEvent(eventSplitted)
            else:
                emitMouseEvent(eventSplitted)
s.close()

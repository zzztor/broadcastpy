import pyautogui
import socket
import struct
import sys
global conn
#192.168.235.1
TCP_IP = ''
TCP_PORT = 5005
BUFFER_SIZE = 10240  # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print('Esperando conexion del cliente')
conn, addr = s.accept()
print 'Connection address:', addr
    
def send_events(events):
    global conn
    str = array_to_string(events)
    send_msg(conn, str)

def array_to_string(arr):
    return 'xxx'.join(arr)

def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    conn.send(msg)  # echo
import socket
import time
SERVER_IP = '192.168.1.127'
SERVER_PORT = 3333

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP,SERVER_PORT))
    print("server is listenning...")
    s.listen(1)
    conn, addr = s.accept()
    print(f"Connection established from : {addr}")
    with conn:
        while True:
            cmd = str(input('cmd>'))
            if (cmd == 'exit'):
                break
            #print(cmd)
            conn.send(cmd.encode('utf-8'))
            start_time = time.time()
            data = conn.recv(1024)
            print(data.decode('utf-8'))


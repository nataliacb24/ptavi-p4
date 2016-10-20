#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import sys
import socket


IP = sys.argv[1]
PORT = int(sys.argv[2])
METODO = sys.argv[3]
DIRCC = sys.argv[4]


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((IP, PORT))
    if METODO == "register":
        PETICION_REG = "REGISTER sip:" + DIRCC + " SIP/2.0 \r\n\r\n"
    print("Enviando:", PETICION_REG)
    my_socket.send(bytes(PETICION_REG, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))
    
print("Socket terminado")

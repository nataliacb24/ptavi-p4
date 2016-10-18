#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import sys
import socket


IP = sys.argv[1]
PORT = int(sys.argv[2])
METODO = "REGISTER"
DIRCC = sys.argv[4]
PETICION_REG = METODO + " sip:" + DIRCC + " SIP/2.0 \r\n\r\n"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((IP, PORT))
    print("Enviando:", PETICION_REG)
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))
    
print("Socket terminado")

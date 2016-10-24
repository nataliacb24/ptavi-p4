#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Programa cliente UDP que abre un socket a un servidor
"""

import sys
import socket


IP = sys.argv[1]
PORT = sys.argv[2]
METODO = sys.argv[3]
ADD = sys.argv[4]
EXPIRES = sys.argv[5] #tiempo de expiracion segundos
TERMINAL = sys.argv[0] + IP + PORT + METODO + ADD + EXPIRES

try:
    sys.argv[0:] = TERMINAL 
except:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((IP, PORT))
    if METODO == "register":
        PETICION_REG = "REGISTER sip:" + ADD + " SIP/2.0 \r\n" + " Expires: " + EXPIRES
    print("Enviando:", '\n', PETICION_REG)
    my_socket.send(bytes(PETICION_REG, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado")

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Programa cliente UDP que abre un socket a un servidor
"""

import sys
import socket


if len(sys.argv) != 6:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")

try:
    PORT = int(sys.argv[2])
except:
    sys.exit()

IP = sys.argv[1]
METODO = sys.argv[3]
ADD = sys.argv[4]
EXPIRES = sys.argv[5]

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((IP, int(PORT)))
    if METODO == "register":
        PET = "REGISTER sip:" + ADD + " SIP/2.0 \r\n" + " Expires: " + EXPIRES
    print("Enviando:", '\n', PET)
    my_socket.send(bytes(PET, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado")

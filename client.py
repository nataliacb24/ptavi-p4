#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import sys
import socket

# Constantes. Dirección IP del servidor y contenido a enviar
#server = sys.argv[1]
#port = sys.argv[2]
SERVER = sys.argv[1]
port = int(sys.argv[2])
line = ' '.join(sys.argv[3:])

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, port))
    print("Enviando:", line)
    my_socket.send(bytes(line, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")

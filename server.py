#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import sys
import socketserver


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        IP_client = self.client_address[0]
        Port_client = self.client_address[1]
        self.wfile.write(b"Hemos recibido tu peticion")
        for line in self.rfile:
            print("IP cliente:", IP_client, "Puerto del cliente:", Port_client )
            print("El cliente nos manda ", line.decode('utf-8'))

if __name__ == "__main__":

    Port_serv = int(sys.argv[1])
    serv = socketserver.UDPServer(('', Port_serv), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")

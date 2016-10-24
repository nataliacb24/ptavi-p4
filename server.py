#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import sys
import socketserver


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    SIP Register Handler
    """

    Dicc = {}

    def handle(self):
        IP_client = self.client_address[0]
        Port_client = str(self.client_address[1])
        print('IP cliente:' + IP_client)
        print('Puerto del cliente:' + Port_client + '\n')
        peticion_SIP = self.rfile.read().decode('utf-8').split()
        print(peticion_SIP)
        if peticion_SIP[0] == 'REGISTER':
            address = peticion_SIP[1]
            self.Dicc[address] = self.client_address[0]
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            if peticion_SIP[-1] == '0':
                del self.Dicc[address]
        print(self.Dicc)

if __name__ == "__main__":

    Port_serv = int(sys.argv[1])
    serv = socketserver.UDPServer(('', Port_serv), SIPRegisterHandler)
    print('Lanzando servidor UDP de eco...' + '\n')
    serv.serve_forever()

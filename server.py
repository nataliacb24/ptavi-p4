#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import sys
import json
import time
import socketserver


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    SIP Register Handler class
    """

    Dicc = {}

    def handle(self):
        """
        Registro
        """
        IP_client = self.client_address[0]
        Port_client = str(self.client_address[1])
        print('IP cliente:' + IP_client)
        print('Puerto del cliente:' + Port_client + '\n')
        peticion_SIP = self.rfile.read().decode('utf-8').split()
        if peticion_SIP[0] == 'REGISTER':
            address = peticion_SIP[1]
            self.Dicc[address] = self.client_address[0]
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            if peticion_SIP[-1] == '0':
                self.Dicc.clear()
            else:
                expire = peticion_SIP[-1]
                self.Dicc['Expire'] = expire
        print(self.Dicc)
        fichjson = self.register2json()

    def register2json(self):
        """
        Creacion fichero json
        """
        json.dump(self.Dicc, open('registered.json', 'w'))


if __name__ == "__main__":

    Port_serv = int(sys.argv[1])
    serv = socketserver.UDPServer(('', Port_serv), SIPRegisterHandler)
    print('Lanzando servidor UDP de eco...' + '\n')
    serv.serve_forever()

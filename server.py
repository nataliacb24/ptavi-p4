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
    def register2json(self):
        """
        Creacion fichero json con los datos de un diccionario
        """
        json.dump(self.Dicc, open('registered.json', 'w'))

    def json2register(self):
        """
        Comprobacion del fichero json
        """
        try:
            with open("register.json", 'r') as fichjson:
                self.Dicc = json.load(fichjson)
        except:
            pass

    def delete(self):
        lista = []
        for clave in self.Dicc:
            time_now = self.Dicc[clave][1]
            print(time_now)
            time_strp = time.strptime(time_now, '%Y-%m-%d %H:%M:%S')
            if time_strp <= time.gmtime(time.time()):
                lista.append(clave)
        for cliente in lista:
            del self.Dicc[cliente]

    def handle(self):
        """
        Registro
        """
        IP_client = self.client_address[0]
        Port_client = str(self.client_address[1])
        print('IP cliente:' + IP_client)
        print('Puerto del cliente:' + Port_client + '\n')
        if len(self.Dicc) == 0:
            self.json2register()
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        while 1:

            peticion_SIP = self.rfile.read().decode('utf-8')
            print(peticion_SIP)
            if not peticion_SIP:
                break
            (metodo, address, sip, space, expire) = peticion_SIP.split()
            if metodo != 'REGISTER' and not "@" in address:
                break
            time_now = int(time.time()) + int(expire)
            time_exp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time_now))
            if expire == '0':
                del self.Dicc[address]
            else:
                self.Dicc[address] = [str(IP_client), str(time_exp)]
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            self.delete()
            self.register2json()


if __name__ == "__main__":
    Port_serv = int(sys.argv[1])
    serv = socketserver.UDPServer(('', Port_serv), SIPRegisterHandler)
    print('Lanzando servidor UDP de eco...' + '\n')
    serv.allow_reuse_address = True
    serv.serve_forever()
    serv.close()

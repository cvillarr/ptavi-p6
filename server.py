#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion\r\n")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read().decode('utf-8')
            line_conten = line.split()
            print("El cliente nos manda " + line)
            if line_conten[0] == "INVITE":
                self.wfile.write(b"SIP/2.0 100 Trying\r\nSIP/2.0 180 Ringing\r\n"
                                 + b"SIP/2.0 200 OK\r\n")
            if line_conten[0] != "INVITE":
                self.wfile.write(b"SIP/2.0 405 Method Not Allowed")
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', 5555), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()

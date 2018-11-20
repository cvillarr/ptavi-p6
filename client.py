#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
try:
    USUARIO = sys.argv[2].split(':')[0]
    SERVER = USUARIO.split('@')[1]
    PORT = int(sys.argv[2].split(':')[1])
    METODO = sys.argv[1]

    # Contenido que vamos a enviar
    LINE = (METODO + ' sip:' + USUARIO + ' SIP/2.0')

except IndexError:
    sys.exit('Usage: python3 client.oy method receiver@IP:SIPport')


print (LINE)
# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER, PORT))

    print("Enviando: " + LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)

    print('Recibido -- ', data.decode('utf-8'))
    my_socket.send(bytes("ACK sip:" + USUARIO + " SIP/2.0","Utf-8") + b"\r\n")
    print("Terminando socket...")

print("Fin.")

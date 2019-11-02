import sys
import socket

# HOST = '10.0.0.1' # Dirección en la que va a escuchar nuestro servidor ECHO
HOST = ''           # Lo dejo en blanco para que escuche por cualquier adaptador

PORT = 7            # Puerto en el que escucha por defecto un servidor ECHO

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen()
#       conn, addr = s.accept()
	while True:
		conn, addr = s.accept()
		print('Connected by', addr)
		data = conn.recv(1024)
		if data:
			print(data)
			conn.sendall(data)
#               else:
#                       break
		conn.close()

if __name__ == '__main__':
        sys.exit(main())


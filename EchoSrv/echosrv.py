import sys
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 7			# Port to listen on (non-privileged ports are > 1023)

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

def main():
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.bind((HOST, PORT))
	socket.listen()
	conn, addr = socket.accept()
	with conn:
		print('Connected by', addr)
		while True:
			data = conn.recv(1024)
			if data:
				print(data)
				conn.sendall(data)
#			else:
#				break 


if __name__ == '__main__':
	sys.exit(main())

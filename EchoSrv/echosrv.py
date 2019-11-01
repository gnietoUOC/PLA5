import sys
import socket

HOST = '10.0.0.1'  # Standard loopback interface address (localhost)
PORT = 7			# Port to listen on (non-privileged ports are > 1023)

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connected by', addr)
		while True:
			data = conn.recv(1024)
			if data:
				print(data)
				conn.sendall(data)
#			else:
#				break 
			conn.close()

if __name__ == '__main__':
	sys.exit(main())

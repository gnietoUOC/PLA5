import sys
import socket

# HOST = '10.0.0.1' # Dirección en la que va a escuchar nuestro servidor ECHO
HOST = ''           # Lo dejo en blanco para que escuche por cualquier adaptador 
					# (Wifi o Ethernet)
PORT = 7            # Puerto en el que escucha por defecto un servidor ECHO

def main():
	''' Aplicación que recibe conexiones por el puerto 7 y responde con
		el mismo contenido.
		TODO: Añadir una gestión más elegante de las excepciones que se 
		puedan producir durante el flujo de la aplicación.
	'''

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
		# Abrimos el puerto 7 y nos ponemos a esperar
		sck.bind((HOST, PORT))
		sck.listen()

		while True:
			# Recibimos una conexión e imprimos la dirección del cliente
			conn, addr = sck.accept()
			print('Connected by', addr)

			# Leemos el mensaje de entrada
			data = conn.recv(1024)

			# Si hay datos, respondemos con el mismo contenido y lo mostramos
			# por pantalla
			if data:
				print(data)
				conn.sendall(data)

			# Cerramos la conexión
			conn.close()

if __name__ == '__main__':
        sys.exit(main())


import socket
import time
from datetime import datetime

def start_server():
	try:
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind(('127.0.0.1',2000))
		server.listen(100)
		while True:
			print('Сервер запущен.')
			client_socket, address = server.accept()
			data = client_socket.recv(1024).decode('utf-8')
			print(data)
			content = load_page_from_get_request(data)
			client_socket.send(content)
			client_socket.shutdown(socket.SHUT_WR)
	except KeyboardInterrupt:
		server.close()
		print('Сервер остановленн в ручную.')
		
def load_page_from_get_requests(request_data):
	HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
	HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
	path = requests_data.split(' ')[1]
	response = ''
	try:
		with open('views'+path, 'rb') as file:
			response = file.read()
		return HDRS.encode('utf-8') + response
	except FileNotFoundError:
		return (HDRS_404 + 'Данной странницы не существует.').encode('utf-8')
		
if __name__ == '__main__':
	start_server()

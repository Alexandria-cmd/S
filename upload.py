import socket
import time
from datetime import datetime

def main():
  print('Сервер получил файл()')
  print('Сервер получил файл()')
  print('Сервер получил файл()')
  print('Сервер получил файл()')
  print('Сервер получил файл()')
  print('Сервер получил файл()')
		
def load_page_from_get_request(request_data):
	HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
	HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
	path = request_data.split(' ')[1]
	response = ''
	try:
		with open('views'+path, 'rb') as file:
			response = file.read()
		return HDRS.encode('utf-8') + response
	except FileNotFoundError:
		return (HDRS_404 + 'Данной странницы не существует.').encode('utf-8')
		
if __name__ == '__main__':
	main()

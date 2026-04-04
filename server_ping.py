import requests
import threading
import time
from datetime import datetime
import os
import subprocess

# пишем основной адрес, куда будем слать запросы
BASE_URL = "https://johnathan-fattier-amos.ngrok-free.dev"

# пишем функцию GET-запроса
def fetch_get():
   now = datetime.now()
   time_now = ("[{}.{}.{}  {}:{}:{}]".format(now.day, now.month, now.year, now.hour, now.minute, now.second))
   print(f'{time_now} Отправка GET запроса')
   # объявляем переменную, в которой отправляем GET-запрос на нужный адрес
   response_get = requests.get(f"{BASE_URL}/get")
   # возвращаем статус-код от сервера и ответ в формате JSON
   now = datetime.now()
   time_now = ("[{}.{}.{}  {}:{}:{}]".format(now.day, now.month, now.year, now.hour, now.minute, now.second))
   print(f'{time_now} Отправка GET запроса закончена ({response_get.status_code})')
   if response_get.status_code != 502:
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      try:
         res_os = os.system ('ngrok http --url=johnathan-fattier-amos.ngrok-free.dev 80')
         subprocess.run(['python', 'server_SMTP_err.py'])
      except:
         print('Запустить ngrok заново не получилось.')
         subprocess.run(['python', 'server_SMTP_err.py'])
   else:
      pass

# пишем функцию POST-запроса
def fetch_post():
   now = datetime.now()
   time_now = ("[{}.{}.{}  {}:{}:{}]".format(now.day, now.month, now.year, now.hour, now.minute, now.second))
   print(f'{time_now} Отправка POST запроса')
   # объявляем переменную и указываем, что нужно добавить
   data_to_post = {"key": "value"}
   # объявляем переменную, в которой отправляем POST-запрос на нужный адрес
   response_post = requests.post(f"{BASE_URL}/post", json=data_to_post)
   # возвращаем статус-код от сервера и ответ в формате JSON
   now = datetime.now()
   time_now = ("[{}.{}.{}  {}:{}:{}]".format(now.day, now.month, now.year, now.hour, now.minute, now.second))
   print(f'{time_now} Отправка POST запроса закончена ({response_post.status_code})')
   if response_post.status_code != 502:
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      try:
         res_os = os.system ('ngrok http --url=johnathan-fattier-amos.ngrok-free.dev 80')
         subprocess.run(['python', 'server_SMTP_err.py'])
      except:
         print('Запустить ngrok заново не получилось.')
         subprocess.run(['python', 'server_SMTP_err.py'])
   else:
      pass

# пишем функцию PUT-запроса
def fetch_put():
   now = datetime.now()
   time_now = ("[{}.{}.{}  {}:{}:{}]".format(now.day, now.month, now.year, now.hour, now.minute, now.second))
   print(f'{time_now} Отправка PUT запроса')
   # объявляем переменную и указываем, что нужно обновить
   data_to_put = {"key": "updated_value"}
   # объявляем переменную, в которой отправляем PUT-запрос на нужный адрес
   response_put = requests.put(f"{BASE_URL}/put", json=data_to_put)
   # возвращаем статус-код от сервера и ответ в формате JSON
   now = datetime.now()
   time_now = ("[{}.{}.{}  {}:{}:{}]".format(now.day, now.month, now.year, now.hour, now.minute, now.second))
   print(f'{time_now} Отправка PUT запроса закончена ({response_put.status_code})')
   if response_put.status_code != 502:
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      try:
         res_os = os.system ('ngrok http --url=johnathan-fattier-amos.ngrok-free.dev 80')
         subprocess.run(['python', 'server_SMTP_err.py'])
      except:
         print('Запустить ngrok заново не получилось.')
         subprocess.run(['python', 'server_SMTP_err.py'])
   else:
      pass

# пишем функцию DELETE-запроса
def fetch_delete():
   now = datetime.now()
   time_now = ("[{}.{}.{}  {}:{}:{}]".format(now.day, now.month, now.year, now.hour, now.minute, now.second))
   print(f'{time_now} Отправка DELET запроса')
   # объявляем переменную, в которой отправляем DELETE-запрос на нужный адрес
   response_delete = requests.delete(f"{BASE_URL}/delete")
   # возвращаем статус-код от сервера и ответ в формате JSON
   now = datetime.now()
   time_now = ("[{}.{}.{}  {}:{}:{}]".format(now.day, now.month, now.year, now.hour, now.minute, now.second))
   print(f'{time_now} Отправка DELETE запроса закончена ({response_delete.status_code})')
   if response_delete.status_code != 502:
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      try:
         subprocess.run(['python', 'server_start.py'])
         subprocess.run(['python', 'server_SMTP_err.py'])
      except:
         print('Запустить ngrok заново не получилось.')
         subprocess.run(['python', 'server_SMTP_err.py'])
   else:
      pass
   

while True:
    th1 = threading.Thread(target=fetch_get)
    th2 = threading.Thread(target=fetch_post)
    th3 = threading.Thread(target=fetch_put)
    th4 = threading.Thread(target=fetch_delete)

    th1.start()
    th2.start()
    th3.start()
    th4.start()
    
    th1.join()
    th2.join()
    th3.join()
    th4.join()

    
    print('Сон 1 час')
    time.sleep(600)
    print('Сон 50 минут')
    time.sleep(600)
    print('Сон 40 минут')
    time.sleep(600)
    print('Сон 30 минут')
    time.sleep(600)
    print('Сон 20 минут')
    time.sleep(600)
    print('Сон 10 минут')
    print('=======================================')
    print('=======================================')
    print('=======================================')

import logging
import threading
import time
import requests
import json

url = 'https://host/init_auth'


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def send_req_to_server():
    logging.debug('Starting sending post req')
    time.sleep(3)
    logging.debug('<<<write status>>>')


def get_int_auth():

    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

    if response.status_code == 200:
        print(response.content)
        return json.loads(response.content)
    else:
        return None


#t = threading.Thread(name='send post to server', target=send_req_to_server)

def startTread_init_auth():
   r=t.start()


t = threading.Thread(name='thread init auth', target=get_int_auth)

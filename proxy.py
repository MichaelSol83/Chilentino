import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def send_req_to_server():
    logging.debug('Starting sending post req')
    time.sleep(3)
    logging.debug('<<<write status>>>')



#t = threading.Thread(name='send post to server', target=send_req_to_server)

def startTread():
    t.start()

t = threading.Thread(name='send post to server', target=send_req_to_server)

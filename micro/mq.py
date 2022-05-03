# -*- coding: utf-8 -*

from multiprocessing import Process
from . import config

import logging
import time
import zmq

##
# Workers

class Worker(Process):

    def __init__(self, index, port, handle):
        super().__init__(target=self.target)

        self.index = index
        self.handle = handle
        self.port = port

    def target(self):

        context = zmq.Context()
        socket = context.socket(zmq.PULL)
        socket.connect(f"tcp://127.0.0.1:{self.port}")

        logging.info("worker [%d] connected in %s", self.index, self.port)

        while True:
            try:

                request = socket.recv_json()
                logging.debug("[%s] received %s", self.index, request)

                self.handle( request )
            
            except Exception as ex:
                logging.error(ex) 

##
# Decorador

def worker(port, process=1):

    def decorator(handle):
        try:

            workers = []

            for index in range(0, process):
                w = Worker(index, port, handle)
                w.start()

                workers.append(w)

        except Exception as ex:
            logging.error(ex)

    return decorator

##
# Submit a worker

sockets = {}

context = zmq.Context()

def submit(data, port):

    if port not in sockets:
        socket = context.socket(zmq.PUSH)
        socket.bind(f"tcp://127.0.0.1:{port}")
        sockets[port] = socket
    
    logging.debug("sending to '%d' request %s", port, data)

    sockets[port].send_json(data)

import os
import threading

from flask import Flask,request, send_from_directory


class Server(threading.Thread):

    def __init__(self, workdir, port):
        super(Server, self).__init__()
        self.daemon = True
        self.workdir = workdir
        self.port = port

    def run(self):
        app = Flask('billboard')

        @app.route('/')
        def root():
            return 'OK'

        @app.route('/current')
        def current():
            response = send_from_directory(self.workdir, 'current.jpg')
            response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response.headers['Pragma'] = 'no-cache'
            return  response

        app.run(host='0.0.0.0', port=self.port)





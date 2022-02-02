"""
This script runs the learningFlask application using a development server.
"""

from os import environ
from small_group_app import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    #HOST = '192.168.200.50'
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
        #PORT = 5005
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

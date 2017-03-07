import os

MONGO_PORT = 27017


# try:
MONGO_HOST = os.environ['MONGO_PORT_27017_TCP_ADDR']
# except KeyError:
#     MONGO_HOST = "localhost"

DOMAIN = {
    'lists': {}
    }

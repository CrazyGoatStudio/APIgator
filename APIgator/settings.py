import os, requests

MONGO_PORT = 27017

if requests.get("http://localhost:"+str(MONGO_PORT)).status_code==200:
    MONGO_HOST = "localhost"
else:
    MONGO_HOST = os.environ['MONGO_PORT_27017_TCP_ADDR']


DOMAIN = {
    'lists': {}
    }

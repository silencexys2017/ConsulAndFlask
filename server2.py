from server import HttpServer
from httpapp import AppServer

server=HttpServer('0.0.0.0',8002,'172.17.0.5',8500,AppServer)
server.startServer()

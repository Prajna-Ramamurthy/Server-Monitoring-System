import pickle
from servers import Server

servers = pickle.load(open("servers.pic"))

print("Example to add server ")

servername = input("Enter server name")
port = int(input("Enter a port number as integer"))
connection = input("Enter a type plain/ping/ssl")
priority = input("Enter prioroty high/low ")

new_server = Server(servername, port, connection, priority)
servers.append(new_server)

pickle.dump(servers, open("servers.pickle", "wb"))

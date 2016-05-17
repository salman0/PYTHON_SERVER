
import socket               # Import socket module
 
s = socket.socket()         
host = socket.gethostname()
port = 10099               # Reserve a port for your service.
 
s.connect((host, port))
reply = s.recv(1024)

print(reply)
s.close()

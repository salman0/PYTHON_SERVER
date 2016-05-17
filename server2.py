'''
    Simple socket server using threads
'''
 
import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 10099 # Arbitrary non-privileged port

i=0
conn3 = 0
conn4 = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ') + str(msg[0]) + (' Message ') + msg[1]
    sys.exit()
     
print ('Socket bind complete')
 
#Start listening on socket
s.listen(2)
print ('Socket now listening')
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send(str.encode('Welcome to the server. Type something and hit enter\n')) #send only takes string
   
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn3.recv(1024)
        reply = (str.encode('OK...')) + data
        if not data: 
            break
        conn4.sendall(reply)
 
    conn3.close()
def clientthread1(conn):
    #Sending message to connected client
    conn.send(str.encode('Welcome to the server. Type something and hit enter\n')) #send only takes string
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn4.recv(1024)
        reply = (str.encode('OK...')) + data
        if not data: 
            break
        conn3.sendall(reply)
   
    conn4.close()
    #now keep talking with the client

while 1:
   
    if(i == 0):	
            conn3, addr = s.accept()
         
	    start_new_thread(clientthread ,(conn3,))	
            i=i+1
            print(i)
    elif(i == 1):
            conn4,addr = s.accept()
           
            start_new_thread(clientthread1 ,(conn4,))

    print ('Connected with ' + addr[0] + ':' + str(addr[1]))        	
    
s.close()

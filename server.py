import socket
from threading import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_adress = '127.0.0.1'
port = 800


server.bind((ip_adress, port))
server.listen()

list_of_clients=[]

print("SERVER HAS STARTED...")

//conn means connection here do not get confused-

def clientthread(conn,addr):
    conn.send("WELCOME TO THIS CHARTROOM!".encode('utf-8'))
    while Tue:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                print ("<" + addr[0] + ">" + message)

                message_to_send = "<" + addr[0] + ">" + message
                broadcast(messge_to_send,conn)
                
           else:
               remove(conn)
       except:
           continue

           def broadcast(message, connection):
               for clients in list_of_clients:
                   if clients! = connection:
                       try:
                           clients.sent(message.encode('utf-8'))
                           except:
                               remove(clients)

def remove(connection):
    if connection in list-of_clients:
        list_of_clients.remove(connection)

        while True:
            conn, addr = server.accept()
            list_of_clients.append(conn)
            print(addr[0] + "CONNECTED") 
            new_thread = Thread(target= clientthread,args=(conn,addr))
            
         //arg is used to Pass variable number of arguments to a function

            new_thread.start()                                      


            



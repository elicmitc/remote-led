import socket
def tcp_server(Host,Port):
    # Host Not Needed (I think)
    # so far Host is unused
    #host = socket.gethostname()
    port = int(Port)  # initiate port no above 1024
    listening = 1 # server starts with ability to listen
    client_n = 0
    server_socket = socket.socket()  # get instance
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((Host, port))  # bind host address and port together
    print("Hello, I am a server");
    while True:
        if(listening == 1):
            server_socket.listen(2) # 2 possible clients
            conn, address = server_socket.accept()# accept new connection
            listening = 0 # stops listening
            print("connection "+ str(client_n) +" from (\'" \
			       + str(address[0]) +"\', " \
			       + str(port)+")")
            client_n = client_n + 1 # increase for next client
        data = conn.recv(256).decode() #get message from client
        print("got message from (\'" + str(address[0])+"\', "+str(port)+")")
        #print(f'raw data: {data}')
        if(data == "What Color?"): # hello instance
            print(f'\'{data}\' received')
            #data = "75 100 95"
            data = "250 0 224"
        elif(data == "goodbye"): # goodbye instance
            data = "farewell"
            conn.send(data.encode())
            conn.close() #close client connection
            listening = 1 #start listening
            continue
        elif(data == "exit"): # exit instance
            print('exit received')
            data = "ok"
            conn.send(data.encode()) #send message "ok"
            break       # exit While loop and close connection
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection
    return
tcp_server('10.0.0.194',8080)

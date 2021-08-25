import socket
def tcp_client(Host, Port):
    # Host not used but should be used
    host = socket.gethostname()  # only on same system
                                 # needs replaced
    port = int(Port)  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((Host, port))  # connect to the server
    print("Hello, I am a client");

    while True:
        message = str(input())  # take input
        message = message[0:256] # restrict input to 256 
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(256).decode()  # receive response

        print(data)  # show in terminal
        if(data == "ok"):
            client_socket.close()
            return -1
        elif(data == "farewell"):
            client_socket.close()
            return -1

    client_socket.close()  # close the connection
tcp_client('127.0.0.1',8080)

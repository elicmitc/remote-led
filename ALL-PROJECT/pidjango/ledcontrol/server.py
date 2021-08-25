import socket
import sys

def tcp_color_server(Host,Port, Color):
    # Host Not Needed (I think)
    # so far Host is unused
    #host = socket.gethostname()
    port = int(Port)  # initiate port no above 1024
    listening = 1 # server starts with ability to listen
    client_n = 0
    server_socket = socket.socket()  # get instance
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((Host, port))  # bind host address and port together
    #print("Hello, I am a color server!");
    
    while True:
        if(listening == 1):
            server_socket.listen(2) # 2 possible clients
            conn, address = server_socket.accept()# accept new connection
            listening = 0 # stops listening
            print("---------------------- Server Information --------------------");
            print("color server: connection "+ str(client_n) +" from (\'" \
			       + str(address[0]) +"\', " \
			       + str(port)+")")
            client_n = client_n + 1 # increase for next client
            #receive = conn.recv(256).decode()
            #print(f'received: {receive}')
        conn.send(Color.encode())
        data = conn.recv(256).decode() #get message from client
        print("color server: got message from (\'" + str(address[0])+"\', "+str(port)+f"): \"{data}\"")
        #print(f'raw data: {data}')
        if(data == "What Color?"): # hello instance
            #data = "75 100 95"
            data = Color
        elif(data == "goodbye"): # goodbye instance
            data = "farewell"
            conn.send(data.encode())
            conn.close() #close client connection
            listening = 1 #start listening
            continue
        elif(data == "exit"): # exit instance
            #data = "ok"
            #conn.send(data.encode()) #send message "ok"
            break       # exit While loop and close connection
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection
    return
#def color_to_rgb(color_name):

if __name__ == "__main__":
    tcp_color_server('10.0.0.194',12345, sys.argv[1])

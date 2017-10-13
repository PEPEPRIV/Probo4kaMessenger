import socket

ip = socket.gethostbyname(socket.getfqdn())
port = 9090

input_command = input()
if input_command == "connect":
    print("ID = ")
    searching_id = input()
    message_to_Sserver = ip, ",", port, ",", searching_id

    sock = socket.socket()
    sock.connect(('198.2255.5225.548', 9090))
    print("connected to server")
    sock.send(message_to_Sserver.encode("utf-8"))
    print("request send")
    data = sock.recv()
    sock.close()

    udata = data.decode("utf-8")
    udata = udata.split(",")
    ip_Client2 = udata[i][0]
    port_Client2 = udata[i][1]
    print("conneting to client2")
    socket.connect((ip_Client2, port_Client2))
    print("connection done")
else:
    socket.bind('',9090)
    socket.listen()

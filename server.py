import socket

print(socket.gethostbyname(socket.getfqdn()))
socket = socket.socket()
ALL_ID = [["192.32.32.32", 9090, 1111], ["192.32.32.89", 9030, 2222]]

socket.bind(('', 9090))
print("listening to client")
socket.listen(1)
conn, addr = socket.accept()
print("connected")

while True:
    data = conn.recv(1024)
    if not data:
        break
print("request received")

udata = data.decode("utf-8")
message_from_Client = udata.split(",")
ip_Client_wchS1 = message_from_Client[0]
port_Client_wchS1 = message_from_Client[1]
searching_id_Client = message_from_Client[2]
i = 0
while True:
    i += 1
    if searching_id_Client == ALL_ID[i][2]:
        ip_Client_w0hS2 = ALL_ID[i][0]
        port_Client_w0hS2 = ALL_ID[i][1]
        searched_id_Client = ALL_ID[i][2]
        message_to_Client_wchS1 = ip_Client_w0hS2, ",", port_Client_w0hS2
        message_to_Client_whoS2 = ip_Client, ",", port_Client_wchS1
        break
conn.close()
print("connection closed")

socket.sendto(message_to_Client_wchS1.encode("utf-8"), ip_Client_wchS1)
print("reply to C1")
socket.sendto(message_to_Client_whoS2.encode("utf-8"), ip_Client_w0hS2)
print("reply to C2")

socket.bind(('', 9090))
socket.listen(1)

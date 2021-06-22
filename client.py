import socket
s=socket.socket()
h="localhost"
p=54322
ad=(h,p)
s.connect(ad)

# print(s.recv(128).decode())
# print(s.recv(128).decode())
# print(s.recv(128).decode())
# print(s.recv(128).decode())
# print(s.recv(128).decode())
# print(s.recv(128).decode())
#
# s.send(op.encode())
# n=input("enter number:")
# s.send(n.encode())
# print(s.recv(128).decode())
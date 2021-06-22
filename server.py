import socket
s=socket.socket()
h="localhost"
p=54321
ad=(h,p)
s.bind(ad)
s.listen(2)

# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return "not prime number"
#             break
#     else:
#         return "prime number"
#
# def fact(n):
#     f=1
#     for i in range(1,n):
#         f+=f*i
#     return f
#
# def fib(n):
#     if n==0 or n==1:
#         return n
#     else:
#         a = fib(n-1)+fib(n-2)
#     return a

while True:
    conn, address=s.accept()
    print("connected successfully")
    # conn.send("\nsuccessfully connected, now enjoy ur connection".encode())
    # conn.send("\n1.Prime Number 2.Fibonacci(using recursion) 3.Factorial".encode())
    # conn.send("\n\nEnter operation(1|2|3):".encode())
    # op=input()
    # conn.send(op.encode())
    # conn.recv(128).decode()
    # conn.send("\nEnter a number:".encode())
    # n=input("")
    # conn.send(n.encode())
    # conn.recv(128).decode()
    # n=int(n)

    # if op=="1"or op=="Prime" or op=="prime":
    #     r=prime(n)
    #     conn.send(r.encode())
    # if op=="2" or op=="Fibonacci" or op=="fibonacci":
    #     r=str(fib(n))
    #     conn.send(r.encode())
    # if op=="3" or op=="Factorial" or op=="factorial":
    #     r=str(fact(n))
    #     conn.send(r.encode())
    conn.close()
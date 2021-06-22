import threading
import time
from tabulate import tabulate

def a():
    a=[]
    for i in range(5):
        a.append(i)
        print(a)



def b():
    b=[]
    for i in range(5):
        b.append(i)
        print(b)


def c():
    c=[]
    for i in range(5):
        c.append(i)
        print(c)


# def d():
#     print(tabulate((a,b,c)))



t1=threading.Thread(target=a)
t2=threading.Thread(target=b)
t3=threading.Thread(target=c)
# t4=threading.Thread(target=d)

print(t1,t2,t3)

t1.start()
t2.start()
t3.start()
# t4.start()
t1.join()
t2.join()
t3.join()
# t4.join()
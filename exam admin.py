from tkinter import *
from tkinter import messagebox
import mysql.connector as m
conn=m.connect(username="root",password="root",host="localhost",database="exam")
cur=conn.cursor()
def admin():
    wd1 = Tk()
    wd1.title("Admin Login")
    wd1.geometry("350x170")
    wd1.resizable(0, 0)

    l1=Label(wd1,text="User name",font="calibri",width=10)
    l1.place(x=10,y=20)

    e1=Entry(wd1,width=20,relief="solid",border=1,font="calibri")
    e1.place(x=120,y=20)

    l2=Label(wd1,text="Password",font="calibri",width=10)
    l2.place(x=10,y=60)

    e2=Entry(wd1,show="*",width=20,relief="solid",border=1,font="calibri")
    e2.place(x=120,y=60)

    def login():

        data=[]
        username=e1.get()
        data.append(username)
        password=e2.get()
        data.append(password)
        data=tuple(data)
        cur.execute("select username,password from admin")
        dbdata=cur.fetchall()
        if data in dbdata:
            wd1.destroy()
            wd2 = Tk()
            wd2.geometry("550x130")
            wd2.title("Add Questions")
            l1=Label(wd2,text="Enter how many questions you want to enter :",font="calibri").place(x=20,y=20)
            e=Entry(wd2,width=10,border=1,relief="solid")
            e.place(x=430,y=25)



            def addquestions():
                try:
                    a=int(e.get())
                    for i in range(a):
                        for j in range(b):
                            pass
                except ValueError:
                    messagebox.showerror("error", "invalid input")



            b4 = Button(wd2, text="Add Questions",font="calibri",command=addquestions)
            b4.place(x=200, y=70)

            wd2.mainloop()

        else:
            messagebox.showerror("error","Invalid credentials")

    b1 = Button(wd1, text="Login",font="calibri", command=login)
    b1.place(x=150, y=110)


    wd1.mainloop()

admin()
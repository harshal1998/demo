import questions as q
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as m

conn = m.connect(username="root", password="root", host="localhost", database="exam")
cur = conn.cursor()


def home():
    wd1 = Tk()
    wd1.title("Login")
    wd1.geometry("350x170")
    wd1.resizable(0, 0)

    l1 = Label(wd1, text="User name", font="calibri", width=10)
    l1.place(x=10, y=20)

    e1 = Entry(wd1, width=20, relief="solid", border=1, font="calibri")
    e1.place(x=120, y=20)

    l2 = Label(wd1, text="Password", font="calibri", width=10)
    l2.place(x=10, y=60)

    e2 = Entry(wd1, show="*", width=20, relief="solid", border=1, font="calibri")
    e2.place(x=120, y=60)

    def login():
        data = []
        username = e1.get()
        data.append(username)
        password = e2.get()
        data.append(password)
        data = tuple(data)
        cur.execute("select username,password from registration")
        dbdata = cur.fetchall()
        if data in dbdata:
            wd1.destroy()
            wd3 = Tk()
            wd3.title("Choose Subject")
            wd3.geometry("350x180")
            wd3.resizable(0, 0)

            l9 = Label(wd3, text="Select Subject:", font="calibri")
            l9.place(x=10, y=20)

            rv1 = IntVar()
            r1 = Radiobutton(wd3, text="Python", font="calibri", variable=rv1, value=1)
            r1.place(x=140, y=20)

            r2 = Radiobutton(wd3, text="Java", font="calibri", variable=rv1, value=2)
            r2.place(x=140, y=50)

            r3 = Radiobutton(wd3, text="C++", font="calibri", variable=rv1, value=3)
            r3.place(x=140, y=80)

            def start():

                if rv1.get() == 1:
                    q.python()
                    wd1.destroy()

                elif rv1.get() == 2:
                    q.java()
                    wd1.destroy()

                elif rv1.get() == 3:
                    q.C()
                    wd1.destroy()

            b4 = Button(wd3, text="Start Exam", font="calibri", command=start)
            b4.place(x=120, y=130)

            wd3.mainloop()


        else:
            messagebox.showerror("error", "Invalid credentials")

    b1 = Button(wd1, text="Login", font="calibri", command=login)
    b1.place(x=70, y=110)

    def register():
        wd1.destroy()
        wd2 = Tk()
        wd2.title("Register")
        wd2.geometry("350x250")
        wd2.resizable(0, 0)

        l5 = Label(wd2, text="Name", font="calibri")
        l5.place(x=10, y=20)

        e5 = Entry(wd2, width=20, relief="solid", border=1, font="calibri")
        e5.place(x=120, y=20)

        l6 = Label(wd2, text="Roll no", font="calibri")
        l6.place(x=10, y=60)

        e6 = Entry(wd2, width=20, relief="solid", border=1, font="calibri")
        e6.place(x=120, y=60)

        l7 = Label(wd2, text="Class", font="calibri")
        l7.place(x=10, y=100)

        Class = ['FY', 'SY', 'TY']
        Class.insert(0, "select your class")
        cb = ttk.Combobox(wd2, width=18, font="calibri", state="readonly")
        cb['value'] = Class
        cb.place(x=119, y=100)
        cb.current(0)

        l8 = Label(wd2, text="Password", font="calibri")
        l8.place(x=10, y=140)

        e8 = Entry(wd2, show="*", width=20, relief="solid", border=1, font="calibri")
        e8.place(x=120, y=140)

        def submit():

            if e5.get() == "":
                messagebox.showerror("error", "Enter your name")
            else:
                nm = e5.get()

            if e6.get() == "":
                messagebox.showerror("error", "Enter your roll no")
            else:
                rn = int(e6.get())

            if cb.get() == "select your class":
                messagebox.showerror("error", "select your class")
            else:
                cl = cb.get()

            if e8.get() == "":
                messagebox.showerror("error", "Password cannot be blank")
            else:
                ps = e8.get()

            ra = random.randrange(10000, 99999)
            un = nm + str(ra)

            v = (rn, nm, cl, un, ps)
            q = "insert into registration(rollno,name,class,username,password) values(%s,%s,%s,%s,%s)"
            cur.execute(q, v)
            conn.commit()
            messagebox.showinfo("NOTE DOWN", "Username: " + str(un) + "\nPassword: " + str(ps))
            wd2.destroy()
            home()

        b3 = Button(wd2, text="Submit", command=submit, font="calibri")
        b3.place(x=135, y=190)

        wd2.mainloop()

    b2 = Button(wd1, text="Register", font="calibri", command=register)
    b2.place(x=160, y=110)

    wd1.mainloop()


home()

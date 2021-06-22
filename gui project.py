from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as m

conn=m.connect(user="root",password="root",host="localhost",database="formdb")
cur=conn.cursor()

def register():
    wd2 = Tk()
    wd2.geometry("400x400")
    wd2.title("Registration")
    wd2.resizable(0,0)
    l3 = Label(wd2, text="Username",font="calibri")
    l3.place(x=20, y=20)
    l4 = Label(wd2, text="Password",font="calibri")
    l4.place(x=20, y=80)
    l5 = Label(wd2, text="Contact No",font="calibri")
    l5.place(x=20, y=140)
    l6 = Label(wd2, text="Mail-ID",font="calibri")
    l6.place(x=20, y=200)

    e3=Entry(wd2,width=20,font="calibri")
    e3.place(x=150,y=20)
    e4=Entry(wd2,show="*",width=20,font="calibri")
    e4.place(x=150, y=80)
    e5=Entry(wd2,width=20,font="calibri")
    e5.place(x=150, y=140)
    e6=Entry(wd2,width=20,font="calibri")
    e6.place(x=150, y=200)

    def regdb():
        data = []
        q3="select * from registration"
        cur.execute(q3)
        a=cur.fetchall()
        registration=list(x[1] for x in a)
        usernm = e3.get()
        if usernm in registration:
            messagebox.showwarning("message","username is already taken")
        else:
            username=e3.get()
            data.append(username)
        password = e4.get()
        data.append(password)
        try:
            contact = int(e5.get())
            data.append(contact)
        except ValueError:
            messagebox.showerror("message", "contact no must be integers")

        mail = e6.get()
        data.append(mail)
        data=tuple(data)
        q2="select username,password,contact,mail from registration"
        cur.execute(q2)
        dbdata=cur.fetchall()
        if data in dbdata:
            messagebox.showinfo("message","user already exists")
        else:
            v = (data[0], data[1], data[2], data[3])
            q = "insert into registration (username,password,contact,mail) values(%s,%s,%s,%s)"
            cur.execute(q,v)
            conn.commit()
            wd2.destroy()
            login()


    b3=Button(wd2,text="Register",font="calibri",command=regdb)
    b3.place(x=150,y=275)
    wd2.mainloop()


def form():
    q2="select * from form"
    cur.execute(q2)
    r=cur.fetchall()
    count=50-len(r)
    wd3 = Tk()
    wd3.geometry("470x750")
    wd3.resizable(0,0)
    wd3.title("Form"+" (Seats Available = "+str(count)+")")

    l1 = Label(wd3, text="Fname", font="calibri")
    l1.place(x=20, y=20)
    e1 = Entry(wd3, width=20, font="calibri", border=1, relief="solid")
    e1.place(x=150, y=20)

    l2 = Label(wd3, text="Lname", font="calibri")
    l2.place(x=20, y=80)
    e2 = Entry(wd3, width=20, font="calibri", border=1, relief="solid")
    e2.place(x=150, y=80)

    l3 = Label(wd3, text="Contact", font="calibri")
    l3.place(x=20, y=140)
    e3 = Entry(wd3, width=20, font="calibri", border=1, relief="solid")
    e3.place(x=150, y=140)

    l4 = Label(wd3, text="Email", font="calibri")
    l4.place(x=20, y=200)
    e4 = Entry(wd3, width=20, font="calibri", border=1, relief="solid")
    e4.place(x=150, y=200)

    l5 = Label(wd3, text="Gender", font="calibri")
    l5.place(x=20, y=260)
    rv = IntVar()
    rb1 = Radiobutton(wd3, text="Male", font="calibri", variable=rv, value=1)
    rb1.place(x=150, y=260)
    rb2 = Radiobutton(wd3, text="Female", font="calibri", variable=rv, value=2)
    rb2.place(x=250, y=260)
    rb3 = Radiobutton(wd3, text="Others", font="calibri", variable=rv, value=3)
    rb3.place(x=350, y=260)

    l6 = Label(wd3, text="Hobby", font="calibri")
    l6.place(x=20, y=320)
    cv1 = IntVar()
    cv2 = IntVar()
    cv3 = IntVar()
    cb1 = Checkbutton(wd3, text="Playing", font="calibri", variable=cv1, onvalue=1, offvalue=0)
    cb1.place(x=150, y=320)
    cb2 = Checkbutton(wd3, text="Singing", font="calibri", variable=cv2, onvalue=1, offvalue=0)
    cb2.place(x=250, y=320)
    cb3 = Checkbutton(wd3, text="Reading", font="calibri", variable=cv3, onvalue=1, offvalue=0)
    cb3.place(x=350, y=320)

    l7 = Label(wd3, text="Qualification", font="calibri")
    l7.place(x=20, y=380)
    rv1 = IntVar()
    cb4 = Radiobutton(wd3, text="10th", font="calibri", variable=rv1, value=1)
    cb4.place(x=150, y=380)
    cb5 = Radiobutton(wd3, text="12th", font="calibri", variable=rv1, value=2)
    cb5.place(x=250, y=380)
    cb6 = Radiobutton(wd3, text="Degree", font="calibri", variable=rv1, value=3)
    cb6.place(x=350, y=380)

    l8 = Label(wd3, text="Age", font="calibri")
    l8.place(x=20, y=440)
    age = [i for i in range(20, 41)]
    age.insert(0, "Select Your Age")
    db = ttk.Combobox(wd3, width=14)
    db['value'] = age
    db.place(x=150, y=440)
    db.current(0)

    l9 = Label(wd3, text="Address", font="calibri")
    l9.place(x=20, y=500)
    e5 = Text(wd3, height=5, width=25, font="calibri", border=1, relief="solid")
    e5.place(x=150, y=500)

    def submit():
        if count<=0:
            messagebox.showinfo("Message","No seats available")
        else:
            data = []
            if len(e1.get()) == 0:
                messagebox.showinfo("message", "enter Fname")
            else:
                Fname = e1.get()
                data.append(Fname)
            if len(e2.get()) == 0:
                messagebox.showinfo("message", "enter Lname")
            else:
                Lname = e2.get()
                data.append(Lname)

            if len(e3.get()) == 0:
                messagebox.showinfo("message", "Enter contact no")

            elif len(e3.get()) == 10:
                try:
                    contact = int(e3.get())
                    data.append(contact)
                except ValueError:
                    messagebox.showerror("error", "contact no must be in number format")
            elif 0 < len(e3.get()) < 10:
                messagebox.showerror("message", "contact no must be 10 digit")
            elif len(e3.get()) > 10:
                messagebox.showerror("message", "contact no must be 10 digit")

            if len(e4.get()) == 0:
                messagebox.showinfo("message", "enter Email")
            else:
                email = e4.get()
                data.append(email)

            if rv.get() == 1:
                gender = "Male"
                data.append(gender)
            elif rv.get() == 2:
                gender = "Female"
                data.append(gender)
            elif rv.get() == 3:
                gender = "Others"
                data.append(gender)
            else:
                messagebox.showinfo("message", "select gender")

            hobby = ""
            if cv1.get() == 1:
                hobby = hobby + "Playing "
            if cv2.get() == 1:
                hobby = hobby + "Singing "
            if cv3.get() == 1:
                hobby = hobby + "Reading "
            if cv1.get() == 0 and cv2.get() == 0 and cv3.get() == 0:
                messagebox.showinfo("message", "select hobby")
            data.append(hobby)

            if rv1.get() == 1:
                qualification = "10th"
                data.append(qualification)
            elif rv1.get() == 2:
                qualification = "12th"
                data.append(qualification)
            elif rv1.get() == 3:
                qualification = "Degree"
                data.append(qualification)
            else:
                messagebox.showinfo("message", "enter qualification")

            try:
                age = int(db.get())
                data.append(age)
            except ValueError:
                messagebox.showinfo("message", "select age")

            ad = e5.get("0.1", "end")
            ad = ad.replace("\n", "")
            if len(ad) > 0:
                address = e5.get("0.1", "end")
                address = address.replace("\n", "")
                data.append(address)
            else:
                messagebox.showinfo("message", "enter address")

            data=tuple(data)
            q1="select fname,lname,contact,mail,gender,hobby,qualification,age,address from form"
            cur.execute(q1)
            dbdata=cur.fetchall()
            if data in dbdata:
                messagebox.showinfo("message","Data is already stored")
            else:
                v = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
                q = "insert into form(fname,lname,contact,mail,gender,hobby,qualification,age,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(q, v)
                conn.commit()
                messagebox.showinfo("message", "data submitted successfully.")
        wd3.destroy()

    b1 = Button(wd3, text="Submit", font="calibri", border=1, relief="solid", command=submit)
    b1.place(x=150, y=680)

    # b2=Button(wd,width=15,text="Reset",font="calibri",border=1,relief="solid",command=reset)
    # b2.place(x=250,y=700)

    wd3.mainloop()


def login():
    wd1=Tk()
    wd1.geometry("400x250")
    wd1.title("Login")
    wd1.resizable(0,0)


    l1=Label(wd1,text="Username",font="calibri")
    l1.place(x=20,y=20)
    e1=Entry(wd1,width=20,font="calibri")
    e1.place(x=150,y=20)
    l2=Label(wd1,text="Password",font="calibri")
    l2.place(x=20,y=70)
    e2=Entry(wd1,show="*",width=20,font="calibri")
    e2.place(x=150,y=70)

    def login():
        data=[]
        username=e1.get()
        password=e2.get()
        data.append(username)
        data.append(password)
        data=tuple(data)
        v=(username,password)
        try:
            q2 = "select username,password from registration where username=%s or password=%s"
            cur.execute(q2,v)
            dbdata = cur.fetchall()

            if dbdata[0][0]==username and dbdata[0][1]==password:
                wd1.destroy()
                form()
            elif dbdata[0][0]==username and dbdata[0][1]!=password:
                messagebox.showerror("message","incorrect password")
            elif dbdata[0][0] != username and dbdata[0][1] == password:
                messagebox.showerror("message","incorrect username")
        except IndexError:
            messagebox.showinfo("message", "user does not exists plz register")



    b1=Button(wd1,text="Login",font="calibri",command=login)
    b1.place(x=100,y=150)
    b2=Button(wd1,text="Register",font="calibri",command=lambda:[wd1.destroy(),register()])
    b2.place(x=200,y=150)
    wd1.mainloop()

login()
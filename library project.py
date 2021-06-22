from tkinter import *
from tkinter import messagebox
import mysql.connector as m

conn=m.connect(user='root',password='root',host='localhost',database="library")
cur=conn.cursor()

try:
    def a(event):
        login()
    def login():
        data=[]
        username=e1.get()
        data.append(username)
        password=e2.get()
        data.append(password)
        data=tuple(data)

        q="select username,password from login"
        cur.execute(q)
        dbdata=cur.fetchall()

        if data in dbdata:
            wd1.destroy()
            form()
        else:
            messagebox.showinfo("error","Invalid Credentials")

        e1.delete(0,END)
        e2.delete(0,END)

    class fun:

        def add():
            wd3=Tk()
            wd3.geometry("400x250")
            wd3.title("Add Book")
            wd3.resizable(0,0)
            l1=Label(wd3,text="Book ID",font="calibri")
            l1.place(x=20,y=20)
            e1=Entry(wd3,width=20,font="calibri",border=1,relief="solid")
            e1.place(x=150, y=20)

            l2=Label(wd3,text="Book Name",font="calibri")
            l2.place(x=20, y=80)
            e2=Entry(wd3,width=20,font="calibri",border=1,relief="solid")
            e2.place(x=150, y=80)

            l3=Label(wd3,text="Author Name",font="calibri")
            l3.place(x=20, y=140)
            e3=Entry(wd3,width=20,font="calibri",border=1,relief="solid")
            e3.place(x=150, y=140)

            def dbadd():
                data = []
                bid = int(e1.get())
                data.append(bid)
                name = e2.get()
                data.append(name)
                author = e3.get()
                data.append(author)
                data = tuple(data)
                q1 = "select bid, bname, author,status from books"
                cur.execute(q1)
                dbdata = cur.fetchall()
                if data in dbdata:
                    messagebox.showinfo("message", "Book already exists!")
                else:
                    v = (bid, name, author)
                    q2 = "insert into books(bid,bname,author,status) values(%s,%s,%s,'available')"
                    cur.execute(q2, v)
                    messagebox.showinfo("message", "Book added successfully.")
                    conn.commit()
                    e1.delete(0,END)
                    e2.delete(0,END)
                    e3.delete(0,END)

            b1=Button(wd3, text="Add",font="calibri",command=dbadd)
            b1.place(x=170,y=200)

            wd3.mainloop()



        def delete():
            wd4 = Tk()
            wd4.geometry("400x150")
            wd4.title("Delete Book")
            wd4.resizable(0,0)
            l1 = Label(wd4, text="Book Id", font="calibri")
            l1.place(x=20, y=20)

            e1 = Entry(wd4, width=20, font="calibri", border=1, relief="solid")
            e1.place(x=150, y=20)

            def dbdelete():
                bid = int(e1.get())
                q1="select * from books"
                cur.execute(q1)
                a=cur.fetchall()
                dbdata=list(x[0] for x in a)
                if bid in dbdata:
                    q = ("delete from books where bid=%s") % (bid)
                    cur.execute(q)
                    messagebox.showinfo("message", "Book deleted successfully.")
                    conn.commit()
                else:
                    messagebox.showerror("error","no book with such book id")

            b1 = Button(wd4, text="Delete", font="calibri",command=dbdelete)
            b1.place(x=160, y=80)

            wd4.mainloop()



        def view():

            wd5 = Tk()
            wd5.title("View")
            wd5.geometry("700x500")
            # wd5.resizable(0, 0)
            c = Canvas(wd5)
            sc = Scrollbar(wd5, orient="vertical", command=c.yview)

            frame = Frame(c)
            # group of widgets
            list=["Bid","Bname","Author","status"]
            for i in range(4):
                Label(frame, text=list[i],width=15, font="calibri").grid(row=0, column=i, ipadx=5, ipady=5)

            cur.execute("SELECT * FROM books")
            i=1
            for books in cur:
                for j in range(len(books)):
                    Label(frame, text=books[j],width=15, font="calibri").grid(row=i, column=j, ipadx=5, ipady=5)
                i+=1
            # put the frame in the canvas
            c.create_window(0, 0, anchor='nw', window=frame)
            # make sure everything is displayed before configuring the scrollregion
            c.update_idletasks()

            c.configure(scrollregion=c.bbox('all'),
                        yscrollcommand=sc.set)

            c.pack(fill='both', expand=True, side='left')
            sc.pack(fill='y', side='right')


            # wd5=Tk()
            # wd5.title("View")
            # wd5.geometry("650x500")
            # wd5.resizable(0,0)
            # cur.execute("SELECT bid,bname,author,status FROM books")
            # list=["Bid","Bname","Author","status"]
            # for k in range(4):
            #     l1=Label(wd5,text=list[k],width=10, fg='black',justify="center",font=("calibri"),border=1,relief='flat')
            #     l1.grid(row=0,column=k,pady=10)
            # i=1
            # for books in cur:
            #     for j in range(len(books)):
            #         e = Label(wd5,text=books[j], width=15, fg='black',justify="center",font=("calibri"),border=1,relief='flat')
            #         e.grid(row=i, column=j,pady=10)
            #         # e.insert(END, books[j])
            #     i=i+1

            wd5.mainloop()

        def issue():
            wd6 = Tk()
            wd6.geometry("500x460")
            wd6.title("Issue Book")
            wd6.resizable(0, 0)

            l1 = Label(wd6, text="Book ID", font=("calibri"))
            l1.place(x=50, y=50)
            e1 = Entry(wd6, width=20, font=("calibri"), border=1, relief='solid')
            e1.place(x=250, y=50)

            l2 = Label(wd6, text="Student ID", font=("calibri"))
            l2.place(x=50, y=100)
            e2 = Entry(wd6, width=20, font=("calibri"), border=1, relief='solid')
            e2.place(x=250, y=100)

            l3 = Label(wd6, text="Student Name", font=("calibri"))
            l3.place(x=50, y=150)
            e3 = Entry(wd6, width=20, font=("calibri"), border=1, relief='solid')
            e3.place(x=250, y=150)

            def dbissue():
                bid=int(e1.get())
                sid=int(e2.get())
                sname=e3.get()
                v=(bid,sid,sname)
                q2="select * from books"
                cur.execute(q2)
                a=cur.fetchall()
                dbdata1 = list(x[0] for x in a)
                q3="select * from issue"
                cur.execute(q3)
                b=cur.fetchall()
                dbdata2=list(x[0] for x in b)
                if bid in dbdata1 and bid in dbdata2:
                    messagebox.showinfo("message","Book is currently not available")
                elif bid not in dbdata1:
                    messagebox.showinfo("error","no such book exists")
                elif bid in dbdata1 and bid not in dbdata2:
                    q="insert into issue (bid,sid,sname,idate,edate) values (%s,%s,%s,now(),date_add(now(),interval 15 day))"
                    cur.execute(q,v)
                    q1=("select bid,idate,edate from issue where bid=%s and sid=%s")%(bid,sid)
                    cur.execute(q1)
                    data=cur.fetchall()
                    e4.config(text=data[0][1])
                    e5.config(text=data[0][2])
                    messagebox.showinfo("message","issued successsfully")
                    q2=("update books set status='not available' where bid=%s")%(bid)
                    cur.execute(q2)
                    conn.commit()
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.config(text="")
                e5.config(text="")


            l4 = Label(wd6, text="Book Issue Date", font=("calibri"))
            l4.place(x=50, y=200)
            e4 = Label(wd6,text="", width=20, font=("calibri"), border=1, relief='solid')
            e4.place(x=250, y=200)

            l5 = Label(wd6, text="Expected Return Date", font=("calibri"))
            l5.place(x=50, y=250)
            e5 = Label(wd6,text="", width=20, font=("calibri"), border=1, relief='solid')
            e5.place(x=250, y=250)

            bt = Button(wd6, text="Issue", width=10, font=("calibri"),command=dbissue)
            bt.place(x=185, y=350)

            wd6.mainloop()

        def Return():
            wd7 = Tk()
            wd7.title("Return Book")
            wd7.geometry("350x240")
            wd7.resizable(0, 0)

            l1 = Label(wd7, text="Book ID", font=("calibri"))
            l1.place(x=20, y=30)

            e1 = Entry(wd7, width=20, relief="solid", border=1, font=("calibri"))
            e1.place(x=120, y=30)

            l2 = Label(wd7, text="Student ID", font=("calibri"))
            l2.place(x=20, y=100)

            e2 = Entry(wd7, width=20, relief="solid", border=1, font=("calibri"))
            e2.place(x=120, y=100)

            def dbreturn():
                bid = int(e1.get())
                sid = int(e2.get())
                v = (bid, sid)
                q = "delete from issue where bid=%s and sid=%s"
                cur.execute(q, v)
                messagebox.showinfo("message", "Book return successfull")
                wd7.destroy()
                conn.commit()

            b1 = Button(wd7, text="Return", font=("calibri"), command=dbreturn)
            b1.place(x=130, y=160)

            wd7.mainloop()

        def record():

            wd8 = Tk()
            wd8.title("Issue Record")
            wd8.geometry("1100x600")
            c = Canvas(wd8)
            sc = Scrollbar(wd8, orient="vertical", command=c.yview)

            frame = Frame(c)
            # group of widgets
            list = ["Book Id", "Student Id", "Student Name", "Issue Date","Expected Return Date"]
            for i in range(5):
                Label(frame, text=list[i],width=20, font="calibri").grid(row=0, column=i, ipadx=5, ipady=5)

            cur.execute("SELECT * FROM issue")
            i=1
            for issue in cur:
                for j in range(len(issue)):
                    Label(frame, text=issue[j],width=20, font="calibri").grid(row=i, column=j, ipadx=5, ipady=5)
                i+=1
            # put the frame in the canvas
            c.create_window(0, 0, anchor='nw', window=frame)
            # make sure everything is displayed before configuring the scrollregion
            c.update_idletasks()

            c.configure(scrollregion=c.bbox('all'),
                        yscrollcommand=sc.set)

            c.pack(fill='both', expand=True, side='left')
            sc.pack(fill='y', side='right')



    def form():
        wd2=Tk()
        wd2.geometry("400x400")
        wd2.title("Library")
        wd2.resizable(0,0)
        # bg=PhotoImage(file="library.png")
        # l2=Label(wd2,image=bg)
        # l2.place(x=0,y=0)
        l1=Label(wd2,text="Welcome to Harshal's Library",font=("calibri",18))
        l1.place(x=20,y=10)

        b1=Button(wd2,text="Add Book Detail",width=30,font="calibri",command=fun.add)
        b1.place(x=50,y=80)

        b2=Button(wd2,text="Delete Book",width=30,font="calibri",command=fun.delete)
        b2.place(x=50, y=130)

        b3=Button(wd2,text="View Book List",width=30,font="calibri",command=fun.view)
        b3.place(x=50, y=180)

        b4=Button(wd2,text="Issue Book to student",width=30,font="calibri",command=fun.issue)
        b4.place(x=50, y=230)

        b5=Button(wd2,text="Return Book",width=30,font="calibri",command=fun.Return)
        b5.place(x=50, y=280)

        b6=Button(wd2,text="Issue Record",width=30,font="calibri",command=fun.record)
        b6.place(x=50,y=330)

        wd2.mainloop()




    wd1 = Tk()
    wd1.geometry("400x200")
    wd1.title("Login")
    wd1.resizable(0,0)

    l1=Label(wd1,text="Username",font="calibri")
    l1.place(x=30,y=20)
    l2=Label(wd1,text="Password",font="calibri")
    l2.place(x=30,y=80)

    e1=Entry(wd1,width=20,font="calibri",border=1,relief="solid")
    e1.place(x=150,y=20)
    e2=Entry(wd1,width=20,font="calibri",show="*",border=1,relief="solid")
    e2.place(x=150,y=80)

    b1=Button(wd1,text="Login",font="calibri",command=login)
    b1.place(x=160,y=140)
    wd1.bind('<Return>',a)


    wd1.mainloop()

except TypeError:
    messagebox.showerror("error","Invalid data")
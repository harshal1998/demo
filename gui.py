from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as m

conn=m.connect(user="root",password="root",host="localhost")
cur=conn.cursor()


def submit():
    q1="use formdb"
    cur.execute(q1)
    data=[]
    if len(e1.get())==0:
        messagebox.showinfo("message", "enter Fname")
    else:
        Fname=e1.get()
        data.append(Fname)
    if len(e2.get())==0:
        messagebox.showinfo("message", "enter Lname")
    else:
        Lname=e2.get()
        data.append(Lname)

    if len(e3.get())==0:
        messagebox.showinfo("message", "Enter contact no")

    elif len(e3.get())==10:
        try:
            contact = int(e3.get())
            data.append(contact)
        except ValueError:
            messagebox.showerror("error", "contact no must be in number format")
    elif 0<len(e3.get())<10:
        messagebox.showerror("message","contact no must be 10 digit")
    elif len(e3.get())>10:
        messagebox.showerror("message", "contact no must be 10 digit")


    if len(e4.get())==0:
        messagebox.showinfo("message", "enter Email")
    else:
        email=e4.get()
        data.append(email)

    if rv.get()==1:
        gender="Male"
        data.append(gender)
    elif rv.get()==2:
        gender="Female"
        data.append(gender)
    elif rv.get()==3:
        gender="Others"
        data.append(gender)
    else:
        messagebox.showinfo("message","select gender")

    hobby=""
    if cv1.get()==1:
        hobby=hobby+"Playing "
    if cv2.get()==1:
        hobby=hobby+"Singing "
    if cv3.get()==1:
        hobby=hobby+"Reading "
    if cv1.get()==0 and  cv2.get()==0 and cv3.get()==0:
        messagebox.showinfo("message","select hobby")
    data.append(hobby)

    if rv1.get()==1:
        qualification="10th"
        data.append(qualification)
    elif rv1.get()==2:
        qualification = "12th"
        data.append(qualification)
    elif rv1.get()==3:
        qualification = "Degree"
        data.append(qualification)
    else:
        messagebox.showinfo("message","enter qualification")

    try:
        age = int(db.get())
        data.append(age)
    except ValueError:
        messagebox.showinfo("message","select age")

    ad=e5.get("0.1","end")
    ad=ad.replace("\n","")
    if len(ad)>0:
        address=e5.get("0.1","end")
        address=address.replace("\n","")
        data.append(address)
    else:
        messagebox.showinfo("message","enter address")

    print(data)

    v=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])
    q="insert into uinfo(fname,lname,contact,mail,gender,hobby,qualification,age,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(q,v)
    conn.commit()
    messagebox.showinfo("message","data submitted successfully.")
    wd.destroy()

wd=Tk()
wd.geometry("470x750")
wd.title("Form")

l1=Label(wd,text="Fname",font="calibri")
l1.place(x=20,y=20)
e1=Entry(wd,width=20,font="calibri",border=1,relief="solid")
e1.place(x=150,y=20)

l2=Label(wd,text="Lname",font="calibri")
l2.place(x=20,y=80)
e2=Entry(wd,width=20,font="calibri",border=1,relief="solid")
e2.place(x=150,y=80)

l3=Label(wd,text="Contact",font="calibri")
l3.place(x=20,y=140)
e3=Entry(wd,width=20,font="calibri",border=1,relief="solid")
e3.place(x=150,y=140)

l4=Label(wd,text="Email",font="calibri")
l4.place(x=20,y=200)
e4=Entry(wd,width=20,font="calibri",border=1,relief="solid")
e4.place(x=150,y=200)

l5=Label(wd,text="Gender",font="calibri")
l5.place(x=20,y=260)
rv=IntVar()
rb1=Radiobutton(wd,text="Male",font="calibri",variable=rv,value=1)
rb1.place(x=150,y=260)
rb2=Radiobutton(wd,text="Female",font="calibri",variable=rv,value=2)
rb2.place(x=250,y=260)
rb3=Radiobutton(wd,text="Others",font="calibri",variable=rv,value=3)
rb3.place(x=350,y=260)

l6=Label(wd,text="Hobby",font="calibri")
l6.place(x=20,y=320)
cv1=IntVar()
cv2=IntVar()
cv3=IntVar()
cb1=Checkbutton(wd,text="Playing",font="calibri",variable=cv1,onvalue=1,offvalue=0)
cb1.place(x=150,y=320)
cb2=Checkbutton(wd,text="Singing",font="calibri",variable=cv2,onvalue=1,offvalue=0)
cb2.place(x=250,y=320)
cb3=Checkbutton(wd,text="Reading",font="calibri",variable=cv3, onvalue=1, offvalue=0)
cb3.place(x=350,y=320)

l7=Label(wd,text="Qualification", font="calibri")
l7.place(x=20, y=380)
rv1=IntVar()
cb4=Radiobutton(wd,text="10th", font="calibri", variable=rv1, value=1)
cb4.place(x=150,y=380)
cb5=Radiobutton(wd, text="12th", font="calibri", variable=rv1, value=2)
cb5.place(x=250,y=380)
cb6=Radiobutton(wd, text="Degree", font="calibri", variable=rv1, value=3)
cb6.place(x=350, y=380)

l8=Label(wd,text="Age",font="calibri")
l8.place(x=20,y=440)
age=[i for i in range(20,41)]
age.insert(0,"Select Your Age")
db=ttk.Combobox(wd, width=14)
db['value']=age
db.place(x=150, y=440)
db.current(0)

l9=Label(wd, text="Address", font="calibri")
l9.place(x=20,y=500)
e5=Text(wd,height=5, width=25, font="calibri", border=1, relief="solid")
e5.place(x=150,y=500)

b1=Button(wd,text="Submit", font="calibri", border=1, relief="solid", command=submit)
b1.place(x=150,y=680)

# b2=Button(wd,width=15,text="Reset",font="calibri",border=1,relief="solid",command=reset)
# b2.place(x=250,y=700)

wd.mainloop()

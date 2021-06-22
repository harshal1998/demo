from tkinter import *
from tkinter import messagebox
c=1
def a(x):
    global c
    if c>9:
        messagebox.showinfo("Out of moves")
    elif c%2==0:
        x.config(text="O")
    elif c%2!=0:
        x.config(text="X")
    if c>=5:
        result()
    c += 1

def result():
    v1 = str(b1.cget("text"))
    v2 = str(b2.cget("text"))
    v3 = str(b3.cget("text"))
    v4 = str(b4.cget("text"))
    v5 = str(b5.cget("text"))
    v6 = str(b6.cget("text"))
    v7 = str(b7.cget("text"))
    v8 = str(b8.cget("text"))
    v9 = str(b9.cget("text"))
    if v1!="" and v2!="" and v3!="":
        if v1==v2 and v1==v3:
            messagebox.showinfo("message", v1 + " Player Won")
            wd.destroy()
    if v4 != "" and v5 != "" and v6 != "":
        if v4==v5 and v4==v6:
            messagebox.showinfo("message", v4+" Player Won")
            wd.destroy()
    if v7 != "" and v8 != "" and v9 != "":
        if v7==v8 and v7==v9:
            messagebox.showinfo("message", v7+" Player Won")
            wd.destroy()
    if v1 != "" and v4 != "" and v7 != "":
        if v1==v4 and v1==v7:
            messagebox.showinfo("message", v1+" Player Won")
            wd.destroy()
    if v2 != "" and v5 != "" and v8 != "":
        if v2==v5 and v2==v8:
            messagebox.showinfo("message", v2+" Player Won")
            wd.destroy()
    if v3 != "" and v6 != "" and v9 != "":
        if v3==v6 and v3==v9:
            messagebox.showinfo("message",v3+" Player Won")
            wd.destroy()
    if v1 != "" and v5 != "" and v9 != "":
        if v1==v5 and v1==v9:
            messagebox.showinfo("message",v1+" Player Won")
            wd.destroy()
    if v3 != "" and v5 != "" and v7 != "":
        if v3==v5 and v3==v7:
            messagebox.showinfo("message",v3+" Player Won")
            wd.destroy()
    if v1!="" and v2!="" and v3!="" and v4!="" and v5!="" and v6!="" and v7!="" and v8!="" and v9!="":
        messagebox.showinfo("message","Draw")
        wd.destroy()

wd=Tk()
wd.geometry("300x350")
wd.title("tic tac toe")
wd.resizable(0,0)

b1=Button(wd,text="",border=1,relief="sunken",font=("calibri",15),height=3,width=7,command=lambda:[b1.config(state="disabled"),a(b1)])
b1.grid(row=0,column=0)
b2=Button(wd,text="",border=1,relief="sunken",font=("calibri",15),height=3,width=7,command=lambda:[b2.config(state="disabled"),a(b2)])
b2.grid(row=0,column=1)
b3=Button(wd,text="",border=1,relief="sunken",font=("calibri",15),height=3,width=7,command=lambda:[b3.config(state="disabled"),a(b3)])
b3.grid(row=0,column=2)
b4=Button(wd,text="",border=1,relief="sunken",font=("calibri",15),height=3,width=7,command=lambda:[b4.config(state="disabled"),a(b4)])
b4.grid(row=1,column=0)
b5=Button(wd,text="",border=1,relief="sunken",font=("calibri",15),height=3,width=7,command=lambda:[b5.config(state="disabled"),a(b5)])
b5.grid(row=1,column=1)
b6=Button(wd,text="",border=1,relief="sunken",font=("calibri",15),height=3,width=7,command=lambda:[b6.config(state="disabled"),a(b6)])
b6.grid(row=1,column=2)
b7=Button(wd,text="",border=1,relief="sunken",font=("calibri",15),height=3,width=7,command=lambda:[b7.config(state="disabled"),a(b7)])
b7.grid(row=2,column=0)
b8=Button(wd,text="",border=1,relief="sunken",font=("calibri",15),height=3,width=7,command=lambda:[b8.config(state="disabled"),a(b8)])
b8.grid(row=2,column=1)
b9=Button(wd,text="",border=1,relief="sunken",font=("calibri",15),height=3,width=7,command=lambda:[b9.config(state="disabled"),a(b9)])
b9.grid(row=2,column=2)

wd.mainloop()
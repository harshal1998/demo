import tkinter
import os
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


class file:

    def open():
        a = askopenfile(mode="r", filetypes=[("Python File", "*.py"), ("Text File", "*.txt")])
        # print(os.path.basename(str(a.name)))
        if a == "":
            a = None
        else:
            d = a.read()
            t.delete(1.0, END)
            t.insert(END, d)
            w.title(os.path.basename(a.name))
        f=open(w.title(),"a")

    def new():
        w.title("untitled file")
        file = None
        t.delete(1.0, END)

    def save():
        print(w.title())
        if w.title()=="untitled file" or w.title()=="Notepad":
            print("save function")
            b = asksaveasfilename(defaultextension=".txt",initialfile="untitled.txt", filetypes=[("Python File", "*.py"), ("Text File", "*.txt")])
            if b == "":
                b = None
            else:
                file = open(b, "a")
                file.write(t.get(1.0, END))
                file.close()
                w.title(os.path.basename(b))
        else:
            file = open(w.title(),"a")
            file.write(t.get(1.0,END))
            print("append")
            file.close()



    def saveas():
        b = asksaveasfilename(defaultextension=".txt", initialfile="untitled.txt",
                              filetypes=[("Python File", "*.py"), ("Text File", "*.txt")])
        if b == "":
            b = None
        else:
            file = open(b, "a")
            file.write(t.get(1.0, END))
            file.close()
            w.title(os.path.basename(b))

    def exit():
        w.destroy()


class edit:

    def undo():
        t.event_generate("<<Undo>>")

    def cut():
        t.event_generate("<<Cut>>")

    def copy():
        t.event_generate("<<Copy>>")

    def paste():
        t.event_generate("<<Paste>>")


w = Tk()
w.geometry("500x500")
w.title("Notepad")

mb = Menu(w)

f = Menu(mb, tearoff=0)
f.add_command(label="Open", command=file.open)
f.add_command(label="New", command=file.new)
f.add_separator()
f.add_command(label="Save", command=file.save)
f.add_command(label="Saveas", command=file.saveas)
f.add_separator()
f.add_command(label="Exit", command=file.exit)
mb.add_cascade(label="File", menu=f)

e = Menu(mb, tearoff=0)
e.add_command(label="Undo", command=edit.undo)
e.add_separator()
e.add_command(label="Cut", command=edit.cut)
e.add_command(label="Copy", command=edit.copy)
e.add_command(label="Paste", command=edit.paste)
mb.add_cascade(label="Edit", menu=e)

w.config(menu=mb)

sc = Scrollbar(w)
sc.pack(side=RIGHT)

t = Text(w, height=1000, width=490, yscrollcommand=sc.set)
t.pack(side=LEFT)

sc.config(command=t.yview)

w.mainloop()

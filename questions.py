from tkinter import *
from tkinter import messagebox

run = True
s = 0
m = 30


def java():
    def countdown():

        global run, s, m
        if s < 10:
            s = "0" + str(s)
        # Delete old text
        c.delete('cl1')
        # Add new text
        cl1 = Label(c, anchor=CENTER, text="Timer : %s:%s" % (m, s), font=("calibri")).place(x=760, y=16)
        s = int(s)
        if s <= 0:
            s = 59
            m -= 1
        elif s > 0:
            s -= 1
        if str(m) + str(s) == "0500":
            messagebox.showinfo("message", "Only 5 minutes remaining.")
        if str(m) + str(s) == "0000":
            score()
            messagebox.showinfo("message", "Your answers submitted successfully")
            w.destroy()

        # After 1 second, call Run again (start an infinite recursive loop)
        w.after(1000, countdown)

    w = Tk()
    w.title("Java")
    w.geometry("900x800")

    c = Canvas(w, height=500, width=500)

    sc = Scrollbar(w, orient="vertical", command=c.yview)
    sc.pack(side='right', fill='y')

    f = Frame(c)

    Label(f, text="Java MCQ(Multiple Choice Questions)", font=("calibri", 25)).grid(row=0, sticky=W, ipadx=20)

    mv1 = IntVar()

    Label(f, text="1) Which of the following is not a Java features? ", font="calibri").grid(row=2, sticky=W, ipadx=20,
                                                                                             ipady=10)
    Radiobutton(f, text="  Dynamic", font='calibri', variable=mv1, value=1, tristatevalue=0,
                command=lambda: [mv1.set(1)]).grid(row=3, sticky=W, ipadx=60)
    Radiobutton(f, text="  Architecture Neutral", font='calibri', variable=mv1, value=2, tristatevalue=0,
                command=lambda: [mv1.set(2)]).grid(row=4, sticky=W, ipadx=60)
    Radiobutton(f, text="  Use of pointers.", font='calibri', variable=mv1, value=3, tristatevalue=0,
                command=lambda: [mv1.set(3)]).grid(row=5, sticky=W, ipadx=60)
    Radiobutton(f, text="  Object-oriented", font='calibri', variable=mv1, value=4, tristatevalue=0,
                command=lambda: [mv1.set(4)]).grid(row=6, sticky=W, ipadx=60)

    mv2 = IntVar()
    Label(f, text="2) The \u0021 article referred to as a ", font="calibri").grid(row=7, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="  Line Feed", font='calibri', variable=mv2, value=1, tristatevalue=0,
                command=lambda: [mv2.set(1)]).grid(row=8, sticky=W, ipadx=60)
    Radiobutton(f, text="  Octal escape", font='calibri', variable=mv2, value=2, tristatevalue=0,
                command=lambda: [mv2.set(2)]).grid(row=9, sticky=W, ipadx=60)
    Radiobutton(f, text="  Hexadecimal", font='calibri', variable=mv2, value=3, tristatevalue=0,
                command=lambda: [mv2.set(3)]).grid(row=10, sticky=W, ipadx=60)
    Radiobutton(f, text="  Unicode escape sequence.", font='calibri', variable=mv2, value=4, tristatevalue=0,
                command=lambda: [mv2.set(4)]).grid(row=11, sticky=W, ipadx=60)

    mv3 = IntVar()
    Label(f, text="3) _____ is used to find and fix bugs in the Java programs. ", font="calibri").grid(row=12, sticky=W,
                                                                                                       ipadx=20,
                                                                                                       ipady=10)
    Radiobutton(f, text="  JVM", font='calibri', variable=mv3, value=1, tristatevalue=0,
                command=lambda: [mv3.set(1)]).grid(row=13, sticky=W, ipadx=60)
    Radiobutton(f, text="  JRE", font='calibri', variable=mv3, value=2, tristatevalue=0,
                command=lambda: [mv3.set(2)]).grid(row=14, sticky=W, ipadx=60)
    Radiobutton(f, text="  JDK", font='calibri', variable=mv3, value=3, tristatevalue=0,
                command=lambda: [mv3.set(3)]).grid(row=15, sticky=W, ipadx=60)
    Radiobutton(f, text="  JDB.", font='calibri', variable=mv3, value=4, tristatevalue=0,
                command=lambda: [mv3.set(4)]).grid(row=16, sticky=W, ipadx=60)

    mv4 = IntVar()
    Label(f, text="4) What is the return type of the hashCode() method in the Object class?", font="calibri").grid(
        row=17, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="Object", font='calibri', variable=mv4, value=1, tristatevalue=0,
                command=lambda: [mv4.set(1)]).grid(row=18, sticky=W, ipadx=60)
    Radiobutton(f, text="int.", font='calibri', variable=mv4, value=2, tristatevalue=0,
                command=lambda: [mv4.set(2)]).grid(row=19, sticky=W, ipadx=60)
    Radiobutton(f, text="long", font='calibri', variable=mv4, value=3, tristatevalue=0,
                command=lambda: [mv4.set(3)]).grid(row=20, sticky=W, ipadx=60)
    Radiobutton(f, text="void", font='calibri', variable=mv4, value=4, tristatevalue=0,
                command=lambda: [mv4.set(4)]).grid(row=21, sticky=W, ipadx=60)

    mv5 = IntVar()
    Label(f, text="5) Which of the following is a valid long literal?", font="calibri").grid(row=22, sticky=W, ipadx=20,
                                                                                             ipady=10)
    Radiobutton(f, text="ABH8097", font='calibri', variable=mv5, value=1, tristatevalue=0,
                command=lambda: [mv5.set(1)]).grid(row=23, sticky=W, ipadx=60)
    Radiobutton(f, text="L990023", font='calibri', variable=mv5, value=2, tristatevalue=0,
                command=lambda: [mv5.set(2)]).grid(row=24, sticky=W, ipadx=60)
    Radiobutton(f, text="904423", font='calibri', variable=mv5, value=3, tristatevalue=0,
                command=lambda: [mv5.set(3)]).grid(row=25, sticky=W, ipadx=60)
    Radiobutton(f, text="0xnf029L.", font='calibri', variable=mv5, value=4, tristatevalue=0,
                command=lambda: [mv5.set(4)]).grid(row=26, sticky=W, ipadx=60)

    mv6 = IntVar()
    Label(f, text="6) What does the expression float a = 35 / 0 return?", font="calibri").grid(row=27, sticky=W,
                                                                                               ipadx=20, ipady=10)
    Radiobutton(f, text="0", font='calibri', variable=mv6, value=1, tristatevalue=0, command=lambda: [mv6.set(1)]).grid(
        row=28, sticky=W, ipadx=60)
    Radiobutton(f, text="Not a Number", font='calibri', variable=mv6, value=2, tristatevalue=0,
                command=lambda: [mv6.set(2)]).grid(row=29, sticky=W, ipadx=60)
    Radiobutton(f, text="Infinity.", font='calibri', variable=mv6, value=3, tristatevalue=0,
                command=lambda: [mv6.set(3)]).grid(row=30, sticky=W, ipadx=60)
    Radiobutton(f, text="Run time exception", font='calibri', variable=mv6, value=4, tristatevalue=0,
                command=lambda: [mv6.set(4)]).grid(row=31, sticky=W, ipadx=60)

    mv7 = IntVar()
    Label(f, text="7) Which of the following creates a List of 3 visible items and multiple selections abled?",
          font="calibri").grid(row=32, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="new List(false, 3)", font='calibri', variable=mv7, value=1, tristatevalue=0,
                command=lambda: [mv7.set(1)]).grid(row=33, sticky=W, ipadx=60)
    Radiobutton(f, text="new List(3, true).", font='calibri', variable=mv7, value=2, tristatevalue=0,
                command=lambda: [mv7.set(2)]).grid(row=34, sticky=W, ipadx=60)
    Radiobutton(f, text="new List(true, 3)", font='calibri', variable=mv7, value=3, tristatevalue=0,
                command=lambda: [mv7.set(3)]).grid(row=35, sticky=W, ipadx=60)
    Radiobutton(f, text="new List(3, false)", font='calibri', variable=mv7, value=4, tristatevalue=0,
                command=lambda: [mv7.set(4)]).grid(row=36, sticky=W, ipadx=60)

    mv8 = IntVar()
    Label(f,
          text="8)  Which method of the Class.class is used to determine the name of a class represented by the class object as a String?",
          font="calibri").grid(row=37, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="getClass()", font='calibri', variable=mv8, value=1, tristatevalue=0,
                command=lambda: [mv8.set(1)]).grid(row=38, sticky=W, ipadx=60)
    Radiobutton(f, text="intern()", font='calibri', variable=mv8, value=2, tristatevalue=0,
                command=lambda: [mv8.set(2)]).grid(row=39, sticky=W, ipadx=60)
    Radiobutton(f, text="getName().", font='calibri', variable=mv8, value=3, tristatevalue=0,
                command=lambda: [mv8.set(3)]).grid(row=40, sticky=W, ipadx=60)
    Radiobutton(f, text="toString()", font='calibri', variable=mv8, value=4, tristatevalue=0,
                command=lambda: [mv8.set(4)]).grid(row=41, sticky=W, ipadx=60)

    mv9 = IntVar()
    Label(f, text="9) In which process, a local variable has the same name as one of the instance variables?",
          font="calibri").grid(row=42, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="Serialization", font='calibri', variable=mv9, value=1, tristatevalue=0,
                command=lambda: [mv9.set(1)]).grid(row=43, sticky=W, ipadx=60)
    Radiobutton(f, text="Variable Shadowing.", font='calibri', variable=mv9, value=2, tristatevalue=0,
                command=lambda: [mv9.set(2)]).grid(row=44, sticky=W, ipadx=60)
    Radiobutton(f, text="Abstraction", font='calibri', variable=mv9, value=3, tristatevalue=0,
                command=lambda: [mv9.set(3)]).grid(row=45, sticky=W, ipadx=60)
    Radiobutton(f, text="Multi-threading", font='calibri', variable=mv9, value=4, tristatevalue=0,
                command=lambda: [mv9.set(4)]).grid(row=46, sticky=W, ipadx=60)

    mv10 = IntVar()
    Label(f, text="10) Which package contains the Random class?", font="calibri").grid(row=47, sticky=W, ipadx=20,
                                                                                       ipady=10)
    Radiobutton(f, text="java.util package.", font='calibri', variable=mv10, value=1, tristatevalue=0,
                command=lambda: [mv10.set(1)]).grid(row=48, sticky=W, ipadx=60)
    Radiobutton(f, text="java.lang package", font='calibri', variable=mv10, value=2, tristatevalue=0,
                command=lambda: [mv10.set(2)]).grid(row=49, sticky=W, ipadx=60)
    Radiobutton(f, text="java.awt package", font='calibri', variable=mv10, value=3, tristatevalue=0,
                command=lambda: [mv10.set(3)]).grid(row=50, sticky=W, ipadx=60)
    Radiobutton(f, text="java.io package", font='calibri', variable=mv10, value=4, tristatevalue=0,
                command=lambda: [mv10.set(4)]).grid(row=51, sticky=W, ipadx=60)

    mv11 = IntVar()
    Label(f,
          text="11) Which of the following modifiers can be used for a variable so that it can be accessed by any thread or a part of a program?",
          font="calibri").grid(row=52, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="global", font='calibri', variable=mv11, value=1, tristatevalue=0,
                command=lambda: [mv11.set(1)]).grid(row=53, sticky=W, ipadx=60)
    Radiobutton(f, text="transient", font='calibri', variable=mv11, value=2, tristatevalue=0,
                command=lambda: [mv11.set(2)]).grid(row=54, sticky=W, ipadx=60)
    Radiobutton(f, text="volatile.", font='calibri', variable=mv11, value=3, tristatevalue=0,
                command=lambda: [mv11.set(3)]).grid(row=55, sticky=W, ipadx=60)
    Radiobutton(f, text="default", font='calibri', variable=mv11, value=4, tristatevalue=0,
                command=lambda: [mv11.set(4)]).grid(row=56, sticky=W, ipadx=60)

    mv12 = IntVar()
    Label(f, text="12) Which of the following is an immediate subclass of the Panel class?", font="calibri").grid(
        row=57, sticky=W, ipadx=20,
        ipady=10)
    Radiobutton(f, text="Applet class.", font='calibri', variable=mv12, value=1, tristatevalue=0,
                command=lambda: [mv12.set(1)]).grid(row=58, sticky=W, ipadx=60)
    Radiobutton(f, text="Window class", font='calibri', variable=mv12, value=2, tristatevalue=0,
                command=lambda: [mv12.set(2)]).grid(row=59, sticky=W, ipadx=60)
    Radiobutton(f, text="Frame class", font='calibri', variable=mv12, value=3, tristatevalue=0,
                command=lambda: [mv12.set(3)]).grid(row=60, sticky=W, ipadx=60)
    Radiobutton(f, text="Dialog class", font='calibri', variable=mv12, value=4, tristatevalue=0,
                command=lambda: [mv12.set(4)]).grid(row=61, sticky=W, ipadx=60)

    mv13 = IntVar()
    Label(f, text="13) In which memory a String is stored, when we create a string using new operator?",
          font="calibri").grid(row=62, sticky=W, ipadx=20,
                               ipady=10)
    Radiobutton(f, text="Stack", font='calibri', variable=mv13, value=1, tristatevalue=0,
                command=lambda: [mv13.set(1)]).grid(row=63, sticky=W, ipadx=60, )
    Radiobutton(f, text="String memory", font='calibri', variable=mv13, value=2, tristatevalue=0,
                command=lambda: [mv13.set(2)]).grid(row=64, sticky=W, ipadx=60)
    Radiobutton(f, text="Heap memory.", font='calibri', variable=mv13, value=3, tristatevalue=0,
                command=lambda: [mv13.set(3)]).grid(row=65, sticky=W, ipadx=60, )
    Radiobutton(f, text="Random storage space", font='calibri', variable=mv13, value=4, tristatevalue=0,
                command=lambda: [mv13.set(4)]).grid(row=66, sticky=W, ipadx=60)

    mv14 = IntVar()
    Label(f, text="14) Which of the following is a reserved keyword in Java?", font="calibri").grid(row=67, sticky=W,
                                                                                                    ipadx=20,
                                                                                                    ipady=10)
    Radiobutton(f, text="object", font='calibri', variable=mv14, value=1, tristatevalue=0,
                command=lambda: [mv14.set(1)]).grid(row=68, sticky=W, ipadx=60, )
    Radiobutton(f, text="strictfp.", font='calibri', variable=mv14, value=2, tristatevalue=0,
                command=lambda: [mv14.set(2)]).grid(row=69, sticky=W, ipadx=60)
    Radiobutton(f, text="main", font='calibri', variable=mv14, value=3, tristatevalue=0,
                command=lambda: [mv14.set(3)]).grid(row=70, sticky=W, ipadx=60, )
    Radiobutton(f, text="system", font='calibri', variable=mv14, value=4, tristatevalue=0,
                command=lambda: [mv14.set(4)]).grid(row=71, sticky=W, ipadx=60)

    mv15 = IntVar()
    Label(f, text="15) Which keyword is used for accessing the features of a package?", font="calibri").grid(row=72,
                                                                                                             sticky=W,
                                                                                                             ipadx=20,
                                                                                                             ipady=10)
    Radiobutton(f, text="package", font='calibri', variable=mv15, value=1, tristatevalue=0,
                command=lambda: [mv15.set(1)]).grid(row=73, sticky=W, ipadx=60, )
    Radiobutton(f, text="import.", font='calibri', variable=mv15, value=2, tristatevalue=0,
                command=lambda: [mv15.set(2)]).grid(row=74, sticky=W, ipadx=60)
    Radiobutton(f, text="extends", font='calibri', variable=mv15, value=3, tristatevalue=0,
                command=lambda: [mv15.set(3)]).grid(row=75, sticky=W, ipadx=60, )
    Radiobutton(f, text="export", font='calibri', variable=mv15, value=4, tristatevalue=0,
                command=lambda: [mv15.set(4)]).grid(row=76, sticky=W, ipadx=60)

    def score():

        sdata = []
        score = 0
        mv = ["mv", mv1, mv2, mv3, mv4, mv5, mv6, mv7, mv8, mv9, mv10, mv11, mv12, mv13, mv14, mv15]
        ans = ["mv", 3, 4, 4, 2, 4, 3, 2, 3, 2, 1, 3, 1, 3, 2, 2]
        for i in range(1, 15):
            if i > 0:
                v = mv[i].get()
                if v == ans[i]:
                    score += 1
                mv1.set(0)
        messagebox.showinfo("score", "score: " + str(score))
        w.destroy()

    b1 = Button(c, text="Submit", font='calibri', command=score)
    b1.place(x=800, y=50)

    c.create_window(0, 0, anchor='nw', window=f)
    c.update_idletasks()
    c.configure(scrollregion=c.bbox('all'), yscrollcommand=sc.set)
    c.pack(fill='both', expand=True, side='left')

    w.after(1, countdown)
    w.mainloop()


# java()


def C():
    def countdown():
        global run, s, m
        if s < 10:
            s = "0" + str(s)
        # Delete old text
        c.delete('cl1')
        # Add new text
        cl1 = Label(c, anchor=CENTER, text="Timer : %s:%s" % (m, s), font=("calibri")).place(x=760, y=16)
        s = int(s)
        if s <= 0:
            s = 59
            m -= 1
        elif s > 0:
            s -= 1
        if str(m) + str(s) == "0500":
            messagebox.showinfo("message", "Only 5 minutes remaining.")
        if str(m) + str(s) == "0000":
            submit()
            messagebox.showinfo("message", "Your answers submitted successfully")

        # After 1 second, call Run again (start an infinite recursive loop)
        w.after(1000, countdown)

    w = Tk()
    w.geometry("900x800")
    w.title("C++")

    c = Canvas(w, height=500, width=500)

    sc = Scrollbar(w, orient="vertical", command=c.yview)
    sc.pack(side='right', fill='y')

    f = Frame(c)
    # group of widgets
    # cl=Label(f,text="Timer :",font=("calibri")).grid(row=0,column=2,ipadx=130)

    hl = Label(f, text="C++ MCQ(Multiple Choice Questions)", font=("calibri", 25)).grid(row=0, sticky=W, ipadx=20)

    mv1 = IntVar()
    Label(f, text="1) Which of the following is the correct identifier? ", font="calibri").grid(row=2, sticky=W,
                                                                                                ipadx=20, ipady=10)
    Radiobutton(f, text="  $var_name", font='calibri', variable=mv1, value=1, tristatevalue=0,
                command=lambda: [mv1.set(1)]).grid(row=3, sticky=W, ipadx=60)
    Radiobutton(f, text="  VAR_123.", font='calibri', variable=mv1, value=2, tristatevalue=0,
                command=lambda: [mv1.set(2)]).grid(row=4, sticky=W, ipadx=60)
    Radiobutton(f, text="  varname@", font='calibri', variable=mv1, value=3, tristatevalue=0,
                command=lambda: [mv1.set(3)]).grid(row=5, sticky=W, ipadx=60)
    Radiobutton(f, text="  None of the above", font='calibri', variable=mv1, value=4, tristatevalue=0,
                command=lambda: [mv1.set(4)]).grid(row=6, sticky=W, ipadx=60)

    mv2 = IntVar()
    Label(f, text="2) Which of the following is the address operator?", font="calibri").grid(row=7, sticky=W, ipadx=20,
                                                                                             ipady=10)
    Radiobutton(f, text="  @", font='calibri', variable=mv2, value=1, tristatevalue=0,
                command=lambda: [mv2.set(1)]).grid(row=8, sticky=W, ipadx=60)
    Radiobutton(f, text="  #", font='calibri', variable=mv2, value=2, tristatevalue=0,
                command=lambda: [mv2.set(2)]).grid(row=9, sticky=W, ipadx=60)
    Radiobutton(f, text="  &.", font='calibri', variable=mv2, value=3, tristatevalue=0,
                command=lambda: [mv2.set(3)]).grid(row=10, sticky=W, ipadx=60)
    Radiobutton(f, text="  %", font='calibri', variable=mv2, value=4, tristatevalue=0,
                command=lambda: [mv2.set(4)]).grid(row=11, sticky=W, ipadx=60)

    mv3 = IntVar()
    Label(f,
          text="3) Which of the following features must be supported by any programming language to become a pure object-oriented programming language?",
          font="calibri").grid(row=12, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="  Encapsulation", font='calibri', variable=mv3, value=1, tristatevalue=0,
                command=lambda: [mv3.set(1)]).grid(row=13, sticky=W, ipadx=60)
    Radiobutton(f, text="  Inheritance", font='calibri', variable=mv3, value=2, tristatevalue=0,
                command=lambda: [mv3.set(2)]).grid(row=14, sticky=W, ipadx=60)
    Radiobutton(f, text="  JDK", font='calibri', variable=mv3, value=3, tristatevalue=0,
                command=lambda: [mv3.set(3)]).grid(row=15, sticky=W, ipadx=60)
    Radiobutton(f, text="  Polymorphism.", font='calibri', variable=mv3, value=4, tristatevalue=0,
                command=lambda: [mv3.set(4)]).grid(row=16, sticky=W, ipadx=60)

    mv4 = IntVar()
    Label(f, text="4) The programming language that has the ability to create new data types is called___.",
          font="calibri").grid(row=17, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="Overloaded", font='calibri', variable=mv4, value=1, tristatevalue=0,
                command=lambda: [mv4.set(1)]).grid(row=18, sticky=W, ipadx=60)
    Radiobutton(f, text="Encapsulated", font='calibri', variable=mv4, value=2, tristatevalue=0,
                command=lambda: [mv4.set(2)]).grid(row=19, sticky=W, ipadx=60)
    Radiobutton(f, text="Reprehensible", font='calibri', variable=mv4, value=3, tristatevalue=0,
                command=lambda: [mv4.set(3)]).grid(row=20, sticky=W, ipadx=60)
    Radiobutton(f, text="Extensible.", font='calibri', variable=mv4, value=4, tristatevalue=0,
                command=lambda: [mv4.set(4)]).grid(row=21, sticky=W, ipadx=60)

    mv5 = IntVar()
    Label(f, text="5) Which of the following is the original creator of the C++ language?", font="calibri").grid(row=22,
                                                                                                                 sticky=W,
                                                                                                                 ipadx=20,
                                                                                                                 ipady=10)
    Radiobutton(f, text="Dennis Ritchie", font='calibri', variable=mv5, value=1, tristatevalue=0,
                command=lambda: [mv5.set(1)]).grid(row=23, sticky=W, ipadx=60)
    Radiobutton(f, text="Ken Thompson", font='calibri', variable=mv5, value=2, tristatevalue=0,
                command=lambda: [mv5.set(2)]).grid(row=24, sticky=W, ipadx=60)
    Radiobutton(f, text="Bjarne Stroustrup.", font='calibri', variable=mv5, value=3, tristatevalue=0,
                command=lambda: [mv5.set(3)]).grid(row=25, sticky=W, ipadx=60)
    Radiobutton(f, text="Brian Kernighan", font='calibri', variable=mv5, value=4, tristatevalue=0,
                command=lambda: [mv5.set(4)]).grid(row=26, sticky=W, ipadx=60)

    mv6 = IntVar()
    Label(f,
          text="6) Which of the following is the correct syntax to read the single character to console in the C++ language?",
          font="calibri").grid(row=27, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="Read ch()", font='calibri', variable=mv6, value=1, tristatevalue=0,
                command=lambda: [mv6.set(1)]).grid(row=28, sticky=W, ipadx=60)
    Radiobutton(f, text="Getline vh()", font='calibri', variable=mv6, value=2, tristatevalue=0,
                command=lambda: [mv6.set(2)]).grid(row=29, sticky=W, ipadx=60)
    Radiobutton(f, text="get(ch).", font='calibri', variable=mv6, value=3, tristatevalue=0,
                command=lambda: [mv6.set(3)]).grid(row=30, sticky=W, ipadx=60)
    Radiobutton(f, text="Scanf(ch)", font='calibri', variable=mv6, value=4, tristatevalue=0,
                command=lambda: [mv6.set(4)]).grid(row=31, sticky=W, ipadx=60)

    mv7 = IntVar()
    Label(f,
          text="7) Which of the following features is required to be supported by the programming language to become a pure object-oriented programming language?",
          font="calibri").grid(row=32, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="Encapsulation", font='calibri', variable=mv7, value=1, tristatevalue=0,
                command=lambda: [mv7.set(1)]).grid(row=33, sticky=W, ipadx=60)
    Radiobutton(f, text="Inheritance", font='calibri', variable=mv7, value=2, tristatevalue=0,
                command=lambda: [mv7.set(2)]).grid(row=34, sticky=W, ipadx=60)
    Radiobutton(f, text="Polymorphism", font='calibri', variable=mv7, value=3, tristatevalue=0,
                command=lambda: [mv7.set(3)]).grid(row=34, sticky=W, ipadx=60)
    Radiobutton(f, text="All of the above.", font='calibri', variable=mv7, value=4, tristatevalue=0,
                command=lambda: [mv7.set(4)]).grid(row=35, sticky=W, ipadx=60)

    mv8 = IntVar()
    Label(f,
          text="8)  Which of the following comment syntax is correct to create a single-line comment in the C++ program?",
          font="calibri").grid(row=36, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="//Comment.", font='calibri', variable=mv8, value=1, tristatevalue=0,
                command=lambda: [mv8.set(1)]).grid(row=37, sticky=W, ipadx=60)
    Radiobutton(f, text="/Comment/", font='calibri', variable=mv8, value=2, tristatevalue=0,
                command=lambda: [mv8.set(2)]).grid(row=38, sticky=W, ipadx=60)
    Radiobutton(f, text="Comment//", font='calibri', variable=mv8, value=3, tristatevalue=0,
                command=lambda: [mv8.set(3)]).grid(row=39, sticky=W, ipadx=60)
    Radiobutton(f, text="None of the above", font='calibri', variable=mv8, value=4, tristatevalue=0,
                command=lambda: [mv8.set(4)]).grid(row=40, sticky=W, ipadx=60)

    mv9 = IntVar()
    Label(f, text="9) C++ is a ___ type of language.", font="calibri").grid(row=41, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="High-level Language", font='calibri', variable=mv9, value=1, tristatevalue=0,
                command=lambda: [mv9.set(1)]).grid(row=42, sticky=W, ipadx=60)
    Radiobutton(f, text="Low-level language", font='calibri', variable=mv9, value=2, tristatevalue=0,
                command=lambda: [mv9.set(2)]).grid(row=43, sticky=W, ipadx=60)
    Radiobutton(f, text="Middle-level language.", font='calibri', variable=mv9, value=3, tristatevalue=0,
                command=lambda: [mv9.set(3)]).grid(row=44, sticky=W, ipadx=60)
    Radiobutton(f, text="None of the above", font='calibri', variable=mv9, value=4, tristatevalue=0,
                command=lambda: [mv9.set(4)]).grid(row=45, sticky=W, ipadx=60)

    mv10 = IntVar()
    Label(f,
          text="10) If we stored five elements or data items in an array, what will be the index address or the index number of the array's last data item?",
          font="calibri").grid(row=46, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="3", font='calibri', variable=mv10, value=1, tristatevalue=0,
                command=lambda: [mv10.set(1)]).grid(row=47, sticky=W, ipadx=60)
    Radiobutton(f, text="5", font='calibri', variable=mv10, value=2, tristatevalue=0,
                command=lambda: [mv10.set(2)]).grid(row=48, sticky=W, ipadx=60)
    Radiobutton(f, text="4.", font='calibri', variable=mv10, value=3, tristatevalue=0,
                command=lambda: [mv10.set(3)]).grid(row=49, sticky=W, ipadx=60)
    Radiobutton(f, text="88", font='calibri', variable=mv10, value=4, tristatevalue=0,
                command=lambda: [mv10.set(4)]).grid(row=50, sticky=W, ipadx=60)

    mv11 = IntVar()
    Label(f, text="11) Which type of memory is used by an Array in C++ programming language?", font="calibri").grid(
        row=51, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="Contiguous.", font='calibri', variable=mv11, value=1, tristatevalue=0,
                command=lambda: [mv11.set(1)]).grid(row=52, sticky=W, ipadx=60)
    Radiobutton(f, text="None-contiguous", font='calibri', variable=mv11, value=2, tristatevalue=0,
                command=lambda: [mv11.set(2)]).grid(row=53, sticky=W, ipadx=60)
    Radiobutton(f, text="Both A and B", font='calibri', variable=mv11, value=3, tristatevalue=0,
                command=lambda: [mv11.set(3)]).grid(row=54, sticky=W, ipadx=60)
    Radiobutton(f, text="Not mentioned", font='calibri', variable=mv11, value=4, tristatevalue=0,
                command=lambda: [mv11.set(4)]).grid(row=55, sticky=W, ipadx=60)

    mv12 = IntVar()
    Label(f,
          text="12) Elements of a one-dimensional array are numbered as 0,1,2,3,4,5, and so on; these numbers are known as ___",
          font="calibri").grid(row=56, sticky=W, ipadx=20,
                               ipady=10)
    Radiobutton(f, text="Subscript of Array", font='calibri', variable=mv12, value=1, tristatevalue=0,
                command=lambda: [mv12.set(1)]).grid(row=57, sticky=W, ipadx=60, )
    Radiobutton(f, text="Members of Array", font='calibri', variable=mv12, value=2, tristatevalue=0,
                command=lambda: [mv12.set(2)]).grid(row=58, sticky=W, ipadx=60)
    Radiobutton(f, text="Index values", font='calibri', variable=mv12, value=3, tristatevalue=0,
                command=lambda: [mv12.set(3)]).grid(row=59, sticky=W, ipadx=60, )
    Radiobutton(f, text="Both A and C.", font='calibri', variable=mv12, value=4, tristatevalue=0,
                command=lambda: [mv12.set(4)]).grid(row=60, sticky=W, ipadx=60)

    mv13 = IntVar()
    Label(f,
          text="13) Which of the following refers to the wrapping of data and its functionality into a single individual entity?",
          font="calibri").grid(row=61, sticky=W, ipadx=20,
                               ipady=10)
    Radiobutton(f, text="Modularity", font='calibri', variable=mv13, value=1, tristatevalue=0,
                command=lambda: [mv13.set(1)]).grid(row=62, sticky=W, ipadx=60, )
    Radiobutton(f, text="Abstraction", font='calibri', variable=mv13, value=2, tristatevalue=0,
                command=lambda: [mv13.set(2)]).grid(row=63, sticky=W, ipadx=60)
    Radiobutton(f, text="Encapsulation.", font='calibri', variable=mv13, value=3, tristatevalue=0,
                command=lambda: [mv13.set(3)]).grid(row=64, sticky=W, ipadx=60, )
    Radiobutton(f, text="None of the above", font='calibri', variable=mv13, value=4, tristatevalue=0,
                command=lambda: [mv13.set(4)]).grid(row=65, sticky=W, ipadx=60)

    mv14 = IntVar()
    Label(f, text="14) Which of the following refers to using the existing code instead of rewriting it?",
          font="calibri").grid(row=66, sticky=W, ipadx=20,
                               ipady=10)
    Radiobutton(f, text="Inheritance.", font='calibri', variable=mv14, value=1, tristatevalue=0,
                command=lambda: [mv14.set(1)]).grid(row=67, sticky=W, ipadx=60, )
    Radiobutton(f, text="Encapsulation", font='calibri', variable=mv14, value=2, tristatevalue=0,
                command=lambda: [mv14.set(2)]).grid(row=68, sticky=W, ipadx=60)
    Radiobutton(f, text="Abstraction", font='calibri', variable=mv14, value=3, tristatevalue=0,
                command=lambda: [mv14.set(3)]).grid(row=69, sticky=W, ipadx=60, )
    Radiobutton(f, text="Both A and B", font='calibri', variable=mv14, value=4, tristatevalue=0,
                command=lambda: [mv14.set(4)]).grid(row=70, sticky=W, ipadx=60)

    mv15 = IntVar()
    Label(f, text="15) Among the following given options, which can be considered as a member of a class?",
          font="calibri").grid(row=71, sticky=W, ipadx=20,
                               ipady=10)
    Radiobutton(f, text="Class variable", font='calibri', variable=mv15, value=1, tristatevalue=0,
                command=lambda: [mv15.set(1)]).grid(row=72, sticky=W, ipadx=60, )
    Radiobutton(f, text="Member variable.", font='calibri', variable=mv15, value=2, tristatevalue=0,
                command=lambda: [mv15.set(2)]).grid(row=73, sticky=W, ipadx=60)
    Radiobutton(f, text="Class functions", font='calibri', variable=mv15, value=3, tristatevalue=0,
                command=lambda: [mv15.set(3)]).grid(row=74, sticky=W, ipadx=60, )
    Radiobutton(f, text="Both A and B", font='calibri', variable=mv15, value=4, tristatevalue=0,
                command=lambda: [mv15.set(4)]).grid(row=75, sticky=W, ipadx=60)

    def score():

        sdata = []
        score = 0
        mv = ["mv", mv1, mv2, mv3, mv4, mv5, mv6, mv7, mv8, mv9, mv10, mv11, mv12, mv13, mv14, mv15]
        ans = ["mv", 2, 3, 4, 4, 3, 3, 4, 1, 3, 3, 1, 4, 3, 1, 2]
        for i in range(1, 15):
            if i > 0:
                v = mv[i].get()
                if v == ans[i]:
                    score += 1
                mv1.set(0)
        messagebox.showinfo("score", "score: " + str(score))
        w.destroy()

    b1 = Button(c, text="Submit", font='calibri', command=score).place(x=800, y=50)

    c.create_window(0, 0, anchor='nw', window=f)
    c.update_idletasks()
    c.configure(scrollregion=c.bbox('all'), yscrollcommand=sc.set)
    c.pack(fill='both', expand=True, side='left')

    w.after(1, countdown)
    w.mainloop()


# # C()
def python():
    def countdown():
        global run, s, m
        if s < 10:
            s = "0" + str(s)
        # Delete old text
        c.delete('cl1')
        # Add new text
        cl1 = Label(c, anchor=CENTER, text="Timer : %s:%s" % (m, s), font=("calibri")).place(x=760, y=16)
        s = int(s)
        if s <= 0:
            s = 59
            m -= 1
        elif s > 0:
            s -= 1
        if str(m) + str(s) == "0500":
            messagebox.showinfo("message", "Only 5 minutes remaining.")
        if str(m) + str(s) == "0000":
            submit()
            messagebox.showinfo("message", "Your answers submitted successfully")

        # After 1 second, call Run again (start an infinite recursive loop)
        w.after(1000, countdown)

    w = Tk()
    w.title("Python")
    w.geometry("900x700")
    c = Canvas(w, height=500, width=500)
    sc = Scrollbar(w, orient="vertical", command=c.yview)
    sc.pack(side='right', fill='y')
    f = Frame(c)

    hl = Label(f, text="Python MCQ(Multiple Choice Questions)", font=("calibri", 25)).grid(row=0, sticky=W, ipadx=60)

    mv1 = IntVar()
    Label(f, text="1) what is the maximum possible length of an identifier ? ", font="calibri").grid(row=1, sticky=W,
                                                                                                     ipadx=20, ipady=10)
    Radiobutton(f, text="  16", font='calibri', variable=mv1, value=1, tristatevalue=0,
                command=lambda: [mv1.set(1)]).grid(row=2, sticky=W, ipadx=60)
    Radiobutton(f, text="  32", font='calibri', variable=mv1, value=2, tristatevalue=0,
                command=lambda: [mv1.set(2)]).grid(row=3, sticky=W, ipadx=60)
    Radiobutton(f, text="  64", font='calibri', variable=mv1, value=3, tristatevalue=0,
                command=lambda: [mv1.set(3)]).grid(row=4, sticky=W, ipadx=60)
    Radiobutton(f, text="  None of the Above.", font='calibri', variable=mv1, value=4, tristatevalue=0,
                command=lambda: [mv1.set(4)]).grid(row=5, sticky=W, ipadx=60)

    mv2 = IntVar()
    Label(f, text="2) Who developed the Python language? ", font="calibri").grid(row=6, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="  Akshay", font='calibri', variable=mv2, value=1, tristatevalue=0,
                command=lambda: [mv2.set(1)]).grid(row=7, sticky=W, ipadx=60)
    Radiobutton(f, text="  Guido Van Rossum.", font='calibri', variable=mv2, value=2, tristatevalue=0,
                command=lambda: [mv2.set(2)]).grid(row=8, sticky=W, ipadx=60)
    Radiobutton(f, text="  Harshal", font='calibri', variable=mv2, value=3, tristatevalue=0,
                command=lambda: [mv2.set(3)]).grid(row=9, sticky=W, ipadx=60)
    Radiobutton(f, text="  Inder", font='calibri', variable=mv2, value=4, tristatevalue=0,
                command=lambda: [mv2.set(4)]).grid(row=10, sticky=W, ipadx=60)

    mv3 = IntVar()
    Label(f, text="3) Who developed the Python language? ", font="calibri").grid(row=11, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="  1995", font='calibri', variable=mv3, value=1, tristatevalue=0,
                command=lambda: [mv3.set(1)]).grid(row=12, sticky=W, ipadx=60)
    Radiobutton(f, text="  1972", font='calibri', variable=mv3, value=2, tristatevalue=0,
                command=lambda: [mv3.set(2)]).grid(row=13, sticky=W, ipadx=60)
    Radiobutton(f, text="  1981", font='calibri', variable=mv3, value=3, tristatevalue=0,
                command=lambda: [mv3.set(3)]).grid(row=14, sticky=W, ipadx=60)
    Radiobutton(f, text="  1989.", font='calibri', variable=mv3, value=4, tristatevalue=0,
                command=lambda: [mv3.set(4)]).grid(row=15, sticky=W, ipadx=60)

    mv4 = IntVar()
    Label(f, text="4) In which language is Python written?", font="calibri").grid(row=16, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="English", font='calibri', variable=mv4, value=1, tristatevalue=0,
                command=lambda: [mv4.set(1)]).grid(row=17, sticky=W, ipadx=60)
    Radiobutton(f, text="PHP", font='calibri', variable=mv4, value=2, tristatevalue=0,
                command=lambda: [mv4.set(2)]).grid(row=18, sticky=W, ipadx=60)
    Radiobutton(f, text="C.", font='calibri', variable=mv4, value=3, tristatevalue=0,
                command=lambda: [mv4.set(3)]).grid(row=19, sticky=W, ipadx=60)
    Radiobutton(f, text="All of the Above", font='calibri', variable=mv4, value=4, tristatevalue=0,
                command=lambda: [mv4.set(4)]).grid(row=20, sticky=W, ipadx=60)

    mv5 = IntVar()
    Label(f, text="5) Which one of the following is the correct extension of the Python file?", font="calibri").grid(
        row=21, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text=".p", font='calibri', variable=mv5, value=1, tristatevalue=0,
                command=lambda: [mv5.set(1)]).grid(row=22, sticky=W, ipadx=60)
    Radiobutton(f, text=".py.", font='calibri', variable=mv5, value=2, tristatevalue=0,
                command=lambda: [mv5.set(2)]).grid(row=23, sticky=W, ipadx=60)
    Radiobutton(f, text=".python", font='calibri', variable=mv5, value=3, tristatevalue=0,
                command=lambda: [mv5.set(3)]).grid(row=24, sticky=W, ipadx=60)
    Radiobutton(f, text="None of the Above", font='calibri', variable=mv5, value=4, tristatevalue=0,
                command=lambda: [mv5.set(4)]).grid(row=25, sticky=W, ipadx=60)

    mv6 = IntVar()
    Label(f, text="6) In which year was the Python 3.0 version developed?", font="calibri").grid(row=26, sticky=W,
                                                                                                 ipadx=20, ipady=10)
    Radiobutton(f, text="  2008.", font='calibri', variable=mv6, value=1, tristatevalue=0,
                command=lambda: [mv6.set(1)]).grid(row=27, sticky=W, ipadx=60)
    Radiobutton(f, text="  2000", font='calibri', variable=mv6, value=2, tristatevalue=0,
                command=lambda: [mv6.set(2)]).grid(row=28, sticky=W, ipadx=60)
    Radiobutton(f, text="  2010", font='calibri', variable=mv6, value=3, tristatevalue=0,
                command=lambda: [mv6.set(3)]).grid(row=29, sticky=W, ipadx=60)
    Radiobutton(f, text="  2005", font='calibri', variable=mv6, value=4, tristatevalue=0,
                command=lambda: [mv6.set(4)]).grid(row=30, sticky=W, ipadx=60)

    mv7 = IntVar()
    Label(f, text="7) What do we use to define a block of code in Python language?", font="calibri").grid(row=31,
                                                                                                          sticky=W,
                                                                                                          ipadx=20,
                                                                                                          ipady=10)
    Radiobutton(f, text="  Key", font='calibri', variable=mv7, value=1, tristatevalue=0,
                command=lambda: [mv7.set(1)]).grid(row=32, sticky=W, ipadx=60)
    Radiobutton(f, text="  Indentations.", font='calibri', variable=mv7, value=2, tristatevalue=0,
                command=lambda: [mv7.set(2)]).grid(row=33, sticky=W, ipadx=60)
    Radiobutton(f, text="  Brackets.", font='calibri', variable=mv7, value=3, tristatevalue=0,
                command=lambda: [mv7.set(3)]).grid(row=34, sticky=W, ipadx=60)
    Radiobutton(f, text="  None of the above", font='calibri', variable=mv7, value=4, tristatevalue=0,
                command=lambda: [mv7.set(4)]).grid(row=35, sticky=W, ipadx=60)

    mv8 = IntVar()
    Label(f, text="8) Which character is used in Python to make a single line comment ? ", font="calibri").grid(row=36,
                                                                                                                sticky=W,
                                                                                                                ipadx=20,
                                                                                                                ipady=10)
    Radiobutton(f, text="  /", font='calibri', variable=mv8, value=1, tristatevalue=0,
                command=lambda: [mv8.set(1)]).grid(row=37, sticky=W, ipadx=60)
    Radiobutton(f, text="  //", font='calibri', variable=mv8, value=2, tristatevalue=0,
                command=lambda: [mv8.set(2)]).grid(row=38, sticky=W, ipadx=60)
    Radiobutton(f, text="  #.", font='calibri', variable=mv8, value=3, tristatevalue=0,
                command=lambda: [mv8.set(3)]).grid(row=39, sticky=W, ipadx=60)
    Radiobutton(f, text="  !", font='calibri', variable=mv8, value=4, tristatevalue=0,
                command=lambda: [mv8.set(4)]).grid(row=40, sticky=W, ipadx=60)

    mv9 = IntVar()
    Label(f, text="9) Operators with the same precedence are evaluated in which manner? ", font="calibri").grid(row=41,
                                                                                                                sticky=W,
                                                                                                                ipadx=20,
                                                                                                                ipady=10)
    Radiobutton(f, text="Left to Right.", font='calibri', variable=mv9, value=1, tristatevalue=0,
                command=lambda: [mv9.set(1)]).grid(row=42, sticky=W, ipadx=60)
    Radiobutton(f, text="Right to Left", font='calibri', variable=mv9, value=2, tristatevalue=0,
                command=lambda: [mv9.set(2)]).grid(row=43, sticky=W, ipadx=60)
    Radiobutton(f, text="Can't say", font='calibri', variable=mv9, value=3, tristatevalue=0,
                command=lambda: [mv9.set(3)]).grid(row=44, sticky=W, ipadx=60)
    Radiobutton(f, text="None of the Above", font='calibri', variable=mv9, value=4, tristatevalue=0,
                command=lambda: [mv9.set(4)]).grid(row=45, sticky=W, ipadx=60)

    mv10 = IntVar()
    Label(f, text="10) What is the method inside the class in python language?", font="calibri").grid(row=46, sticky=W,
                                                                                                      ipadx=20,
                                                                                                      ipady=10)
    Radiobutton(f, text="Object", font='calibri', variable=mv10, value=1, tristatevalue=0,
                command=lambda: [mv10.set(1)]).grid(row=47, sticky=W, ipadx=60)
    Radiobutton(f, text="Function.", font='calibri', variable=mv10, value=2, tristatevalue=0,
                command=lambda: [mv10.set(2)]).grid(row=48, sticky=W, ipadx=60)
    Radiobutton(f, text="Attribute", font='calibri', variable=mv10, value=3, tristatevalue=0,
                command=lambda: [mv10.set(3)]).grid(row=49, sticky=W, ipadx=60)
    Radiobutton(f, text="Argument", font='calibri', variable=mv10, value=4, tristatevalue=0,
                command=lambda: [mv10.set(4)]).grid(row=50, sticky=W, ipadx=60)

    mv11 = IntVar()

    Label(f, text="11) Which of the following declarations is incorrect? ", font="calibri").grid(row=51, sticky=W,
                                                                                                 ipadx=20, ipady=10)
    Radiobutton(f, text="  _x = 2", font='calibri', variable=mv11, value=1, tristatevalue=0,
                command=lambda: [mv11.set(1)]).grid(row=52, sticky=W, ipadx=60)
    Radiobutton(f, text="  __x = 3", font='calibri', variable=mv11, value=2, tristatevalue=0,
                command=lambda: [mv11.set(2)]).grid(row=53, sticky=W, ipadx=60)
    Radiobutton(f, text="  __xyz__ = 5", font='calibri', variable=mv11, value=3, tristatevalue=0,
                command=lambda: [mv11.set(3)]).grid(row=54, sticky=W, ipadx=60)
    Radiobutton(f, text="  None of the Above.", font='calibri', variable=mv11, value=4, tristatevalue=0,
                command=lambda: [mv11.set(4)]).grid(row=55, sticky=W, ipadx=60)

    mv12 = IntVar()
    Label(f, text="12) What is the output of this expression, 3*1**3? ", font="calibri").grid(row=56, sticky=W,
                                                                                              ipadx=20, ipady=10)
    Radiobutton(f, text="  27", font='calibri', variable=mv12, value=1, tristatevalue=0,
                command=lambda: [mv12.set(1)]).grid(row=57, sticky=W, ipadx=60)
    Radiobutton(f, text="  9", font='calibri', variable=mv12, value=2, tristatevalue=0,
                command=lambda: [mv12.set(2)]).grid(row=58, sticky=W, ipadx=60)
    Radiobutton(f, text="  3.", font='calibri', variable=mv12, value=3, tristatevalue=0,
                command=lambda: [mv12.set(3)]).grid(row=59, sticky=W, ipadx=60)
    Radiobutton(f, text="  1", font='calibri', variable=mv12, value=4, tristatevalue=0,
                command=lambda: [mv12.set(4)]).grid(row=60, sticky=W, ipadx=60)

    mv13 = IntVar()
    Label(f, text="13) Which of the following is not a keyword in Python language? ", font="calibri").grid(row=61,
                                                                                                           sticky=W,
                                                                                                           ipadx=20,
                                                                                                           ipady=10)
    Radiobutton(f, text="  val.", font='calibri', variable=mv13, value=1, tristatevalue=0,
                command=lambda: [mv13.set(1)]).grid(row=62, sticky=W, ipadx=60)
    Radiobutton(f, text="  raise", font='calibri', variable=mv13, value=2, tristatevalue=0,
                command=lambda: [mv13.set(2)]).grid(row=63, sticky=W, ipadx=60)
    Radiobutton(f, text="  try", font='calibri', variable=mv13, value=3, tristatevalue=0,
                command=lambda: [mv13.set(3)]).grid(row=64, sticky=W, ipadx=60)
    Radiobutton(f, text="  with", font='calibri', variable=mv13, value=4, tristatevalue=0,
                command=lambda: [mv13.set(4)]).grid(row=65, sticky=W, ipadx=60)

    mv14 = IntVar()
    Label(f, text="14) Which one of the following has the highest precedence in the expression?", font="calibri").grid(
        row=66, sticky=W, ipadx=20, ipady=10)
    Radiobutton(f, text="Division", font='calibri', variable=mv14, value=1, tristatevalue=0,
                command=lambda: [mv14.set(1)]).grid(row=67, sticky=W, ipadx=60)
    Radiobutton(f, text="Substraction", font='calibri', variable=mv14, value=2, tristatevalue=0,
                command=lambda: [mv14.set(2)]).grid(row=68, sticky=W, ipadx=60)
    Radiobutton(f, text="Power", font='calibri', variable=mv14, value=3, tristatevalue=0,
                command=lambda: [mv14.set(3)]).grid(row=69, sticky=W, ipadx=60)
    Radiobutton(f, text="Parentheses.", font='calibri', variable=mv14, value=4, tristatevalue=0,
                command=lambda: [mv14.set(4)]).grid(row=70, sticky=W, ipadx=60)

    mv15 = IntVar()
    Label(f, text="15) Which is the correct operator for power(xy)?", font="calibri").grid(row=71, sticky=W, ipadx=20,
                                                                                           ipady=10)
    Radiobutton(f, text="X^y", font='calibri', variable=mv15, value=1, tristatevalue=0,
                command=lambda: [mv15.set(1)]).grid(row=72, sticky=W, ipadx=60)
    Radiobutton(f, text="X**y.", font='calibri', variable=mv15, value=2, tristatevalue=0,
                command=lambda: [mv15.set(2)]).grid(row=73, sticky=W, ipadx=60)
    Radiobutton(f, text="X^^y", font='calibri', variable=mv15, value=3, tristatevalue=0,
                command=lambda: [mv15.set(3)]).grid(row=74, sticky=W, ipadx=60)
    Radiobutton(f, text="None of the Above", font='calibri', variable=mv15, value=4, tristatevalue=0,
                command=lambda: [mv15.set(4)]).grid(row=75, sticky=W, ipadx=60)

    def score():

        sdata = []
        score = 0
        mv = ["mv", mv1, mv2, mv3, mv4, mv5, mv6, mv7, mv8, mv9, mv10, mv11, mv12, mv13, mv14, mv15]
        ans = ["mv", 4, 2, 4, 3, 2, 1, 2, 3, 1, 2, 4, 3, 1, 4, 2]
        for i in range(1, 15):
            if i > 0:
                v = mv[i].get()
                if v == ans[i]:
                    score += 1
                mv1.set(0)
        messagebox.showinfo("score", "score: " + str(score))
        w.destroy()

    b1 = Button(c, text="Submit", font='calibri',command=score).place(x=800, y=50)

    c.create_window(0, 0, anchor='nw', window=f)
    c.update_idletasks()
    c.configure(scrollregion=c.bbox('all'), yscrollcommand=sc.set)
    c.pack(fill='both', expand=True, side='left')

    w.after(1, countdown)
    w.mainloop()

# python()

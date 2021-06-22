from tabulate import tabulate
import mysql.connector as m
conn=m.connect(user='root',password='root',host='localhost')
cur=conn.cursor()

class db:
    def dbtb(self):
        global tname
        q2 = "show tables"
        cur.execute(q2)
        a = cur.fetchall()
        header1 = []
        for i in cur.description:
            header1.append(i[0])
        print(tabulate(a, header1, tablefmt="psql"))
        op2 = input("create|use table:")
        tname = input("enter name of table:")
        if op2 == "create":
            a = input("enter column names with datatype:")
            q = ("create table " + tname + "(" + a + ")")
            cur.execute(q)
            q2 = "show tables"
            cur.execute(q2)
            a = cur.fetchall()
            header1 = []
            for i in cur.description:
                header1.append(i[0])
            print(tabulate(a, header1, tablefmt="psql"))
        elif op2 == "use":
            q = "select * from " + tname
            cur.execute(q)
            a = cur.fetchall()
            header = []
            for i in cur.description:
                header.append(i[0])
            print(tabulate(a, header, tablefmt="psql"))
        else:
            print("plz enter valid operation!")

    def dbop(self):
        try:
            # database creation and use
            q1 = "show databases"
            cur.execute(q1)
            b = cur.fetchall()
            header = []
            for i in cur.description:
                header.append(i[0])
            print(tabulate(b,header,tablefmt="psql"))
            op1 = input("use|create database:")

            if op1 == "create":
                name = input("enter name of db u want to create:")
                q = ("create database " + name)
                q1 = ("use " + name)
                cur.execute(q)
                cur.execute(q1)
                conn.commit()
            elif op1 == "use":
                name = input("enter name of db u want to use:")
                q = ("use " + name)
                cur.execute(q)
                conn.commit()
            else:
                print("plz enter valid operation!")

            # table creation and use
            db.dbtb(self)

            x=0
            while x==0:
                op=input("enter operation name(add|update|delete|view|switch db|switch table|close):")

                # view data
                if op=="view":
                    q="select * from "+tname
                    cur.execute(q)
                    r = cur.fetchall()
                    header = []
                    for i in cur.description:
                        header.append(i[0])
                    print(tabulate(r, header, tablefmt="psql"))

                #data insertion
                elif op=="add":
                    q="insert into "+tname+" (id,name,salary) values(%s,%s,%s)"
                    v=[]
                    for i in range(int(input("no of inputs:"))):
                        a=[]
                        id=int(input("id:"))
                        a.append(id)
                        name=input("name:")
                        a.append(name)
                        salary=int(input("salary:"))
                        a.append(salary)
                        a=tuple(a)
                        v.append(a)
                        print()
                    cur.executemany(q, v)


                # data update
                elif op=="update":
                    a=input("which column u want to update:")
                    if a=="name":
                        s = input("name:")
                        id = int(input("id:"))
                        v = (s, id)
                        q = ("update "+tname+" set name=%s where id=%s")
                        cur.execute(q, v)
                        q1 = "select * from " + tname
                        cur.execute(q1)
                        b = cur.fetchall()
                        for i in b:
                            print(*i, sep="\t")
                    if a=="salary":
                        s=int(input("salary:"))
                        id=int(input("id:"))
                        v=(s,id)
                        q=("update "+tname+" set salary=%s where id=%s")
                        cur.execute(q, v)

                # data deletion
                elif op=="delete":
                    a = input("how much u want to delete(one|all):")
                    if a == "all":
                        q = ("delete from "+tname)
                        cur.execute(q)

                    if a=="one":
                        name=input("name:")
                        id=int(input("id:"))
                        v=(name,id)
                        q = ("delete from "+tname+" where name=%s and id=%s")
                        cur.execute(q,v)

                #switching database program
                elif op=="switch db":
                    db.dbop(self)

                elif op=="switch table":
                    db.dbtb(self)

                #close
                elif op=="close":
                    break

                else:
                    print("plz enter valid operation!")
        except ValueError:
            print("plz enter correct datatype")
        except:
            print("Unexpected error:")
            raise
        finally:
            conn.commit()

obj=db()
obj.dbop()
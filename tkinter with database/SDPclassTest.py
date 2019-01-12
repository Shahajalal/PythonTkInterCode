from tkinter import *
import MySQLdb
import tkinter.messagebox
#**********Work For calculator***********
first = None
second = None
operator = ""
class calculator:
    def __init__(self,win):
        self.win = win
        frame = Frame(self.win)
        frame.pack()
        self.win.title("Calculator")
        var = StringVar()
        def funpo():
            s = text.get()
            var.set(s + ".")

        def funce():
            s = text.get()
            s1 = len(s)
            s2 = s[:s1 - 1]
            var.set(s2)

        def fun1():
            s = text.get()
            var.set(s + "1")

        def fun2():
            s = text.get()
            var.set(s + "2")

        def fun3():
            s = text.get()
            var.set(s + "3")

        def fun4():
            s = text.get()
            var.set(s + "4")

        def fun5():
            s = text.get()
            var.set(s + "5")

        def fun6():
            s = text.get()
            var.set(s + "6")

        def fun7():
            s = text.get()
            var.set(s + "7")

        def fun8():
            s = text.get()
            var.set(s + "8")

        def fun9():
            s = text.get()
            var.set(s + "9")

        def fun0():
            s = text.get()
            var.set(s + "0")

        def funp():
            global first
            first = float(text.get())
            var.set("")
            global operator
            operator = "+"

        def funm():
            global first
            first = float(text.get())
            var.set("")
            global operator
            operator = "-"

        def fung():
            global first
            first = float(text.get())
            var.set("")
            global operator
            operator = "*"

        def fund():
            global first
            first = float(text.get())
            var.set("")
            global operator
            operator = "/"

        def fune():
            second = float(text.get())
            global first
            if (operator == "+"):
                result = first + second
                result1 = str(result)
                index = result1.find(".")
                if (result1[index + 1:] == "0"):
                    var.set(result1[:index])
                else:
                    var.set(result1)
            elif (operator == "-"):
                result = first - second
                result1 = str(result)
                index = result1.find(".")
                if (result1[index + 1:] == "0"):
                    var.set(result1[:index])
                else:
                    var.set(result1)
            elif (operator == "*"):
                result = first * second
                result1 = str(result)
                index = result1.find(".")
                if (result1[index + 1:] == "0"):
                    var.set(result1[:index])
                else:
                    var.set(result1)
            else:
                result = first / second
                result1 = str(result)
                index = result1.find(".")
                if (result1[index + 1:] == "0"):
                    var.set(result1[:index])
                else:
                    var.set(result1)

        def func():
            var.set("")

        text = Entry(frame, textvariable=var, justify="right", bd=20, insertwidth=2, font=30)
        text.pack(side=TOP)
        b1 = Button(frame, text="1", fg="blue", bg="white", bd=8, padx=20, pady=15, command=fun1)
        b1.pack(side=LEFT)
        b2 = Button(frame, text="2", fg="blue", bg="white", bd=8, padx=20, pady=15, command=fun2)
        b2.pack(side=LEFT)
        b3 = Button(frame, text="3", fg="blue", bg="white", bd=8, padx=20, pady=15, command=fun3)
        b3.pack(side=LEFT)
        b4 = Button(frame, text="4", fg="blue", bg="white", bd=8, padx=20, pady=15, command=fun4)
        b4.pack(side=LEFT)

        frame1 = Frame(self.win)
        frame1.pack(side=TOP)
        b5 = Button(frame1, text="5", fg="blue", bg="white", bd=8, padx=20, pady=15, command=fun5)
        b5.pack(side=LEFT)
        b6 = Button(frame1, text="6", fg="blue", bg="white", bd=8, padx=20, pady=15, command=fun6)
        b6.pack(side=LEFT)
        b7 = Button(frame1, text="7", fg="blue", bg="white", bd=8, padx=20, pady=15, command=fun7)
        b7.pack(side=LEFT)
        b8 = Button(frame1, text="8", fg="blue", bg="white", bd=8, padx=20, pady=15, command=fun8)
        b8.pack(side=LEFT)

        frame2 = Frame(self.win)
        frame2.pack(side=TOP)
        b9 = Button(frame2, text="9", fg="blue", bg="white", bd=8, padx=20, pady=15, command=fun9)
        b9.pack(side=LEFT)
        b0 = Button(frame2, text="0", fg="blue", bg="white", bd=8, padx=20, pady=15, command=fun0)
        b0.pack(side=LEFT)
        bp = Button(frame2, text="+", fg="blue", bg="white", bd=8, padx=20, pady=15, command=funp)
        bp.pack(side=LEFT)
        bm = Button(frame2, text="-", fg="blue", bg="white", bd=8, padx=20, pady=15, command=funm)
        bm.pack(side=LEFT)

        frame3 = Frame(self.win)
        frame3.pack(side=TOP)
        bg = Button(frame3, text="*", fg="blue", bg="white", bd=8, padx=20, pady=15, command=fung)
        bg.pack(side=LEFT)
        bd = Button(frame3, text="/", fg="blue", bg="white", bd=8, padx=20, pady=15, command=fund)
        bd.pack(side=LEFT)
        be = Button(frame3, text="=", fg="blue", bg="white", bd=8, padx=20, pady=15, command=fune)
        be.pack(side=LEFT)
        bc = Button(frame3, text="C", fg="blue", bg="white", bd=8, padx=20, pady=15, command=func)
        bc.pack(side=LEFT)

        frame4 = Frame(self.win)
        frame4.pack(side=TOP)
        bpo = Button(frame4, text=".", fg="blue", bg="white", bd=8, padx=50, pady=15, command=funpo)
        bpo.pack(side=LEFT)
        bce = Button(frame4, text="CE", fg="blue", bg="white", bd=8, padx=50, pady=15, command=funce)
        bce.pack(side=LEFT)
#******************Work For Calculator**********************

#*******Show**************
class show:
    def __init__(self,win):
        self.win=win
        self.win.geometry("500x400")
        self.win.title("Data Selection")
        t1 = Text(self.win, width=80, height=20)

        def showinfo():
            db = MySQLdb.connect("localhost", "root", "s1hahajalal", "school")
            c = db.cursor()
            sql = "select * from student"
            c.execute(sql)
            row = c.fetchone()
            while row is not None:
                t1.insert(END, str(row) + '\n')
                row = c.fetchone()

            db.close()

        t1.pack()
        b1 = Button(self.win, text="Show Data", command=showinfo,fg="red",bg="white")

        b1.pack()
#*******End show*********


#******** Insert*******
class insert:
    def __init__(self,win):
        self.win =win
        self.win.geometry("280x150")
        self.win.title("Insert data from user")

        labelid = Label(self.win, text="Id", anchor=E)
        entryid = Entry(self.win, width=30)

        labelname = Label(self.win, text="Name", anchor=E)
        entryname = Entry(self.win, width=30)

        labeladdress = Label(self.win, text="Section", anchor=E)
        entryaddress = Entry(self.win, width=30)

        def showinfo():
            if entryid.get() == "":
                tkinter.messagebox.showwarning("Entry Restriction", "Please enter ID")
            else:
                id = int(entryid.get())
                name = entryname.get()
                address = entryaddress.get()

                db = MySQLdb.connect("localhost", "root", "s1hahajalal", "school")
                cursor = db.cursor()
                s = "insert into student values('%d','%s','%s')" % (id, name, address)
                try:
                    cursor.execute(s)
                    db.commit()
                    tkinter.messagebox.showinfo("Success", "Your data is inserted successfully")
                except:
                    db.rollback()
                    tkinter.messagebox.showwarning("Unsucess", "Your data is not inserted successfully")
                db.close()

        b1 = Button(self.win, text="Insert Data", command=showinfo)

        spacelabel = Label(self.win)

        labelid.grid(row="0")
        entryid.grid(row="0", column="1")

        labelname.grid(row="1")
        entryname.grid(row="1", column="1")

        labeladdress.grid(row="2")
        entryaddress.grid(row="2", column="1")

        spacelabel.grid(row="4")

        b1.grid(row="5", column="1")


#*********End of insert*********

#***********Delete**********
class delete:
    def __init__(self,win):
        self.win = win
        win.geometry("280x150")
        win.title("Delete data")

        labelid = Label(win, text="Id", anchor=E)
        entryid = Entry(win, width=30)

        def showinfo():
            if entryid.get() == "":
                tkinter.messagebox.showwarning("Entry Restriction", "Please enter ID")
            else:
                id = int(entryid.get())
                db = MySQLdb.connect("localhost", "root", "s1hahajalal", "school")
                cursor = db.cursor()
                s = "delete from student where id=('%d')" % (id)
                check = cursor.execute(s)
                if check > 0:
                    db.commit()
                    tkinter.messagebox.showinfo("Sucessfull", "Data deleted successfully")
                else:
                    db.rollback()
                    tkinter.messagebox.showwarning("Uncessfull", "Data is not deleted")

                db.close()

        b1 = Button(win, text="Delete Data", command=showinfo)

        spacelabel = Label(win)

        labelid.grid(row="0")
        entryid.grid(row="0", column="1")

        spacelabel.grid(row="1")

        b1.grid(row="2", column="1")

#**********End of DELETE********

#**********Search*********
class search:
    def __init__(self,win):
        self.win = win
        win.geometry("280x150")
        win.title("Search data")

        labelid = Label(win, text="Id", anchor=E)
        entryid = Entry(win, width=30)

        def showinfo():
            if entryid.get() == "":
                tkinter.messagebox.showwarning("Entry Restriction", "Please enter ID")
            else:
                id = int(entryid.get())
                db = MySQLdb.connect("localhost", "root", "s1hahajalal", "school")
                cursor = db.cursor()
                s = "select * from student where id=('%d')" % (id)
                check = cursor.execute(s)
                if check > 0:
                    row = cursor.fetchone()
                    r2 = Tk()
                    r2.title("Data Found")
                    r2.geometry("300x300")
                    t1 = Text(r2, width=40, height=30)
                    t1.insert(END, row)
                    t1.pack()
                    r2.mainloop()
                else:
                    tkinter.messagebox.showwarning("Not Found", "Search data is not found")

                db.close()

        b1 = Button(win, text="Search Data", command=showinfo)

        spacelabel = Label(win)

        labelid.grid(row="0")
        entryid.grid(row="0", column="1")

        spacelabel.grid(row="1")

        b1.grid(row="2", column="1")


#*********END of SEARCH*******

#*********UPdate*******
class update:
    def __init__(self,win):
        root = win
        root.geometry("300x300")

        def insert():
            db = MySQLdb.connect("localhost", "root", "s1hahajalal", "school")
            c = db.cursor()
            if (identry.get() == ""):
                tkinter.messagebox.showinfo("warning", "Please inser id then press insert button")
            else:
                try:
                    id = int(identry.get())
                    name = nameentry.get()
                    department = departmententry.get()
                    sql = "update student set name=('%s'),section=('%s') where id=('%d')" % (name, department, id)
                    c.execute(sql)
                    db.commit()
                    tkinter.messagebox.showinfo("successful", "successful")
                except:
                    db.rollback()
                    tkinter.messagebox.showinfo("unsuccessful", "unsuccessful")
            db.close()

        idlabel = Label(root, text="ID")
        idlabel.grid(row=0)
        identry = Entry(root)
        identry.grid(row=0, column=1)
        namelabel = Label(root, text="Name")
        namelabel.grid(row=1)
        nameentry = Entry(root)
        nameentry.grid(row=1, column=1)
        departmentlabel = Label(root, text="Department")
        departmentlabel.grid(row=2)
        departmententry = Entry(root)
        departmententry.grid(row=2, column=1)
        button = Button(root, text="Update", command=insert)
        button.grid(row=5, column=1)

#********END of update*****
root=Tk()
root.geometry("300x300")
root.title("Calculator + Database")
root.configure(background="white")
#root.configure(background='blue')
def insert1():
    root1 = Toplevel(root)
    b = insert(root1)
def update1():
    root1 = Toplevel(root)
    b = update(root1)
def search1():
    root1 = Toplevel(root)
    b = search(root1)
def delete1():
    root1 = Toplevel(root)
    b = delete(root1)
def show1():
    root1=Toplevel(root)
    b=show(root1)
def cal():
    #***TopLavel is the most Importent thing***
    root1=Toplevel(root)
    b=calculator(root1)
frame1=Frame(root)
frame1.pack(side=TOP)
label1=Label(frame1,text="Please go to menu to see the database operation ",fg="blue",bg="white")
label1.grid(row=0)
label4=Label(frame1)
label4.grid(row=1)
frame2=Frame(root)
frame2.pack(side=TOP)
label2=Label(frame2,text="Please Enter the Calculator Button to see the Calculator ")
label5=Label(frame2)
label5.grid(row=3)
label2.grid(row=2)
frame3=Frame(root)
frame3.pack(side=TOP)
button=Button(frame3,text="Calculator",command=cal,fg="red",bg="white")
button.grid(row=4)
#*******Menu Work*******
m1=Menu(root)
root.config(menu=m1)
submenu=Menu(m1)
m1.add_cascade(label="Database operation",menu=submenu)
submenu.add_command(label="Show",command=show1)
submenu.add_separator()
submenu.add_command(label="Insert",command=insert1)
submenu.add_separator()
submenu.add_command(label="Delete",command=delete1)
submenu.add_separator()
submenu.add_command(label="Search",command=search1)
submenu.add_separator()
submenu.add_command(label="Update",command=update1)
root.mainloop()


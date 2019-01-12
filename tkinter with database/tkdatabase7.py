import MySQLdb
from tkinter import *
import tkinter.messagebox

win = Tk()
win.geometry("280x150")
win.title("Search data")

labelid = Label(win, text = "Id", anchor =E)
entryid = Entry(win, width = 30)


def showinfo():
    if entryid.get() == "":
        tkinter.messagebox.showwarning("Entry Restriction","Please enter ID")
    else:
        id = int(entryid.get())
        db = MySQLdb.connect("localhost","root","s1hahajalal","school")
        cursor = db.cursor()
        s = "select * from student where id=('%d')" % (id)
        check = cursor.execute(s)
        if check>0:
           row =cursor.fetchone()
           r2 = Tk()
           r2.title("Data Found")
           r2.geometry("300x300")
           t1 = Text(r2, width = 40, height = 30)
           t1.insert(END, row)
           t1.pack()
           r2.mainloop()
        else:
            tkinter.messagebox.showwarning("Not Found", "Search data is not found")

        db.close()

b1 = Button(win, text ="Search Data", command = showinfo)

spacelabel =Label(win)

labelid.grid(row = "0")
entryid.grid(row ="0", column = "1")

spacelabel.grid(row ="1")

b1.grid(row ="2", column = "1")
win.mainloop()

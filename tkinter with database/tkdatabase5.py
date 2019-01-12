import MySQLdb
from tkinter import *
import tkinter.messagebox

win = Tk()
win.geometry("280x150")
win.title("Insert data from user")

labelid = Label(win, text = "Id", anchor =E)
entryid = Entry(win, width = 30)

labelname = Label(win, text = "Name", anchor =E)
entryname = Entry(win, width = 30)

labeladdress = Label(win, text = "Section", anchor =E)
entryaddress = Entry(win, width = 30)


def showinfo():
    if entryid.get() == "":
        tkinter.messagebox.showwarning("Entry Restriction","Please enter ID")
    else:
        id = int(entryid.get())
        name = entryname.get()
        address = entryaddress.get()

        db = MySQLdb.connect("localhost","root","s1hahajalal","school")
        cursor = db.cursor()
        s = "insert into student values('%d','%s','%s')" % (id,name,address)
        try:
            cursor.execute(s)
            db.commit()
            tkinter.messagebox.showinfo("Success","Your data is inserted successfully")
        except:
            db.rollback()
            tkinter.messagebox.showwarning("Unsucess","Your data is not inserted successfully")
        db.close()

b1 = Button(win, text ="Insert Data", command = showinfo)

spacelabel =Label(win)

labelid.grid(row = "0")
entryid.grid(row ="0", column = "1")

labelname.grid(row = "1")
entryname.grid(row ="1", column = "1")

labeladdress.grid(row = "2")
entryaddress.grid(row ="2", column = "1")


spacelabel.grid(row ="4")

b1.grid(row ="5", column = "1")
win.mainloop()

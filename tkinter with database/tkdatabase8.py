import MySQLdb
from tkinter import *
import tkinter.messagebox

win = Tk()
win.geometry("280x150")
win.title("Delete data")

labelid = Label(win, text = "Id", anchor =E)
entryid = Entry(win, width = 30)


def showinfo():
    if entryid.get() == "":
        tkinter.messagebox.showwarning("Entry Restriction","Please enter ID")
    else:
        id = int(entryid.get())
        db = MySQLdb.connect("localhost","root","s1hahajalal","school")
        cursor = db.cursor()
        s = "delete from student where id=('%d')" % (id)
        check = cursor.execute(s)
        if check>0:
           db.commit()
           tkinter.messagebox.showinfo("Sucessfull", "Data deleted successfully")
        else:
            db.rollback()
            tkinter.messagebox.showwarning("Uncessfull", "Data is not deleted")

        db.close()

b1 = Button(win, text ="Delete Data", command = showinfo)

spacelabel =Label(win)

labelid.grid(row = "0")
entryid.grid(row ="0", column = "1")

spacelabel.grid(row ="1")

b1.grid(row ="2", column = "1")
win.mainloop()

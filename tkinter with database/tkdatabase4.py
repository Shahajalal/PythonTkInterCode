import MySQLdb
from tkinter import*
import tkinter.messagebox
win = Tk()
win.geometry("300x100")
win.title("Insert Data")

def showinfo():
    db = MySQLdb.connect("localhost","root","s1hahajalal","school")
    c = db.cursor()
    sql = "insert into student values(10,'the','CSE')"
    try:
        c.execute(sql)
        db.commit()
        tkinter.messagebox.showinfo("Success","Your data is inserted successfully")
    except:
        db.rollback()
        tkinter.messagebox.showwarning("Unsuccess", "Your data is not inserted successfully")

    db.close()

b1 = Button(win, text = "Insert Data", command = showinfo)

b1.pack()

win.mainloop()

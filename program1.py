import MySQLdb
from tkinter import *
import tkinter.messagebox

win = Tk()
win.geometry("280x150")
win.title("Insert data from user")

def showinfo():
        db = MySQLdb.connect("localhost","root","s1hahajalal","university")
        cursor = db.cursor()
        s="CREATE TABLE "+entry1.get()+"(id int PRIMARY key,Name varchar(20))";
        try:
            cursor.execute(s)
            db.commit()
            tkinter.messagebox.showinfo("Success")
        except:
            db.rollback()
            tkinter.messagebox.showwarning("Unsucess")
        db.close()
label1=Label(win,text="Table Name")
entry1=Entry(win)
b1 = Button(win, text ="Insert Data", command = showinfo)
label1.grid(row="4",column="1")
entry1.grid(row="4",column="2")
b1.grid(row ="5", column = "1")
win.mainloop()

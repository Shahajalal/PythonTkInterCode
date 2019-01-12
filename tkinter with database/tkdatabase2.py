import MySQLdb
from tkinter import*
win = Tk()
win.geometry("300x200")
win.title("Data Selection")

def showinfo():
    db = MySQLdb.connect("localhost","root","s1hahajalal","school")
    c = db.cursor()
    sql = "select * from student"
    c.execute(sql)
    row = c.fetchone()
    while row is not None:
        print(row)
        row = c.fetchone()

    db.close()

b1 = Button(win, text = "Show Data", command = showinfo)
b1.pack()

win.mainloop()

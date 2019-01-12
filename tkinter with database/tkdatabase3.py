import MySQLdb
from tkinter import*
win = Tk()
win.geometry("500x400")
win.title("Data Selection")
t1 = Text(win, width = 80, height =20)
def showinfo():
    db = MySQLdb.connect("localhost","root","s1hahajalal","school")
    c = db.cursor()
    sql = "select * from student"
    c.execute(sql)
    row = c.fetchone()
    while row is not None:
       t1.insert(END,str(row) +'\n')
       row = c.fetchone()

    db.close()
t1.pack()
b1 = Button(win, text = "Show Data", command = showinfo)

b1.pack()

win.mainloop()

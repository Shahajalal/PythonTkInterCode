from tkinter import *
import tkinter.messagebox
import MySQLdb
root=Tk()
root.geometry("300x300")
def insert():
    db=MySQLdb.connect("localhost","root","s1hahajalal","university")
    c=db.cursor()
    if(identry.get()==""):
        tkinter.messagebox.showinfo("warning","Please inser id then press insert button")
    else:
        try:
            id = int(identry.get())
            name = nameentry.get()
            department = departmententry.get()
            sql ="update student set name=('%s'),department=('%s') where id=('%d')"%(name,department,id)
            c.execute(sql)
            db.commit()
            tkinter.messagebox.showinfo("successful", "successful")
        except:
            db.rollback()
            tkinter.messagebox.showinfo("unsuccessful", "unsuccessful")
    db.close()
idlabel=Label(root,text="ID")
idlabel.grid(row=0)
identry=Entry(root)
identry.grid(row=0,column=1)
namelabel=Label(root,text="Name")
namelabel.grid(row=1)
nameentry=Entry(root)
nameentry.grid(row=1,column=1)
departmentlabel=Label(root,text="Department")
departmentlabel.grid(row=2)
departmententry=Entry(root)
departmententry.grid(row=2,column=1)
button=Button(root,text="Update",command=insert)
button.grid(row=5,column=1)
root.mainloop()
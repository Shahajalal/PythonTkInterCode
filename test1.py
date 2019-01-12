from tkinter import *
import tkinter.messagebox
win=Tk()
win.title("North western")
win.geometry("300x100")
v=StringVar()
def display():
    s=e1.get()
    v.set(s+"100")
def display1():
    s = e1.get()
    v.set(s + "200")
def display3():
    s = e1.get()
    v.set(s + "+")
def display4():
    x=e1.get()
    p=x.find("+")
    a=int(x[:p])
    b=int(x[p+1:])
    v.set(str(a+b))
e1=Entry(win,width=30,justify="right",textvariable=v)
b1=Button(win,text="100",command=display)
b2=Button(win,text="200",command=display1)
b3=Button(win,text="+",command=display3)
b4=Button(win,text="=",command=display4)
e1.grid(row="0")
b1.grid(row="1")
b2.grid(row="2")
b3.grid(row="3")
b4.grid(row="4")
win.mainloop()

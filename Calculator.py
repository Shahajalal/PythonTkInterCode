from tkinter import *
win=Tk()
frame=Frame(win)
frame.pack()
win.title("Calculator")
var=StringVar()
first=None
second=None
operator=""
def funpo():
    s = text.get()
    var.set(s + ".")
def funce():
   s=text.get()
   s1=len(s)
   s2=s[:s1-1]
   var.set(s2)

def fun1():
    s=text.get()
    var.set(s+"1")
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
    first=float(text.get())
    var.set("")
    global operator
    operator="+"
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
    second=float(text.get())
    global first
    if(operator=="+"):
        result = first + second
        result1=str(result)
        index=result1.find(".")
        if(result1[index+1:]=="0"):
            var.set(result1[:index])
        else:
            var.set(result1)
    elif(operator=="-"):
        result = first - second
        result1 = str(result)
        index = result1.find(".")
        if (result1[index + 1:] == "0"):
            var.set(result1[:index])
        else:
            var.set(result1)
    elif(operator=="*"):
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



text=Entry(frame,textvariable=var,justify="right",bd=20,insertwidth=2,font=30)
text.pack(side=TOP)
b1=Button(frame,text="1",fg="blue",bg="white",bd=8,padx=20,pady=15,command=fun1)
b1.pack(side=LEFT)
b2=Button(frame,text="2",fg="blue",bg="white",bd=8,padx=20,pady=15,command=fun2)
b2.pack(side=LEFT)
b3=Button(frame,text="3",fg="blue",bg="white",bd=8,padx=20,pady=15,command=fun3)
b3.pack(side=LEFT)
b4=Button(frame,text="4",fg="blue",bg="white",bd=8,padx=20,pady=15,command=fun4)
b4.pack(side=LEFT)

frame1=Frame(win)
frame1.pack(side=TOP)
b5=Button(frame1,text="5",fg="blue",bg="white",bd=8,padx=20,pady=15,command=fun5)
b5.pack(side=LEFT)
b6=Button(frame1,text="6",fg="blue",bg="white",bd=8,padx=20,pady=15,command=fun6)
b6.pack(side=LEFT)
b7=Button(frame1,text="7",fg="blue",bg="white",bd=8,padx=20,pady=15,command=fun7)
b7.pack(side=LEFT)
b8=Button(frame1,text="8",fg="blue",bg="white",bd=8,padx=20,pady=15,command=fun8)
b8.pack(side=LEFT)

frame2=Frame(win)
frame2.pack(side=TOP)
b9=Button(frame2,text="9",fg="blue",bg="white",bd=8,padx=20,pady=15,command=fun9)
b9.pack(side=LEFT)
b0=Button(frame2,text="0",fg="blue",bg="white",bd=8,padx=20,pady=15,command=fun0)
b0.pack(side=LEFT)
bp=Button(frame2,text="+",fg="blue",bg="white",bd=8,padx=20,pady=15,command=funp)
bp.pack(side=LEFT)
bm=Button(frame2,text="-",fg="blue",bg="white",bd=8,padx=20,pady=15,command=funm)
bm.pack(side=LEFT)

frame3=Frame(win)
frame3.pack(side=TOP)
bg=Button(frame3,text="*",fg="blue",bg="white",bd=8,padx=20,pady=15,command=fung)
bg.pack(side=LEFT)
bd=Button(frame3,text="/",fg="blue",bg="white",bd=8,padx=20,pady=15,command=fund)
bd.pack(side=LEFT)
be=Button(frame3,text="=",fg="blue",bg="white",bd=8,padx=20,pady=15,command=fune)
be.pack(side=LEFT)
bc=Button(frame3,text="C",fg="blue",bg="white",bd=8,padx=20,pady=15,command=func)
bc.pack(side=LEFT)

frame4=Frame(win)
frame4.pack(side=TOP)
bpo=Button(frame4,text=".",fg="blue",bg="white",bd=8,padx=50,pady=15,command=funpo)
bpo.pack(side=LEFT)
bce=Button(frame4,text="CE",fg="blue",bg="white",bd=8,padx=50,pady=15,command=funce)
bce.pack(side=LEFT)
win.mainloop()
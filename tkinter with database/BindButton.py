from tkinter import *
root=Tk()
def fun1(event):
    print("My Name is Shahajalal")
def fun2(event):
    print("This is another name")
button1=Button(root,text="Show my name")
button1.bind("<Button-1>",fun1)
button1.pack()
button2=Button(root,text="Print another name")
button2.bind("<Button-1>",fun2)
button2.pack()
root.mainloop()
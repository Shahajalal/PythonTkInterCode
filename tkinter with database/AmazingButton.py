from tkinter import *
root=Tk()
def fun1(event):
    print("left")
def fun2(event):
    print("MIddle")
def fun3(event):
    print("Right")
frame=Frame(root,height=300,width=200)
frame.bind("<Button-1>",fun1)
frame.bind("<Button-2>",fun2)
frame.bind("<Button-3>",fun3)
frame.pack()
root.mainloop()
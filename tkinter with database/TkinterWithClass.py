from tkinter import *
class shahajalal:
    def __init__(self,master):
        frame=Frame(master,height=100,width=50)
        frame.pack()
        self.printbutton=Button(master,text="print",command=self.printmessage)
        self.printbutton.pack()
    def printmessage(self):
        print("my name is shahajalal")

root=Tk()
def fun1():
    root1 = Tk()
    b=shahajalal(root1)
def fun2():
    root2 = Tk()
    c=shahajalal(root2)
frame=Frame(root,height=300,width=300)
button1=Button(root,text="first",command=fun1)
button1.pack()
button2=Button(root,text="second",command=fun2)
button2.pack()
root.mainloop()
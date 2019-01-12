from tkinter import *
class welcome():
    def __init__(self,master):
        self.master=master
        self.master.geometry('400x200+100+200')
        self.master.title("welcome")
        self.label1=Label(self.master,text="welcome to the wages calculator GUI",fg="red").grid(row=0,column=2)
        self.button1=Button(self.master,text="OK",fg="blue",command=self.gotowages).grid(row=6,column=2)
        self.button2=Button(self.master,text="Quit",fg="blue",command=self.finish).grid(row=6,column=3)
    def gotowages(self):
        root2=Toplevel(self.master)
        myGUI=wages(root2)
    def finish(self):
        self.master.destroy()

class wages():
    def __init__(self,master):
        self.nhours=DoubleVar()
        self
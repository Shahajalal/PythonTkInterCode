from tkinter import *
root=Tk()
one=Label(root,text="One",fg="red",bg="white")
one.pack()
two=Label(root,text="Two",fg="white",bg="red")
two.pack(fill=X)
three=Label(root,text="Three",fg="white",bg="blue")
three.pack(side=RIGHT,fill=Y)
root.mainloop()

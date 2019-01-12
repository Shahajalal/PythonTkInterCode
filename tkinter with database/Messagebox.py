from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry("100x100")
def message():
    answer=tkinter.messagebox.askquestion("question","Do You know python language?")
    if(answer=="yes"):
        print("Yes you know python")
button=Button(root,text="press to see messagebox",command=message)
button.pack()
root.mainloop()
from tkinter import *
window=Tk()
window.title("Menu Program")
window.geometry("250x100")

def donothing():
    label=Label(window,text="Something will happen")
    label.pack()

m1=Menu(window)
window.config(menu=m1)

filesubmenu=Menu(m1)
m1.add_cascade(label="File",menu=filesubmenu)

filesubmenu.add_command(label="New",command=donothing)
filesubmenu.add_command(label="show data",command=donothing())
filesubmenu.add_separator()

filesubmenu.add_command(label="Insert",command=donothing)
filesubmenu.add_command(label="Update",command=donothing)
filesubmenu.add_separator()

window.mainloop()
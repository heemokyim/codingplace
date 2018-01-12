# we'll need tkinter and sqlite3
# Python2 = Tkinter
# Python3 = tkinter

# How tkinter make GUI?
# 1. Window
# 2. Widget

# www.tkdocs.com/images/

from tkinter import *

window = Tk()
# every element goes between window=Tk() and window.mainloop()

def km_to_miles():
    miles=int(e1_value.get())*1.6
    t1.insert(END,miles)

b1 = Button(window,text="Execute",command=km_to_miles)
# b1.pack()
b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=25)
t1.grid(row=0,column=2)

window.mainloop()

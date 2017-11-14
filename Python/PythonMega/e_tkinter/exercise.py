from tkinter import *

window=Tk()

def kg_to_gram():
    kg=int(e1_value.get())
    t1.insert(END,kg*1000)
    t2.insert(END,kg*2.20462)
    t3.insert(END,kg*35.274)

b1=Button(window,text='convert',command=kg_to_gram)
b1.grid(row=0,column=2)

l1=Label(window,text='Kg')
l1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)

window.mainloop()

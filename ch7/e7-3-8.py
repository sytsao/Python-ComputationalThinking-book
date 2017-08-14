#e7-3-8簡單佈局
from tkinter import *
root =Tk()
lbl = Label(root,text= 'Hi! ')
lbl.pack()
btnl = Button( root,text = 'BUTTON1')
btnl.pack( side =LEFT)
btn2 = Button( root,text = 'BUTTON2')
btn2.pack(side = RIGHT)
root.mainloop()

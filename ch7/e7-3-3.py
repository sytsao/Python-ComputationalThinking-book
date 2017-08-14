#e7-3-3建立一個包含標籤的視窗
from tkinter import *
root = Tk()
lbl = Label (root,text = "歡迎使用GUI",width=50,height=10) 
lbl.pack()
root.mainloop( )

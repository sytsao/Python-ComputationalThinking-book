#e7-3-5建立按鈕與文字方塊實例
from tkinter import *
root= Tk()
def show():
    inputTxt=entry1.get()
    entry2.delete(0,END)
    entry2.insert(0,inputTxt)
entry1 = Entry(root,width = 30) 
entry1.pack()
btn = Button(root,text = '顯示內容',command = show)#
btn.pack()
entry2= Entry(root ,width = 30) 
entry2.pack()
root.mainloop()

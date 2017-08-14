#e7-3-4建立視窗按鈕控制項
from tkinter import *
root =Tk()
def hello( ) :
    print("Hello!")
btn = Button( root,text='點我試試! ',command = hello) 
btn.pack()
root.mainloop()

#e7-3-6用畫布繪製直線、矩形和圓
from tkinter import *
root = Tk()
cnv = Canvas(root,width = 200,height = 300)
cnv.pack()
cnv.create_line(0,0,200,100,width = 4) 
cnv.create_line(0,100,200,0,fill= 'blue',dash=(4,4))
cnv.create_rectangle(50,25,160,80,fill = 'red') 
cnv.create_oval(50,150,150,250,width= 1) 
root.mainloop()

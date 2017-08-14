#e7-3-2滑鼠事件測試
from tkinter import * 
root= Tk()
def printCoords(event): 
    if event.num == 1:
        mouse_click_type = "滑鼠左擊"
    elif event.num == 3:
        mouse_click_type = "滑鼠右擊"
    else:
        mouse_click_type = "其他滑鼠事件"
    print(mouse_click_type,event.x,event.y)
root.bind('<Button-1>',printCoords) 
root.bind('<Button-3 >',printCoords) 
root.mainloop(  ) 

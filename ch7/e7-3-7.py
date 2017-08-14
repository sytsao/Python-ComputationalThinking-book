#e7-3-7建立簡單功能表
from tkinter import  *
root= Tk()
def openCall() : 
    print('你按一了下開啟檔案 選項')
def saveCall ( ) :
    print('你按一了下儲存檔案 選項')
def aboutCall ( ) :
    print('這是 Menu 功能表的簡單展示')
menubar=Menu(root)#建立功能表列 menubar 
filemenu = Menu(menubar)
filemenu.add_command( label = "開啟檔案",command = openCall)
filemenu.add_command( label = "儲存檔案",command = saveCall)
filemenu.add_separator()
menubar.add_cascade( label = "檔案",menu= filemenu)   
helpmenu = Menu(menubar)
helpmenu.add_command( label = "關於",command = aboutCall)
menubar.add_cascade( label = "幫助",menu = helpmenu)
root.config( menu = menubar) 
mainloop( )

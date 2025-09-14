from tkinter import *
import pyqrcode
import png
from PIL import ImageTk,Image


#ชื่อแอพ
root=Tk()
root.title("QRCode Generator")
canvas=Canvas(root,width=400,height=500)
canvas.pack()

app_label=Label(root,text="QRCode Generator",font=('Arial',20,'bold'))
canvas.create_window(200,50,window=app_label)


name_label=Label(root,text="ชื่อคิวอาร์โค้ด")
canvas.create_window(200,100,window=name_label)

Link_label=Label(root,text="URL")
canvas.create_window(200,100,window=Link_label)

name_entry=Entry(root)
canvas.create_window(200,130,window=name_entry)

link_entry=Entry(root)
canvas.create_window(200,180,window=link_entry)

button=Button(text="สร้างคิวอาร์โค้ด")
canvas.create_window(200,230,window=button)

root.mainloop()
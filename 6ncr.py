import tkinter as tk
root = tk.Tk()
root.title("verry cool script")

mylabel = tk.Label(text="Hello World", fg="black", font="96").pack()

def showMessage():
    tk.Label(text="ชื่อ: นาย ตรัยรัตน์ ประทีปคีรี\nชั้น: ม.5/8\n เลขที่: 23", fg="green", font="48").pack()
    
btn1 = tk.Button(root, text="Press Me!", command=showMessage).pack()

root.geometry("469x469")
root.mainloop()
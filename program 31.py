from tkinter import *

root =Tk()
root.title("bca apps")
root.geometry("700x600")

f1=Frame(root)
f1.config(bg="YELLOW")
f1.pack(fill=BOTH,expand=True)

l1=Label(f1,text="Arithmetic operation",bg="RED",fg="YELLOW",font=("Arial",25,"bold"))
l1.pack()

f2=Frame(root)
f2.config(bg="RED")
f2.pack(fill=BOTH,expand=True)

l2=Label(f2,text="Number first")
l2.pack()

root.mainloop()

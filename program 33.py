from tkinter import*

root=Tk()
root.title("login page")
root.geometry("500x700")

l=Label(root,text="user name")
l.pack()

e=Entry(root)
e.pack()

b=Button(root,text="login")
b.pack()

root.mainloop()

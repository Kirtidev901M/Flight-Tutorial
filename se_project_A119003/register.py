from tkinter import*
from tkinter import messagebox as mb
import os
import sys
import runpy


root = Tk()
root.title("REGISTRAR")
root.geometry("900x600+300+100")
f=Frame(root,height=900,width=900,bg="sienna")


def new():
    root.destroy()
    os.system("reg_str.py")

def update():
    root.destroy()
    os.system("update_reg.py")

def view():
    root.destroy()
    os.system("view_jims.py")

def move():
    root.destroy()
    os.system("start_sE.py")


but=Button(root,width=15,text="REGISTER NEW CASE",font=("Helvetica, bold", 15),bd=7,relief="raised",bg="sandy brown",command=new,padx=20,).place(x=0, y=50)



b1=Button(root,width=15,text="UPDATE CASE",font=("Helvetica, bold", 15),bd=7,relief="raised",bg="sandy brown",command=update,padx=20,).place(x=340, y=50)


 
b1=Button(root,width=15,text="VIEW CASE",font=("Helvetica, bold", 15),bd=7,relief="raised",bg="sandy brown",command=view,padx=20,).place(x=660, y=50)



b1=Button(root,width=15,text="LOGOUT",font=("Helvetica, bold", 15),bd=7,bg="coral",fg="red",relief="raised",padx=20,command=move).place(x=360, y=400)










Label.pack
Entry.pack
f.pack()
root.mainloop()

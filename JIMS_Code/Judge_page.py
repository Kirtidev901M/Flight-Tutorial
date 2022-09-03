from tkinter import*
from tkinter import messagebox as mb
import os
import sys

root = Tk()
root.title("JUDGE ACCOUNT")
root.geometry("900x600+300+100")
f=Frame(root,height=900,width=900,bg="sienna")
w= Label(root,text="NAME:Justice Sharad Arvind Bobde",font=("Helvetica, bold", 25),bg="sienna",padx=20,bd=4,relief="ridge",width=45).place(x = 0,y = 10) 
R= Label(root,text="DOJ:18 November 2019",font=("Helvetica, bold", 20),bg="sienna",padx=20,bd=4,relief="ridge",width=53).place(x = 0,y = 56)
s=Label(root,text="NOMINATOR:Collegium of the Supreme Court of India",font=("Helvetica, bold", 20),bg="sienna",padx=20,bd=4,relief="ridge",width=53).place(x = 0,y = 96)
q=Label(root,text="Former Chief Justice of Madhya Pradesh High Court\nServing as the Chancellor of Maharashtra National Law University,Mumbai University of Delhi\nDue to retire on 23 April 2021.\nTenure of eight years in the Supreme Court of India.",anchor=NW, justify=LEFT,font=("Helvetica, bold", 15),bg="sienna",bd=4,relief="ridge",fg="steelblue",width=80).place(x = 0,y = 136)

def view():
    root.destroy()
    os.system("view_jims.py")




csolved = StringVar()
cpending = StringVar()

w= Label(root,text="ENTER CASE ID/KEYWORD",font=("Helvetica", 15),bg="sienna",padx=20,bd=4,relief="ridge",fg="blue").place(x = 30,y = 250) 
solved=Entry(root, bd=5,relief="sunken",textvariable=csolved).place(x=30,y=280)
r= Button(root,text="VIEW SOLVED CASE ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="raised",command=view).place(x = 30,y = 310)





def capture():
    k= idnumber.get()
    d= password.get()
    if (d=="kdm" and k=="sharad"):
        print("scs")
        mb.showinfo(title="Sharad Arvind Bobde" ,message="LOGIN SUCCESSFULL REDIRECTING")
    else:
        print("o")
        mb.showwarning(title="warning",message="invalid credentials")

def close():
        root.destroy() 
        os.system("start_SE.py")


def reset():
    csolved.set("")
    cpending.set("")

s1=Button(root,width=10,text="RESET",bd=5,relief="raised",bg="coral",command=reset).place(x=400, y=500)
re=Button(root,width=10,text="LOGOUT",bd=5,relief="raised",bg="coral",fg="red",command=close).place(x=300, y=500)






Label.pack
Entry.pack
f.pack()
root.mainloop()

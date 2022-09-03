from tkinter import*
from tkinter import messagebox as mb
import os
import sys


root = Tk()
root.title("JUDICIARY INFORMATION MANAGEMENT SYSTEM")
root.geometry("900x600+300+100")
f=Frame(root,height=900,width=900,bg="sienna")
w= Label(root,text="JUDICIARY INFORMATION MANAGEMENT SYSTEM",font=("Helvetica, bold", 25),fg="black",bg="sienna",padx=20,bd=7,relief="ridge").place(x = 10,y = 10) 

# registrar login:

password = StringVar()
    
def pas():
    
    s=password.get()
    if (s=="registrar"):
       
        print("succ")
        root.destroy()
        os.system("register.py")
        
        
        
    else:
        mb.showerror(title="error",message="UNAUTHORIZED ACCESS IS DENIED")
        password.set("")


r= Label(root,text="REGISTRAR ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken").place(x = 30,y = 100)
ric=Entry(root, bd=5,relief="sunken",show="*",font=("Helvetica, bold",10),textvariable=password).place(x=30,y=130)
r1=Button(root,width=10,text="LOGIN",bd=5,relief="raised",bg="coral",command=pas).place(x=60, y=160)


def lawyer():
    root.destroy()
    os.system("lwayer.py")

    



# judge login page starts here:
def judge():
    root.destroy()
    os.system("judge.py")
# judge login page ends here
# mainpage work
    
j= Label(root,text="JUDGE ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken").place(x = 400,y = 100)
j1=Button(root,width=10,text="ACCESS",bd=5,relief="raised",command=judge,bg="coral").place(x=420, y=150)

l= Label(root,text="ADVOCATE ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken").place(x = 690,y = 100) 
l1=Button(root,width=10,text="ACCESS",bd=5,relief="raised",command=lawyer,bg="coral").place(x=715, y=150)




#copyright and brand name begins here

h= Label(root,text="© KIRTIDEV MOHAPATRA",font=("Helvetica, bold",15),fg="black",bg="sienna").place(x =30,y = 500)
g= Label(root,text="ZYCOS SOFTECH",font=("Helvetica, bold", 15),fg="black",bg="sienna").place(x =30,y = 530)
Label.pack
Label.pack
Label.pack
Label.pack

f.pack()




root.mainloop()

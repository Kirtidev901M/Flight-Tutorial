from tkinter import*
from tkinter import messagebox as mb
import os


root = Tk()
root.title("JUDGE LOGIN_SECTION")
root.geometry("900x600+300+100")
f=Frame(root,height=900,width=900,bg="sienna")
w= Label(root,text="INDIAN BAR COUNCIL",font=("Helvetica, bold", 25),fg="black",bg="sienna",padx=20,bd=7,relief="ridge").place(x = 300,y = 10) 


password = StringVar()
idnumber = StringVar()


r= Label(root,text="USER NAME ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken").place(x = 30,y = 100)
idnumber_k=Entry(root, bd=5,relief="sunken",textvariable=idnumber).place(x=250,y=100)


 
j= Label(root,text="PASSWORD ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken").place(x =30,y = 200)
password_k=Entry(root,bd=5,relief="sunken",show="*",font=("Helvetica, bold",8),textvariable=password).place(x=250,y=200)
 
def capture():
    k= idnumber.get()
    d= password.get()
    if (d=="kdm" and k=="sharad"):
        print("scs")
        mb.showinfo(title="Sharad Arvind Bobde" ,message="LOGIN SUCCESSFULL REDIRECTING ...")
        os.system("Judge_page.py")
    else:
        print("o")
        mb.showwarning(title="warning",message="invalid credentials")
        idnumber.set("")
        password.set("")

def move():
    root.destroy()
    os.system("start_SE.py")

s1=Button(root,width=10,text="LOGIN",bd=5,relief="raised",bg="sandy brown",command=capture).place(x=250, y=300)
z=Button(root,width=10,text="EXIT",bd=5,relief="raised",bg="sandy brown",command=move).place(x=340, y=300)






Label.pack
Entry.pack
f.pack()
root.mainloop()

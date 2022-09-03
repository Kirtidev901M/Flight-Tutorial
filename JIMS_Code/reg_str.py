from tkinter import*
from tkinter import messagebox as mb
import os
import sqlite3

root = Tk()
root.title("NEW CASE")
root.geometry("900x600+300+100")
f23=Frame(root,height=900,width=900,bg="sienna")

conn=sqlite3.connect("jims.db")
c=conn.cursor()
    
    
    
    
    

cname=StringVar()
ccrime=StringVar()
loc=StringVar()
dt=StringVar()
inv=StringVar()
jud=StringVar()
defe=StringVar()
pro=StringVar()
evid=StringVar()
ver=StringVar()

def save():
    k=cname.get()
    a=ccrime.get()
    b=loc.get()
    ck=dt.get()
    d=inv.get()
    e=jud.get()
    f=defe.get()
    g=pro.get()
    h= evid.get()
    i=ver.get()
    print(k,a,b,ck,d,e,f,g,h)
    
    c.execute("CREATE TABLE IF NOT EXISTS case_d(name TEXT PRIMARY KEY,crime TEXT,location TEXT,dt_of_arrest TEXT,officer TEXT,judge TEXT,defendant TEXT,prosecution TEXT,evidence TEXT,verdict TEXT)")
    c.execute('''INSERT INTO case_d (name,crime ,location ,dt_of_arrest ,officer ,judge ,defendant ,prosecution ,evidence,verdict) VALUES(?,?,?,?,?,?,?,?,?,?)''',
          (k,a,b,ck,d,e,f,g,h,i))
    conn.commit()
    mb.showinfo(title="case ID",message=k)
def reset():
    k=cname.set("")
    a=ccrime.set("")
    b=loc.set("")
    ck=dt.set("")
    d=inv.set("")
    e=jud.set("")
    f=defe.set("")
    g=pro.set("")
    h= evid.set("")
    i=ver.set("")
    

r= Label(root,text="CONVICT NAME ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y = 5)
name=Entry(root, bd=5,relief="sunken",width=85,textvariable=cname).place(x=350,y=5)


r= Label(root,text="CRIME ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y = 35)
crime=Entry(root, bd=5,relief="sunken",width=85,textvariable=ccrime).place(x=350,y=35)


r= Label(root,text="LOCATION ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y = 65)
location=Entry(root, bd=5,relief="sunken",width=85,textvariable=loc).place(x=350,y=65)


r= Label(root,text="DATE OF ARREST ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y = 95)
date=Entry(root, bd=5,relief="sunken",width=85,textvariable=dt).place(x=350,y=95)


r= Label(root,text="INVESTING OFFICER ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y = 125)
invest=Entry(root, bd=5,relief="sunken",width=85,textvariable=inv).place(x=350,y=125)


r= Label(root,text="JUDGE ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y =155)
judg=Entry(root, bd=5,relief="sunken",width=85,textvariable=jud).place(x=350,y=155)


r= Label(root,text="DEFENDANT NAME ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y =185)
defendant=Entry(root, bd=5,relief="sunken",width=85,textvariable=defe).place(x=350,y=185)


r= Label(root,text="PROSECUTION NAME ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y =215)
prose=Entry(root, bd=5,relief="sunken",width=85,textvariable=pro).place(x=350,y=215)


r= Label(root,text="EVIDENCE ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y =245)
evidence=Entry(root, bd=5,relief="sunken",width=85,textvariable=evid).place(x=350,y=245)

r= Label(root,text="VERDICT ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y =285)
verdict=Entry(root, bd=5,relief="sunken",width=85,textvariable=ver).place(x=350,y=285)


r1=Button(root,width=10,text="SAVE",bd=5,relief="raised",bg="coral",command=save).place(x=360, y=500)
r5=Button(root,width=10,text="RESET",bd=5,relief="raised",bg="coral",command=reset).place(x=460, y=500)
# choices for different crimes




   










Entry.pack
Label.pack
f23.pack()
root.mainloop()
conn.close()

from tkinter import*
from tkinter import messagebox as mb
import os
import sys
import sqlite3



root = Tk()
root.title("UPDATE CASE")
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
z=StringVar()
cid=StringVar()

def search():
    z=cid.get()
    print(z)
    c.execute("CREATE TABLE IF NOT EXISTS case_d(name TEXT PRIMARY KEY,crime TEXT,location TEXT,dt_of_arrest TEXT,officer TEXT,judge TEXT,defendant TEXT,prosecution TEXT,evidence TEXT,verdict TEXT)")
    c.execute("SELECT crime FROM case_d WHERE name=?",(z,))
    sunny=c.fetchone()
    print(sunny)
    conn.commit()
    vira=ccrime.set(sunny[0])
    
    c.execute("CREATE TABLE IF NOT EXISTS case_d(name TEXT PRIMARY KEY,crime TEXT,location TEXT,dt_of_arrest TEXT,officer TEXT,judge TEXT,defendant TEXT,prosecution TEXT,evidence TEXT,verdict TEXT)")
    c.execute("SELECT name FROM case_d WHERE name=?",(z,))
    sunny=c.fetchone()
    print(sunny)
    conn.commit()
    k=cname.set(sunny[0])
    
    c.execute("CREATE TABLE IF NOT EXISTS case_d(name TEXT PRIMARY KEY,crime TEXT,location TEXT,dt_of_arrest TEXT,officer TEXT,judge TEXT,defendant TEXT,prosecution TEXT,evidence TEXT,verdict TEXT)")
    c.execute("SELECT location FROM case_d WHERE name=?",(z,))
    sunny=c.fetchone()
    print(sunny)
    conn.commit()
    b=loc.set(sunny[0])
    
    c.execute("CREATE TABLE IF NOT EXISTS case_d(name TEXT PRIMARY KEY,crime TEXT,location TEXT,dt_of_arrest TEXT,officer TEXT,judge TEXT,defendant TEXT,prosecution TEXT,evidence TEXT,verdict TEXT)")
    c.execute("SELECT dt_of_arrest FROM case_d WHERE name=?",(z,))
    sunny=c.fetchone()
    print(sunny)
    conn.commit()
    ck=dt.set(sunny[0])
    
    c.execute("CREATE TABLE IF NOT EXISTS case_d(name TEXT PRIMARY KEY,crime TEXT,location TEXT,dt_of_arrest TEXT,officer TEXT,judge TEXT,defendant TEXT,prosecution TEXT,evidence TEXT,verdict TEXT)")
    c.execute("SELECT officer FROM case_d WHERE name=?",(z,))
    sunny=c.fetchone()
    print(sunny)
    conn.commit()
    d=inv.set(sunny[0])
    
    c.execute("CREATE TABLE IF NOT EXISTS case_d(name TEXT PRIMARY KEY,crime TEXT,location TEXT,dt_of_arrest TEXT,officer TEXT,judge TEXT,defendant TEXT,prosecution TEXT,evidence TEXT,verdict TEXT)")
    c.execute("SELECT judge FROM case_d WHERE name=?",(z,))
    sunny=c.fetchone()
    print(sunny)
    conn.commit()
    e=jud.set(sunny[0])
    
    c.execute("CREATE TABLE IF NOT EXISTS case_d(name TEXT PRIMARY KEY,crime TEXT,location TEXT,dt_of_arrest TEXT,officer TEXT,judge TEXT,defendant TEXT,prosecution TEXT,evidence TEXT,verdict TEXT)")
    c.execute("SELECT defendant FROM case_d WHERE name=?",(z,))
    sunny=c.fetchone()
    print(sunny)
    conn.commit()
    f=defe.set(sunny[0])
    
    c.execute("CREATE TABLE IF NOT EXISTS case_d(name TEXT PRIMARY KEY,crime TEXT,location TEXT,dt_of_arrest TEXT,officer TEXT,judge TEXT,defendant TEXT,prosecution TEXT,evidence TEXT,verdict TEXT)")
    c.execute("SELECT prosecution FROM case_d WHERE name=?",(z,))
    sunny=c.fetchone()
    print(sunny)
    conn.commit()
    g=pro.set(sunny[0])
    
    c.execute("CREATE TABLE IF NOT EXISTS case_d(name TEXT PRIMARY KEY,crime TEXT,location TEXT,dt_of_arrest TEXT,officer TEXT,judge TEXT,defendant TEXT,prosecution TEXT,evidence TEXT,verdict TEXT)")
    c.execute("SELECT evidence FROM case_d WHERE name=?",(z,))
    sunny=c.fetchone()
    print(sunny)
    conn.commit()
    h= evid.set(sunny[0])
    
    c.execute("CREATE TABLE IF NOT EXISTS case_d(name TEXT PRIMARY KEY,crime TEXT,location TEXT,dt_of_arrest TEXT,officer TEXT,judge TEXT,defendant TEXT,prosecution TEXT,evidence TEXT,verdict TEXT)")
    c.execute("SELECT verdict FROM case_d WHERE name=?",(z,))
    sunny=c.fetchone()
    print(sunny)
    conn.commit()
    mn=ver.set(sunny[0])
    
    
def move():
    root.destroy()
    os.system("start_sE.py")
   











r= Label(root,text="CONVICT NAME ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y = 5)
name=Entry(root, bd=5,relief="sunken",width=85,state='readonly',textvariable=cname).place(x=350,y=5)


r= Label(root,text="CRIME ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y = 35)
crime=Entry(root, bd=5,relief="sunken",width=85,state='readonly',textvariable=ccrime).place(x=350,y=35)


r= Label(root,text="LOCATION ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y = 65)
location=Entry(root, bd=5,relief="sunken",width=85,state='readonly',textvariable=loc).place(x=350,y=65)


r= Label(root,text="DATE OF ARREST ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y = 95)
date=Entry(root, bd=5,relief="sunken",width=85,state='readonly',textvariable=dt).place(x=350,y=95)


r= Label(root,text="INVESTING OFFICER ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y = 125)
invest=Entry(root, bd=5,relief="sunken",width=85,state='readonly',textvariable=inv).place(x=350,y=125)


r= Label(root,text="JUDGE ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y =155)
judg=Entry(root, bd=5,relief="sunken",width=85,state='readonly',textvariable=jud).place(x=350,y=155)


r= Label(root,text="DEFENDANT NAME ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y =185)
defendant=Entry(root, bd=5,relief="sunken",width=85,state='readonly',textvariable=defe).place(x=350,y=185)


r= Label(root,text="PROSECUTION NAME ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y =215)
prose=Entry(root, bd=5,relief="sunken",width=85,state='readonly',textvariable=pro).place(x=350,y=215)


r= Label(root,text="EVIDENCE ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y =245)
evidence=Entry(root, bd=5,relief="sunken",width=85,state='readonly',textvariable=evid).place(x=350,y=245)

r= Label(root,text="VERDICT ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y =285)
verdict=Entry(root, bd=5,relief="sunken",width=85,state='readonly',textvariable=ver).place(x=350,y=285)

r= Label(root,text="CASE ID ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken",width=25).place(x = 10,y =315)
case_id=Entry(root, bd=5,relief="sunken",width=85,textvariable=cid).place(x=350,y=315)


r5=Button(root,width=10,text="SEARCH",bd=5,relief="raised",bg="coral",command=search).place(x=360, y=500)

r100=Button(root,width=10,text="EXIT",bd=5,relief="raised",bg="coral",command=move).place(x=560, y=500)


























Entry.pack
Label.pack
f23.pack()
root.mainloop()

conn.close()
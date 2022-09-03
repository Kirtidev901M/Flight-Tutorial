from tkinter import*
import os
import sys

root = Tk()
root.title("ADVOCATE SECTION")
root.geometry("900x600+300+100")
f=Frame(root,height=900,width=900,bg="sienna")
w= Label(root,text="INDIAN BAR COUNCIL",font=("Helvetica, bold", 25),fg="black",bg="sienna",padx=20,bd=7,relief="ridge").place(x = 300,y = 10) 


cidn=StringVar()
licn=StringVar()


r= Label(root,text="LICENSCE NUMBER ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken").place(x = 30,y = 100)
lic=Entry(root, bd=5,relief="sunken",textvariable=licn).place(x=250,y=100)


 
j= Label(root,text="CASE ID ",font=("Helvetica", 15),fg="white",bg="sienna",padx=20,bd=2,relief="sunken").place(x =30,y = 200)
cid=Entry(root,bd=5,relief="sunken",textvariable=cidn).place(x=250,y=200)
 
def search():
    j=cidn.get()
    l=licn.get()
    ##res=mb.askquestion(title="PAYMENT",message="MAKE PAYMENT FOR VIEW OF PARTICULARS")
    ##if res=='yes':
    os.system("payment_page1.html")


def close():
    root.destroy()
    os.system("start_SE.py")
    
    
s1=Button(root,width=10,text="SEARCH",bd=5,relief="raised",bg="sandy brown",command=search).place(x=250, y=300)
z=Button(root,width=10,text="BACK",bd=5,relief="raised",bg="sandy brown",command=close).place(x=340, y=300)






Label.pack
Entry.pack
f.pack()




root.mainloop()

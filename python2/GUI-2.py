from tkinter import *

def add():
    nm1=int(txt1.get())
    nm2=int(txt2.get())
    res=nm1+nm2
    print("Addition : ",res)

def sub():
    nm1 = int(txt1.get())
    nm2 = int(txt2.get())
    res=nm1-nm2
    print("substrcation : ",res)

def mul():
    nm1 = int(txt1.get())
    nm2 = int(txt2.get())
    res=nm1*nm2
    print("Multiplication : ",res)

def div():
    nm1 = int(txt1.get())
    nm2 = int(txt2.get())
    res=nm1/nm2
    print("Division : ",res)

root=Tk()
root.title("calculator")
root.geometry("500x500")
root.configure(bg="light gray")
f1=("Calisto MT",14,"bold","underline")
f2=("Calisto MT",14)
f3=("Harrington",19)

tl0=Label(root,text="Calculator...",font=f3,fg="blue",bg="light gray")
tl0.place(x=20,y=20)

tl1=Label(root,text="Enter First Number:",font=f1,fg="black",bg="light gray")
tl1.place(x=20,y=80)
txt1=Entry(root,font=f2,fg="black")
txt1.place(x=220,y=80)

tl2=Label(root,text="Enter second Number:",font=f1,fg="black",bg="light gray")
tl2.place(x=20,y=120)
txt2=Entry(root,font=f2,fg="black")
txt2.place(x=220,y=120)


bt1=Button(root,text="ADD",bg="pink",command=add)
bt1.place(x=20,y=180)

bt1=Button(root,text="SUB",bg="pink",command=sub)
bt1.place(x=70,y=180)

bt1=Button(root,text="MUL",bg="pink",command=mul)
bt1.place(x=120,y=180)

bt1=Button(root,text="DIV",bg="pink",command=div)
bt1.place(x=170,y=180)

tl3=Label(root,text="Result :",font=f1,fg="black",bg="light gray")
tl3.place(x=20,y=230)
txt3=Entry(root,font=f2,fg="black")
txt3.place(x=120,y=230)

root.mainloop()
from tkinter import *


def is_person_exist():
    fg = False
    a = txt1.get()
    b = txt2.get()
    fobj = open("users.txt", "r")
    ex_ur = fobj.readlines()
    for one_ur in ex_ur:
        ls = one_ur.split(",")
        ls1=ls[1].replace("\n","")
        if ls[0] == a and ls1 == b:
            fg = True
            break
    if fg == True:
        print("You have login successfully ...")
    elif fg == False:
        print("No such user is found ...")


try:
    open("users.txt", "r")
except FileNotFoundError as err:
    open("users.txt", "w")
base = Tk()
base.geometry("900x700")  # to set dimension of base

base.configure(bg="light gray")

base.title("Login Frame")

f1 = ("Forte", 18, "bold")
tl = Label(base, text="Baate-shaate", font=f1, fg='black')
tl.place(x=50, y=20)

f2 = ("Comic Sans MS", 13, "bold")
lb = Label(base, text="Enter Your UserName : ", font=f2, bg='pink', fg='black')
lb.place(x=140, y=80)

lb1 = Label(base, text="Enter Your Password : ", font=f2, bg='pink', fg='black')
lb1.place(x=140, y=120)

txt1 = Entry(base, font=f2)
txt1.place(x=500, y=80)

txt2 = Entry(base, font=f2,show="*")
txt2.place(x=500, y=120)

ch = Checkbutton(base, text="Keep loin", bg='pink', fg='black', font=f2)
ch.place(x=500, y=170)

btn1 = Button(base, text="Login", font=f2, bg="sky blue", fg="black", command=is_person_exist)
btn1.place(x=360, y=240)
btn1.config(width=13, height=1)

base.mainloop()

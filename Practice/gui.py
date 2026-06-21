import tkinter
from tkinter import messagebox,ttk,PhotoImage , scrolledtext
import openpyxl 


file_path = r"C:/Users/Lenovo/Desktop/python-/Practice/test.xlsx"

def on_submit():
    name = name_tex.get()
    email = email_tex.get()
    phone = phone_tex.get()
    branch = branch_dropdown.get()
    agree = agree_value.get()
   
    if name and email and phone and branch and agree==1:
        A = openpyxl.load_workbook(file_path)
        B=A["registration"]
        B.append([name,email,phone,branch,agree])
        A.save(file_path)
        A.close
        messagebox.showinfo("Status","Hey "+name+" Your! data submited")
    else:
        messagebox.showwarning("Warning","Please submite all detail")


root = tkinter.Tk()  # create window
root.geometry("400x600")

root.title("Studet Registration Form")
# root.configure(bg="#90D5FF") # for adding baground colour
image_path = PhotoImage(file=r"C:/Users/Lenovo/Desktop/python-/Practice/360logo.png")
bg_image = tkinter.Label(root,image=image_path)
bg_image.place(relheight=1,relwidth=1)

# name_label = tkinter.Label(root,text="Enter Nmae : ")
# name_label.pack(anchor=tkinter.W , padx=10)  
# name_tex = tkinter.Entry(root)
# name_tex.pack(anchor=tkinter.W , padx=10)    
form_label=tkinter.Label(root,text="Welcome...",font=('Georgia',20))

name_label = tkinter.Label(root,text="Enter Nmae : ", font=('Georgia',15))
name_label.pack(anchor=tkinter.W , padx=30, pady=5)  
name_tex = tkinter.Entry(root)
name_tex.pack(anchor=tkinter.W , padx=30, pady=5)  

email_label = tkinter.Label(root,text="Enter Email : ", font=('Georgia',15))
email_label.pack(anchor=tkinter.W , padx=30, pady=5)  
email_tex = tkinter.Entry(root)
email_tex.pack(anchor=tkinter.W , padx=30, pady=5) 

phone_label = tkinter.Label(root,text="Enter Phone : ", font=('Georgia',15))
phone_label.pack(anchor=tkinter.W , padx=30, pady=5)  
phone_tex = tkinter.Entry(root)
phone_tex.pack(anchor=tkinter.W , padx=30, pady=5) 

# for dropdown
branch_label = tkinter.Label(root,text="Choice the branch : ", font=('Georgia',15))
branch_label.pack(anchor=tkinter.W , padx=30, pady=5) 
choices = ["AIML","CS","ENTC","Mech"]
branch_dropdown = ttk.Combobox(root,values=choices)
branch_dropdown.pack(anchor=tkinter.W , padx=30, pady=5) 

# for checkbox
agree_value = tkinter.IntVar()
agree_checkbox = tkinter.Checkbutton(root, text="Do you agree on tearm and condition",variable=agree_value)
agree_checkbox.pack(anchor=tkinter.W , padx=30, pady=5) 

# for Message
msg_label = tkinter.Label(root,text="Message : ", font=('Georgia',15))
text_scroll=scrolledtext.ScrolledText(root, wrap=tkinter.WORD, height=5, state=tkinter.DISABLED, bg='light yellow',font=('Georgia',15))
text_scroll.pack(anchor=tkinter.W , padx=30, pady=5 , fill=tkinter.BOTH,expand=True)

submit_buttn = tkinter.Button(root, text="Submit" , command=on_submit, font=('Georgia',15))
submit_buttn.pack(anchor=tkinter.W , padx=30, pady=5)


root.mainloop()  # running window in loop so that it will be visible
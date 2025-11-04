import datetime

def add_stud():
    print("Enter your detail seprate by space :\n")
    prn=input("PRN :")
    name=input("FULL NAME :")  
    email=input("E-MAIL ID :")  
    phno=input("PHONE NO :")
    cl=input("Class :")
    fobj=open("all_lb_stud.txt","a")
    fobj.write(prn+","+name+","+email+","+phno+","+cl+"\n")
    fobj.close()
    print("New student is added....")


def add_book():
    n_book=input("Enter Book No :")
    t_book=input("Enter Title :")
    a_book=input("Enter Auther :")
    p_book=input("Enter Publication name :")
    fobj=open("all_lb_book.txt","a")
    fobj.write(n_book+","+t_book+","+a_book+","+p_book+"\n")
    fobj.close()
    print("New book is added...")

def is_present(a_list,nm):
    found=False
    for one in a_list:
        ls=one.split(",")
        if ls[0]==nm:
            found= True
    return found
 
def gettime():
    a=datetime.date.today()
    d=str(a.day)
    m=str(a.month)
    y=str(a.year)
    return d,m,y         

def issue_book():
    b_fg=False
    s_fg=False
    b_no=input("Enter book no :")
    enr_no=input("Enter entrollment no :")
    fobj=open("all_lb_book.txt","r")
    b_list=fobj.readlines()
    fobj.close()
    b_fg = is_present(b_list,b_no)
    
    if b_fg==False:
        print("Book is not present....")
    
    fobj=open("all_lb_stud.txt","r")
    s_list=fobj.readlines()
    fobj.close()
    s_fg = is_present(s_list,enr_no)
    
    if s_fg==False:
        print("Student is not in over list , first add student....")
    
    if s_fg==True and b_fg==True:
        cu,mo,yr=gettime()
        fobj=open("all_issue.txt","a")
        fobj.write(b_no+","+enr_no+","+cu+"/"+mo+"/"+yr+","+"NA\n")
        fobj.close()
        print("Book issued....")
    
    
def return_book():
    b_no=input("Enter book no : ")
    enr=input("Enter enrolment no : ")
    fobj=open("all_issue.txt","r")
    b_list=fobj.readlines()
    fobj.close()
    ind=0
    for one_bk in b_list:
        ls=one_bk.split(",")
        if ls[0]==b_no and ls[1]==enr and ls[3]=="NA\n":
           ls[3]="/".join(gettime())+"\n"
           r_str=",".join(ls) 
           b_list[ind]=r_str
           fobj=open("all_issue.txt","w")
           fobj.writelines(b_list)
           fobj.close()
           print("Book returned....")
           break
        ind=ind+1
    
             

def show_not_return():
    fobj=open("all_issue.txt","r")
    r_book=fobj.readlines()
    fobj.close()
    print("NOT returned books are : ")
    for one_bk in r_book:
        ls=one_bk.split(",")
        if ls[3]=="NA\n":
            print("Book no : ",ls[0],"Enrolment no : ",ls[1],"Inssue date : ")
    

def search_stud():
    fg=False
    print("Enter Enrolment no :")
    s_enr=input()
    fobj=open("all_lb_stud.txt","r")
    s_stud=fobj.readlines()
    fobj.close()
    for one_stud in s_stud:
       ls=one_stud.split(",")
       if ls[0]==s_enr:
           print("Name :",ls[1],"Email :",ls[2],"Phone no :",ls[3],"Class :",ls[4])
           fg=True
           break
    if fg==False:
        print("Student is not list....")
        
def search_book():
    fg=False
    b_no=input("Enter Book no : ")
    fobj=open("all_lb_book.txt","r")
    b_list=fobj.readlines()
    fobj.close()
    for b_sea in b_list:
        ls=b_sea.split(",")
        if ls[0]==b_no:
            print(" tital : ",ls[1]," Auther : ",ls[2]," Publication : ",ls[3])
            fg=True
            break
    if fg==False:
        print("Book is not present ....")
    
    
def stud_history():
    enr=input("Enter enrolment no : ")
    fobj = open("all_issue.txt","r")
    s_list=fobj.readlines()
    for one in s_list:
        ls=one.split(",")
        if ls[1]==enr:
            print("Book issued : ",ls[0],"Issued date : ",ls[2],"Return date : ",ls[3])

def book_history():
    b_no=input("Enter book no :")
    fobj=open("all_issue.txt","r")
    f_book=fobj.readlines()
    fobj.close()
    for one in f_book:
       ls=one.split(",")
       if ls[0]==b_no:
           print("histori of that book : ")
           print("Book no: ",ls[0],"date of issue : ",ls[2],"date of return : ",ls[3])




# main program starts from here
while True:
    print("\nSelect operation")
    print("1 - Add New Student")
    print("2 - Add New Book")
    print("3 - Issue Book")
    print("4 - Return Book")
    print("5 - Search Book")
    print("6 - Search Student")
    print("7 - History Student")
    print("8 - History Book")
    print("9 - Show Not Return Book")
    print("0 - Exit")
    ch = int(input("Provide your choice : "))

    if ch==1:
        add_stud()
    elif ch==2:
        add_book()
    elif ch==3:
        issue_book()
    elif ch==4:
        return_book()
    elif ch==5:
        search_book()
    elif ch==6:
        search_stud()
    elif ch==7:
        stud_history()
    elif ch==8:
        book_history()
    elif ch==9:
         show_not_return()
    elif ch==0:
        exit(0)

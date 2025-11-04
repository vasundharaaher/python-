
'''* File Handling project that contains following operations:
	1. Add new student
	2. Delete student
	3. Update student information
	4. Show all student
	5. Search student

* Student Details sholuld be:
	- Enrollment Number
	- Name
	- Mobile Number
	- Email
	- City

* Prepare a menu-driven program with individual functions for each operation.
* The data/values of student should be stored in one file "all_stud.txt"

* HINT : Think abount "a" mode
* Hint: Never write any messages in file. Write only data.
* Hint: Use a separator for data. (one student data in one line)

===================== Refer following skeleton ==================
'''
def add_new_stud():
    # accept all info from user and write into file "all_stud.txt"
    # write only data (with a separator)
    fobj=open("all_stud.txt","a")
    prn=input("Enter your detail seprate by space :PRN :")
    print("\nFULL NAME :")
    name=input()  
    print("\nE-MAIL ID :")
    email=input()  
    print("\nPHONE NO :")
    phno=input() 
    fobj.write(prn+","+name+","+email+","+phno+"\n")


def del_stud():
    # ask enrollment number and delete all information of that student.
    fobj=open("all_stud.txt","r")
    print("Enter PRN whose data you want to delete :")
    d_prn=input()
    str_stud=fobj.readlines()
    fobj.close()
    ind=0
    for one_stud in str_stud:
        ls=one_stud.split(",")
        if ls[0]==d_prn:
            str_stud.pop(ind) 
            fobj=open("all_stud.txt","w")
            fobj.writelines(str_stud)
            fobj.close()
        ind=ind+1
    fobj=open("all_stud.txt","r")
    sd=fobj.readline()
    fobj.close()
    print(sd)

def update_stud():
    # ask enrollment number and give choices to update specific information
    # and update that single information based on given choice

    """
    print("Enter Enrollment Number of student, whose information you want to Update");
    enr = input()

    # open the file in read mode and write logic to search that student.

    # if student found, then give following choice:
        1 - To update Name
        2 - To update Mobile Number
        3 - To update Email
        4 - To update City
    # else show "No such student found"
    """
    fobj=open("all_stud.txt","r")
    print("Enter PRN whose data you want to delete :")
    d_prn=input()
    str_stud=fobj.readlines()
    fobj.close()
    ind=0
    for one_stud in str_stud:
        ls=one_stud.split(",")
        if ls[0]==d_prn:
            print("What you want to update \n1 - Name\n2 - Email\n3 - Mobile No") 
            ch=int(input("Provide your choice"))
            if ch==1:
                nm=input("Enter your update name :")
                ls[1]=nm
                res_s=",".join(ls)
                str_stud[ind]=res_s
            elif ch==2:
                nm=input("Enter your update Email :")
                ls[2]=nm
                res_s=",".join(ls)
                str_stud[ind]=res_s
            elif ch==3:
                nm=input("Enter your update Mobile No :")
                ls[3]=nm
                res_s=",".join(ls)
                str_stud[ind]=res_s
            fobj=open("all_stud.txt","w")
            fobj.writelines(str_stud)
            fobj.close()
        ind=ind+1
      

def show_all_stud():
    # show information of all students in table form (use \t)
    # don't show any message. Only data in table form.
    fobj=open("all_stud.txt","r")
    sd=fobj.readlines()
    fobj.close()
    for one_stud in sd:
        ls=one_stud.replace(",", "\t")
        print(ls)
    

def search_stud():
    # ask enrollment number and display all information with proper message
    pnr=input("Enter you PNR :")
    fobj=open("all_stud.txt","r")
    stud_list=fobj.readlines()
    fobj.close()
    fg=False
    for one_stud in stud_list:
        ls=one_stud.split(",")
        if ls[0]==pnr:
            print("Name :",ls[1],"Email :",ls[2],"Mobile No :",ls[3],sep="\t")
            fg=True
    if fg==False:
        print("NO such person is found")


# main program starts from here
while True:
    print("Select operation")
    print("1 - Add New Student")
    print("2 - Delete Student")
    print("3 - Update Student Information")
    print("4 - Show all Student Information")
    print("5 - Search Student")
    print("6 - Exit")
    ch = int(input("Provide your choice : "))

    if ch==1:
        add_new_stud()
    elif ch==2:
        del_stud()
    elif ch==3:
        update_stud()
    elif ch==4:
        show_all_stud()
    elif ch==5:
        search_stud()
    elif ch==6:
        exit()

def add_dish():
    fobj=open("hotel_detail.txt","r")
    h_list=fobj.readlines()
    fobj.close()
    h_pin=input("Enter hotel PIN : ")
    found=find_fun(h_list, h_pin)
    if found==True :
        d_nm=input("Enter dish name : ")
        d_p=input("Enter price of dish : ")  
        fobj=open("dish_detail.txt","a")
        fobj.writelines(h_pin+","+d_nm+","+d_p+"\n")
        fobj.close()
    elif found==False :
        print("Hotel is not added....")

    
def find_fun(f_list,a):
    fg=False
    for one_h in f_list:
        ls = one_h.split(",")
        if a == ls[0]:
            fg=True
            break    
    return fg
        
    
  
def add_hotel():
    fobj=open("hotel_detail.txt","r")
    h_list=fobj.readlines()
    fobj.close()
    h_pin=input("Enter hotel PIN : ")
    found=find_fun(h_list, h_pin)
    if found==True:
        print("Already added....")
    elif found==False:
        fobj=open("hotel_detail.txt","a")
        h_nm=input("Enter hotel name : ")
        fobj.write(h_pin+","+h_nm+"\n")
        fobj.close()
    
def check_order():
    pass
def todays_sale():
    pass


while True:
    try :
        open("hotel_detail.txt","r")
        open("dish_detail.txt","r")
    except FileNotFoundError as err :
        open("hotel_detail.txt","w")
        open("dish_detail.txt","w")
    
    print("\n....Select operation....")
    print("1 - add new dish ")
    print("2 - add hotel ")
    print("3 - check order ")
    print("4 - check todays sale ")
    print("0 - Exit")
    ch = int(input("Provide your choice : "))

    if ch==1:
        add_dish()
    elif ch==2:
        add_hotel()
    elif ch==3:
        check_order()
    elif ch==4:
        todays_sale()
    elif ch==8:
        exit()

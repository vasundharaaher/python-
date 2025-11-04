
def search_dish():
    fobj=open("dish_detail.txt","r")
    d_list=fobj.readlines()
    fobj.close()
    fobj1=open("hotel_detail.txt","r")
    h_list=fobj1.readlines()
    fobj1.close()
    s_d=input("Enter dish name you want : ")
    i=0
    for one_h in h_list:
        ls_h=h_list[i].split(",")
        for one_d in d_list:
            ls_d=d_list[i].split(",")
            i=0
            if ls_d[1]==s_d and ls_h[0]==ls_d[0]:
                print(" dish name ",ls_d[1]," hotel name : ",ls_h[1]," price of dish : ",ls_d[2])
                
    
    
    
def print_menu():
    pass
def order_dish():
    pass
def add_to_wishlist():
    pass
def purchase_or():
    pass

while True:
    print("\n....Select operation....")
    print("1 - search dish ")
    print("2 - print menu ")
    print("3 - order dish ")
    print("4 - add in wish list ")
    print("5 - check purchase order ")
    print("0 - Exit")
    ch = int(input("Provide your choice : "))

    if ch==1:
        search_dish()
    elif ch==2:
        print_menu()
    elif ch==3:
        order_dish()
    elif ch==4:
        add_to_wishlist()
    elif ch==5:
        purchase_or()
    elif ch==8:
        exit()

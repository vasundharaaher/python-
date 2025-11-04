'''
* File Handling application on Stock Management


1. Prepare Bill (save bill number and bill date and bill amount in separate file)
2. Print Current Stock
3. Add New Product
4. Update Current Stock (when new stock is arrived, the shopkeeper will update current stock by adding new quantity)
5. Check Purchase Order
6. Update Purchase Order 
	(accept product ID and manually update quantity to order)
7. View Today's sale (total bill amount)

==================================================================
'''

def ls_pd_id(a):
    fg=False
    if a in ls1:
        fg=True
    elif a not in ls1:
        ls1.append(a)
        fg=False
    return fg
        
    
       
def add_new_product():
    pd_id=input("Enter product ID : ")
    fg=ls_pd_id(pd_id)
    if fg==True:
        print("Sorry ...Product Id Repeated ....in case you want to add quantity then go to update current stock....")
    elif fg==False:
        pd_nm=input("Enter product name : ")
        pd_qn=input("Enter product quntity : ")
        pr_pd_pri=input("Enter price of (per) product : ")
        fobj=open("stock_list.txt","a")
        fobj.write(pd_id+","+pd_nm+","+pd_qn+","+pr_pd_pri+"\n")
        fobj.close()

def Prepare_bill():
    fobj=open("stock_list.txt","r")
    sk_list=fobj.readlines()
    fobj.close()
    while True:
        p_id=input("Enter product ID : ")
        fg=ls_pd_id(p_id)
        if fg==False:
            print(".... No such product is available ....")
        elif fg==True:
            qu_pd=input("Enter quantity of product : ")
            
        
        

def ch_purchase_or():
    pass

def view_today():
    pass

def print_stock():
    fobj=open("stock_list.txt","r")
    s_list=fobj.readlines()
    fobj.close()
    print("list of available stock : ")
    for one_p in s_list:
        print(" product : ",one_p)

def find_pd(pd_id,pd_list):
    fg=False
    ind=0
    for one in pd_list:
        ls=one.split(",")
        if ls[0]==pd_id:
            fg= True
            break
        ind=ind+1      
    return fg,ind
    
        
def ud_current_st():
    print("Enter a product ID which info you want to update : ")
    f_stock=input()
    fobj=open("stock_list.txt","r")
    st_list=fobj.readlines()
    fobj.close()
    found,i=find_pd(f_stock,st_list)
    if found==False:
        print("No such product found ")
    if found==True:
        ls=st_list[i].split(",")
        up_pd=int(input("How much quntity you want to update : "))
        ls[2]=str(int(ls[2])+up_pd)
        res_ls=",".join(ls)
        st_list[i]=res_ls
        fobj=open("stock_list.txt","w")
        fobj.writelines(st_list)
        print("... Stock is up dated ...")
    
    
def ud_purchase_or():
    pd_id=input("Enter product ID : ")
    fobj=open("stock_list.txt","a")
    pd_list=fobj.readlines()
    fobj.close()
    fobj1=open("purchase_list.txt","a")
    fobj1.close()
    fg,ind=find_pd(pd_id, pd_list)
    if fg==False:
        print("...product is not present...")
    if fg==True:
        ls=pd_list[ind].split()
        ls[2]=input("Enter the quntity of product you want to order : ")
        res_s=",".join(ls)
        pd_list[ind]=res_s
        fobj.writelines(pd_list)
        fobj1.writelines(res_s)
        

ls1=[]
while True:
    print("\n....Select operation....")
    print("1 - Add New Product ")
    print("2 - print current stock ")
    print("3 - update current stock ")
    print("4 - update purchase order ")
    print("5 - check purchase order ")
    print("6 - Prepare bill()")
    print("7 - todays sale ")
    print("0 - Exit")
    ch = int(input("Provide your choice : "))

    if ch==1:
        add_new_product()
    elif ch==2:
        print_stock()
    elif ch==3:
        ud_current_st()
    elif ch==4:
        ud_purchase_or()
    elif ch==5:
        ch_purchase_or()
    elif ch==6:
        Prepare_bill()
    elif ch==7:
        view_today()
    elif ch==8:
        exit()

    
'''    def ls_pd_id(a):
    fobj = open("stock_list.txt","r")
    ls = fobj.readlines()
    fobj.close()
    fg=False
    for one in ls:
        ls1 = one.split(",")
        if ls1[0]==a:
            fg=True
            break
        else:
            fg=False
    return fg
'''


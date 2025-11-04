


'''
ls=['p','q']
ls1=['1','2','3','4','5']
ls2=[]
l=0
for i in ls1:
    c=1
    k=0
    while c<=2:
        ls2.append(ls[k]+ls1[l])
        k=k+1
        c=c+1
    l=l+1
    
print(ls2)
'''
'''
ls=[[],[],[]]
ls1=[3,6,9]
c=0
for i in ls1 :
    j=1
    while j<=i:
        ls[c].append('#')
        j=j+1
    c=c+1
    i=i+1
print(ls)
'''
'''
ls1=[1,3,5,7,9,10]
ls2=[2,4,6,8]
ls3=[]
j=0
for i in ls1 :
    ls3.append(ls1[j])
    j=j+1
j=0
ls3.pop()
for i in ls2:
    ls3.append(ls2[j])
    j=j+1
    
print(ls3)
'''
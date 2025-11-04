'''
print("Q 1")
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)
'''
'''
print("Q 2")
dic={}
for i in range(1,10):
    dic[i]=i*i
print(dic)
'''    
'''
print("Q 3")
dic={}
ls=[]
i=0
j=1
while i<=9:
    ls1=[]
    c=1
    while c<=10:
        ls1.append(j)
        j=j+1
        c=c+1
    ls.append(ls1)
    dic[i]=ls[i]
    i=i+1
print(dic)
'''
print("Q 4")
d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
d3={}
ls=[]
z=zip(d1,d2)
for i,j in z:
        if i==j:
            d3[i]=d1[i]+d2[j]
        else:
            d3[i]=d1[i]
            d3[j]=d2[j]
            
print(d3)
   

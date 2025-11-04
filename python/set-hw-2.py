'''
# Q 1
set={12,34,35,'name','l',12,'name','kvpy','ser',3}
print(set)
# a
print(" A :")
for v in set:
    print(v,end="\t")
print("\n")
# b
print(" B :")
set.add('s')
print(set)

# c
print(" C :")
set.remove('s')
print(set)

# d
print(" D :")
set.discard('name')
print(" 'name' removed :",set)
set.discard('y')
print(" 'y' removed :",set)

# e
print(" E :")
print("length of set :",len(set))

# f
print(" F :")
set1={8,90,34,2,0,89}
print(set1)
m=min(set1)
print("smallest element ",m)
n=max(set1)
print("largest element ",n)

# g
print(" G :")
set1.clear()
print(set1)

# h
print(" H :")
print(set)
d=35 in set
print('is 35 in the set ',d)
d=40 in set
print('is 40 in a set ',d)

'''

# Q 2
s1={45,77,30,30,51,22}
s2={45,77,30,55,89,21,34}
print(s1,s2)

s3=s1.difference(s2)
print("s1-s2 difference :",s3)
s3=s2.difference(s1)
print("s2-s1 difference :",s3)

s3=s2.symmetric_difference(s1)
print("symmetric difference btween s1 and s2",s3)

s3=s1.intersection(s2)
print("commen element ",s3)

s3=s1.difference(s2)
print("A-B :",s3)

s=s1.isdisjoint(s2)
print("is s1 and s2 have commen elements or not :",s)

'''
set1={'mahabaleshwar','pune','mumbai','bangalore','chennai','vishakhapatnam','kochi'}
ls=[]
dic={}
print(set1)

k=max(set1)
print("largest element : ",k)

for i in set1:
    ls.append(len(i))
print("list : ",ls)

for i in set1:
    dic[i]=len(i)
print("updated dictinary : ",dic)
'''
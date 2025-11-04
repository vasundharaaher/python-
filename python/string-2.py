# Q1
'''
rt='computer'
print("Before :",rt)
yu=rt[len(rt)-1]+rt[1:len(rt)-1]+rt[0]
print("after :",yu)
'''
# Q2
'''
gh='566839028'
dic={}
for i in range(0,10):
    dic[i]=gh.count(str(i))  
print(dic)    
'''
# Q3
'''
def add_tags(s,d):
   e='<'+s+'>'+d+'</'+s+'>'
   return e 
hgj="python"
sd=add_tags('i',hgj)
print(sd) 
'''
# Q4
'''
def multipl_copy(l):
    asd=l*4
    return asd
qwe='vasundhara'
p=multipl_copy(qwe[-2::1])
print(p)
'''

# Q5
sd=input()
i=0
c=0
f=''
while i<len(sd):
    if sd[i].isalpha() and c<2:
        s=ord(sd[i])-32
        f=f+chr(s)
        c=c+1
    elif sd[i].isalpha():
        s=ord(sd[i])
        f=f+chr(s)
        c=c+1
    elif sd[i].isascii():
        s=ord(sd[i])
        f=f+chr(s)
    if c==4:
        c=0
    i=i+1
print(f)






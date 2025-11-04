# to creat file and print simple msg
'''f=open("first.txt","w")
f.write("hello")
f.write("hey .....!!!!")
f.close()
'''
'''
sd=open("first.txt","a")
sd.write("\nvasu\nabcd\nmnr\n")
sd.close()
'''
'''
df=open("first.txt","r")
d=df.readlines()
s=len(d)
print(s)
df.close()
'''
'''
c=0
fobj=open("first.txt","r")
for oneline in fobj:
    c=c+1
print(c)
fobj.close()
'''
'''
fobj=open("first.txt","r")
p=fobj.readlines()
i=0
while i<len(p):
    print(p[i])
    i=i+2
''' 
'''
fobj=open("first.txt","r")   
sd=open("secd.txt","w")
s=fobj.read()
sd.write(s)
fobj.close()
sd.close()   
   '''
'''

fobj=open("first.txt","r")   
sd=open("secd.txt","w")

    s=fobj.read()
    a=s.upper()
    sd.write(a)

for one in fobj:
    s=one.upper()
    sd.write(s)
fobj.close()
sd.close()
'''
fobj=open("first.txt","r")  
s=fobj.read()
a=s.upper()
fobj.close()
sd=open("first.txt","w")
sd.write(a)
sd.close()










# Q1
'''
str1="length"
print("stringn is ",str1,"length is",len(str1))
'''
# Q2
'''
str2="google.com"
i=0
dic={}
for i in str2:
    dic[i]=str2.count(i)
print(dic)
'''
# Q3
'''
str3="th"
d=len(str3)
if d>2:
    sr=str3[0]+str3[1]+str3[d-2]+str3[d-1]
    print(sr)
elif d==2:
    sr=2*(str3[0:2])
    print(sr)
else:
    print("string is empty...!!")
'''
# Q4
'''
str1='you are'
print(str1)
a=str1.index(' ')
str2=str1[:a]
str3=str1[a+1:]
print("first string : ",str2)
print("second string : ",str3)
'''
# Q5
'''
s='restart'
d=s[0]+s[1:].replace(s[0],'$')
print(d)
'''

# Q6
'''
s='askl'
print("given string : ",s)
if len(s)<3:
    print(s)
else:
    if s.endswith('ing'):
        s=s+'ly'
        print("ING was present at the end ",s)
    else:
        s=s+'ing'
        print("ING was not present at end : ",s)
'''







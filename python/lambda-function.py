# Q1
'''
fun=lambda a : a+15
print(type(fun))
print(fun(3))
'''

# Q3
'''
def even(k):
    if k%2==0:
        return k
def odd(k):
    if k%2!=0:
        return k
ls=[1,2,3,4,5,6,7,8,9,10]
lk=list(map(even,ls[1:len(ls):2]))
print(lk)
lh=list(map(odd,ls[0:len(ls)-1:2]))
print(lh)
'''

# Q4
'''
sd=lambda a : a*a
gh=lambda a:sd(a)*a
ls=[1,2,3,4,5,6,7,8,9,10]
jk=list(map(sd,ls))
print(jk)
po=list(map(gh,ls))
print(po)
'''
# Q5
'''
lo="2020-01-15"
sd=lambda a :print() if a=='-'  else print(a,end='')
tuple(map(sd, lo))
'''
# Q6
from functools import reduce 
lk=lambda m,n:ls.append(n+m)
ls=[0]

d=1
print("Enter a no ")
s= int(input())
o=0
while o<=s:
    vb=list(reduce(lk, ls, d))
    o=o+1
print(vb)





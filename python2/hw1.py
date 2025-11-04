# problem 11
ls1 = ['abc', 'xyz', 'aba', '1221', 'xyyxz', 'AA']
c = 0
for e in ls1:
    if len(e) >= 3 and e[0] == e[len(e)-1]:
        c = c + 1
print(ls1)
print(c)

'''
# problem 10
ls = [5, 20, 15, 20, 25, 50, 20]
i = 0
while i < 5:        # After remove index no will get decrease 
    if ls[i]==20:
        l=ls[i]
        ls.remove(l)  
    i=i+1
print(ls)
'''
'''
# problem 9
ls1=['a','b',['c',['d','e',['f','g'],'k'],'i'],'m','n']
ls2=['h','i','j']
i=0
while i<3:
    ls1[2][1][2].append(ls2[i])
    i=i+1
print(ls1)
'''

'''
# problem 8
ls=[10,20,[300,400,[5000,6000],500],30,40]
ls[2][2].append(7000)
print(ls)

'''
'''
# problem 7
ls = ["Milk", " ", "Emma", "Kelly", " ", "Brad"]
i = 1
while i < 7:
    if i==1 or i==3 :
        ls.remove(ls[i])
    i=i+1
print(ls)
'''
'''
# problem 6
ls1=[10,20,30,40]
ls2=[100,200,300,400]
i=0
j=3
c=0
while i<4:
    while c<4:
        c=c+1
        print(ls1[i]," ",ls2[j])
        j=j-1
        i=i+1
'''
'''
# problem 5
ls1 = ["hello", "take"]
ls2 = ["dear", "sir"]
ls3 = []
i = 0
while i < 2:
    j = 0
    while j < 2:
        ls3.insert(i, ls1[i] + " " + ls2[j])
        j = j + 1
    i = i + 1
print(ls3)

'''
'''
# problem 4
ls = [1, 2, 3, 4, 5, 6, 7]
ls1 = []
i = 0
while i < 7:
    p=ls[i]**2
    ls1.insert(i,p)
    i = i + 1
print(ls1)
'''
'''
# problem 3
ls=["M","na","I","ke"]
ls1=["y","me","s","lly"]
ls2=[]
i=0
j=0
c=0
while c<4:
    if i==j:
        ls2.insert(c,ls[i]+ls1[j])
    j=j+1
    i=i+1
    c=c+1
print(ls2)
'''

'''#problem 2
ls=[5,10,15,20,25,50,20]
a=ls.index(20)
print(a)
ls[a]=200
print(ls)
'''

''' problem 1
ls=[100,200,300,400,500]
ls.reverse()
print(ls)
'''

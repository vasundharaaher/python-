import random
dic={'vasu':0,'tushar':0,'priti':0}
t=dic.keys()
ls=list(t)
print(ls)
ls1=[1,2,3,4,5,6,'out']
pl=1
s=0
while True:
    print('player',ls[pl-1],'press enter')
    input()
    a=random.choice(ls1)
    if a=='out':
        print("you are out...")
        dic[ls[pl-1]]=s
        print("player",ls[pl-1],"you score",s)
        pl=pl+1
        s=0
        if pl==4:
            break
    else:
        s=s+a
        print(a)
        
print('final score',dic)
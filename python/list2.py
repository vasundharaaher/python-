a = []
i = 0
num = 0
while i <= 9:
    j = 0
    a.append([])
    while j <= 1:
        a[i].append([])
        k = 0
        while k <= 4:
            num = num + 1
            a[i][j].append(num)
            k = k + 1
        j = j + 1
    i = i + 1
print(a)

'''a = []
i = 0
num = 1
while i <= 9:
    j = 1
    a.append([])
    while j <= 10:
        nu = num * j
        a[i].append(nu)
        j = j + 1
    num = num + 1
    i = i + 1
print(a)


# fist progrqm 
th = [[], [], []]
i = 0
a = 0
while i < 3:
    j = 1
    while j < 4:
        a = i * 3 + j
        th[i].append(a)
        j = j + 1
    i = i + 1
print(th)'''

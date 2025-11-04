import time
import random
st = time.perf_counter()
a = random.randint(1, 4)
b = random.randint(1, 4)
r_add = eval(str(a) + "+" + str(b))
r_sub = eval(str(a) + "-" + str(b))
r_mul = eval(str(a) + "*" + str(b))
print(a, " + ", b, " = ?")
add = int(input())
print(a, " - ", b, " = ?")
sub = int(input())
print(a, " * ", b, " = ?")
mul = int(input())
tm=time.perf_counter() - st
print(tm)
count = 0
if r_add == add:
    count = count + 1
if r_sub == sub:
    count = count + 1
if r_mul == mul:
    count = count + 1
print("you got ", count, "score out of 3")
tp = time.perf_counter()
a = random.randint(1, 4)
b = random.randint(1, 4)
r_add = eval(str(a) + "+" + str(b))
r_sub = eval(str(a) + "-" + str(b))
r_mul = eval(str(a) + "*" + str(b))
print(a, " + ", b, " = ?")
add = int(input())
print(a, " - ", b, " = ?")
sub = int(input())
print(a, " * ", b, " = ?")
mul = int(input())
to = time.perf_counter() - tp
print(to)
count2 = 0
if r_add == add:
    count2 = count2 + 1
if r_sub == sub:
    count2 = count2 + 1
if r_mul == mul:
    count2 = count2 + 1
print("you got ", count2, "score out of 3")
if count<count2:
    print("player 2 win....")
elif count>count2:
    print("player 1 win....")
elif count==count2:
    if to>tm:
        print("player 1 win....")
    if to<tm:
        print("player 2 win....")
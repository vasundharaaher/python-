import random

print("Enter your two value ")
a = random.randint(1, 4)
b = random.randint(1, 4)

print(a, " + ", b, " = ?")
add = int(input())
print(a, " - ", b, " = ?")
sub = int(input())
print(a, " * ", b, " = ?")
mul = int(input())
r_add = a + b
r_mul = a * b
r_sub = a - b
count = 0
if r_add == add:
    count = count + 1
if r_sub == sub:
    count = count + 1
if r_mul == mul:
    count = count + 1
print("you got ", count, "score out of 3")

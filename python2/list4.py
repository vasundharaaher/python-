import random

print("Do you want Upper case alphabet in password :")
a = input()
print("Do you want Lower case alphabet in password :")
d = input()
print("Do you want integer in password :")
b = input()
print("Do you want special character in password :")
c = input()
print("Choice password strength :")
print("1. weak\n2. medium\n3. strong")
ch = input()
print("Length of the password :")
le = int(input())
i = 0

# Every thing is yes
if a == "y" and b == "y" and c == "y" and d == "y" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        pas = chr(random.randint(0, 122))
        print(pas, end="")
        i = i + 1

# No lower case letters
if a == "y" and b == "y" and c == "y" and d == "n" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        pas = chr(random.randint(0, 96))
        print(pas, end="")
        i = i + 1

# No Special symbols
if a == "y" and b == "y" and c == "n" and d == "y" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        if i < le:
            pas = chr(random.randint(65, 90))
            print(pas, end="")
        i = i + 1
        if i < le:
            pas = chr(random.randint(97, 122))
            print(pas, end="")
        i = i + 1
        if i < le:
            pas = chr(random.randint(48, 57))
            print(pas, end="")
        i = i + 1

# No Integer / digits
if a == "y" and b == "n" and c == "y" and d == "y" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        if i < le:
            pas = chr(random.randint(58, 122))
            print(pas, end="")
        i = i + 1
        if i < le:
            pas = chr(random.randint(0, 47))
            print(pas, end="")
        i = i + 1

# No Upper case letters
if a == "n" and b == "y" and c == "y" and d == "y" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        if i < le:
            pas = chr(random.randint(0, 64))
            print(pas, end="")
        i = i + 1
        if i < le:
            pas = chr(random.randint(91, 122))
            print(pas, end="")
        i = i + 1

# No upper case and no integer
if a == "n" and b == "n" and c == "y" and d == "y" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        if i < le:
            pas = chr(random.randint(0, 47))
            print(pas, end="")
        i = i + 1
        if i < le:
            pas = chr(random.randint(91, 122))
            print(pas, end="")
        i = i + 1
        if i < le:
            pas = chr(random.randint(58, 64))
            print(pas, end="")
        i = i + 1

# no upper case and no special symbols
if a == "n" and b == "y" and c == "n" and d == "y" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        if i < le:
            pas = chr(random.randint(48, 57))
            print(pas, end="")
        i = i + 1
        if i < le:
            pas = chr(random.randint(91, 122))
            print(pas, end="")
        i = i + 1

# no upper case and no lower case
if a == "n" and b == "y" and c == "y" and d == "n" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        if i < le:
            pas = chr(random.randint(0, 64))
            print(pas, end="")
        i = i + 1
        if i < le:
            pas = chr(random.randint(91, 96))
            print(pas, end="")
        i = i + 1

# no  integer and no special symbol
if a == "y" and b == "n" and c == "n" and d == "y" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        if i < le:
            pas = chr(random.randint(65, 90))
            print(pas, end="")
        i = i + 1
        if i < le:
            pas = chr(random.randint(91, 122))
            print(pas, end="")
        i = i + 1

# no integer and no lower case
if a == "y" and b == "n" and c == "y" and d == "n" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        if i < le:
            pas = chr(random.randint(58, 96))
            print(pas, end="")
        i = i + 1
        if i < le:
            pas = chr(random.randint(10, 47))
            print(pas, end="")
        i = i + 1

# no special symbol and no lower case
if a == "y" and b == "y" and c == "n" and d == "n" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        if i < le:
            pas = chr(random.randint(64, 90))
            print(pas, end="")
        i = i + 1
        if i < le:
            pas = chr(random.randint(48, 57))
            print(pas, end="")
        i = i + 1

# no  integer no special symbols and no lower case
if a == "y" and b == "n" and c == "n" and d == "n" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        if i < le:
            pas = chr(random.randint(64, 90))
            print(pas, end="")
        i = i + 1

# no  upper case no special symbols and no lower case
if a == "n" and b == "y" and c == "n" and d == "n" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        if i < le:
            pas = chr(random.randint(48, 57))
            print(pas, end="")
        i = i + 1

# no  upper case no special symbols and no integer
if a == "n" and b == "n" and c == "n" and d == "y" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        if i < le:
            pas = chr(random.randint(97, 122))
            print(pas, end="")
        i=i+1

# no  upper case no lower case and no integer
if a == "n" and b == "n" and c == "y" and d == "n" and (ch == "3" or ch == "2" or ch == "1"):
    while i < le:
        if i < le:
            pas = chr(random.randint(0, 47))
            print(pas, end="")
        i=i+1
        if i < le:
            pas = chr(random.randint(58, 64))
            print(pas, end="")
        i=i+1
        if i < le:
            pas = chr(random.randint(91, 96))
            print(pas, end="")
        i=i+1


# Every thing is No
if a == "n" and b == "n" and c == "n":
    print("No any kind of password can be generated....!!!")

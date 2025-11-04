import random
'''
print("Enter your alphabet :")
ap = ord(input())
comp = random.randint(97, 122)
b = chr(comp)
print("Your choice :", chr(ap))
print("Computer's choice :",b)
if ap == comp:
    print("You win.....")
else:
    print("Computer win.....")
'''
print("Enter your alphabet :")
ap = ord(input())
comp = random.randint(97, 122)
b = chr(comp)
print("Your choice :", chr(ap),ap)
print("Computer's choice :",b,ord(b))
if ap==(comp-1) or ap==(comp+1) or ap==(comp+2) or ap==(comp-2):
    print("Nearly correct...")
if ap == comp:
    print("You win.....")
else:
    print("Computer win.....")
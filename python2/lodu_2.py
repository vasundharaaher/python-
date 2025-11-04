import random
# ludo with target
print("Enter Target :")
tg = int(input())
sum1 = 0
c1 = 0
c2 = 0
sum2 = 0
while True:
    print()
    print("your turn...Player 1", end="")
    input()
    p1 = random.randint(1, 6)
    print("player 1 you got ", p1)
    if sum1 + p1 <= tg:
        sum1 = sum1 + p1
        print("player 1 your sum :", sum1)
        c1 = c1 + 1
    else:
        print("You extend Target by ", sum1 + p1)
        c1 = c1 + 1
    if sum1 == tg:
        print("P1 win....")
        print("yoy complete your target in ", c1, " count")
        break

    print()

    print("your turn...Player 2", end="")
    input()
    p2 = random.randint(1, 6)
    print("player 2 you got ", p2)
    if sum2 + p2 <= tg:
        sum2 = sum2 + p2
        print("player 2 your sum ", sum2)
        c2 = c2 + 1
    else:
        print("You extend Target by ", sum2 + p2)
        c2 = c2 + 1
    if sum2 == tg:
        print("P2 win....")
        print("yoy complete your target in ", c2, " count")
        break

def showlist(a):
    i = 1
    while i <= 9:
        print(a[i - 1], end="  ")
        if i % 3 == 0:
            print()
        i = i + 1


def store(ele):
    ls1.append(ele)


def check(c):
    if c in ls1:
        print("This box Already occupied...!! ")
        showlist(ls)
        player2()

    else:
        ls[c - 1] = 'O'
        store(c)
        showlist(ls)


def check1(c):
    if c in ls1:
        print("This box Already occupied...!! ")
        showlist(ls)
        player1()

    else:
        ls[c - 1] = 'X'
        store(c)
        showlist(ls)


def check_winner():







def player1():
    print("player ", p_1, "select your box")
    ch = int(input())
    check1(ch)
    check_winner()


def player2():
    print("player ", p_2, "select your box")
    ch = int(input())
    check(ch)
    check_winner()


ls1 = []
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p_1, p_2 = 1, 2
showlist(ls)
while True:
    player1()
    player2()

import random

cls = [1, 2, 3, 4, 5, 6, 'no ball', 'wild ball', 'out']
score = []
player_num = 1

while player_num <= 2:
    score.append([])

    while True:
        print("player no", player_num, "press enter to play")
        input()
        s = random.choice(cls)
        if s == 'no ball' or s == 'wild ball':
            sc = 1
            score[player_num - 1].append(sc)
            print("player you play", s)
        elif s == 'out':
            print("player no", player_num, "out...!!")
            break
        else:
            score[player_num - 1].append(s)
            print("player no", player_num, "you score", s)
    player_num = player_num + 1

p_n = 1
while p_n <= 2:
    print("player no", p_n, "you score", sum(score[p_n-1]))
    p_n = p_n + 1

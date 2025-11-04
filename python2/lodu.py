import random

while True :

  print("Player 1",end="")
  input()
  p1=random.randint(1,6)
  print(p1)
  if p1==6:
    print("player 1 play again ")
    input()
    a=random.randint(1,6)
    print(a)
    if a==6:
      print("Player 1 win ")
      break
  print("Player 2",end="")
  input()
  p2=random.randint(1,6)
  print(p2)
  if p2==6:
    print("player 2 play again ")
    input()
    b=random.randint(1,6)
    print(b)
    if b==6:
      print("Player 2 win ")
      break
def draw_library():
    print("library is found")
    library()
    return

import turtle
import math
def library() :
  house=turtle.Turtle()
  house.pensize(3)
  house.speed(5)
  house.color("Blue")
  side = 150
  diag = math.sqrt(2*(side**2))

  for i in range(4):
    house.fd(side)
    house.lt(90)
  house.lt(90/2)
  moves = [(diag,90),(diag/2,90),(diag/2,90),(diag,90)]
  for (move,turn) in moves:
    house.fd(move)
    house.lt(turn)




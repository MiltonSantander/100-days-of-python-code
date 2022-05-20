# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# from turtle import Turtle, Screen
#
# goku = Turtle()
# print(goku)
# my_screen = Screen()
# print(my_screen.canvwidth)

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("pokemon", ["pikachu", "charizard", "ratatail"])
table.add_column("type", ["electric", "fire", "plant"])

print(table)
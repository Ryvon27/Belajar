# import turtle
# from turtle import Turtle,Screen

# yuyu = Turtle()
# print(yuyu)
# yuyu.shape("turtle")
# yuyu.color("Red")
# yuyu.forward(100)
# yuyu.left(100)
# yuyu.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Nama",["Najib", "Arel", "Irvan"])
table.add_column("TTL", ["Jakarta", "Tangsel", "Kalimantan Utara"])
table.align = "l"
print(table)
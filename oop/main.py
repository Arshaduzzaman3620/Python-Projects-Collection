# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokémon Name", ["Pikachu", "Squirtle", "Bulbasaur"])
table.add_column("Type", ["Fire", "Water", "Grass"])

table.align = "l"  # Left align the column names
print(table)

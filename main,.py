from turtle import Turtle, Screen

screen = Screen()

# Manually setting screen size
screen.setup(500, 500)

y_positions = [-70, -40, -10, 20, 50, 80]
colour = ["black", "green", "blue", "violet", "red", "grey"]

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle would win the race?")

for new_number in range(0, 6):
    race_turtles = Turtle(shape="turtle")
    race_turtles.color(colour[new_number])
    race_turtles.penup()
    race_turtles.goto(x=-230, y=y_positions[new_number])

screen.exitonclick()

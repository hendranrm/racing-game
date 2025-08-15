from turtle import Turtle, Screen
import random

screen = Screen()

# Manually setting screen size
screen.setup(500, 500)

# setting positions of racing turtles in y-coordinate
y_positions = [-70, -40, -10, 20, 50, 80]

# setting colors
colour = ["black", "green", "blue", "violet", "red", "grey"]

# user makes bet
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle would win the race?")

race_on = False

# storing all racing turtle objects
all_turtles = []

for new_number in range(0, 6):
    race_turtles = Turtle(shape="turtle")
    race_turtles.color(colour[new_number])
    race_turtles.penup()
    race_turtles.goto(x=-230, y=y_positions[new_number])
    all_turtles.append(race_turtles)
        
if user_bet:
    race_on = True
    
# logic to make turtles race
while race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 210:
            get_color = turtles.color()
            if get_color[0] == user_bet:
                print(f"Your bet was on point, {get_color[0]} turtle won!")
            else:
                print(f"You got it wrong this time, sorry. {get_color[0]} turtle won!")

            race_on = False
            
        velocity = random.randint(0, 10)
        turtles.forward(velocity)
        

screen.exitonclick()

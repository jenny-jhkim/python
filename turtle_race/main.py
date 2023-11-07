from turtle import Turtle, Screen
import random

game_start = False

screen = Screen()
screen.setup(500, 400)
screen.title("Turtle racing")
user_guess = screen.textinput("Guess the winner","Which tutle do you think will win? enter color string: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


#initial setting of turtles
for index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-235, -120+40*index)
    all_turtles.append(new_turtle)
    
if user_guess:
    game_start = True
    
#set random distance
def random_distance():
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            global game_start
            game_start = False
            print("Game over")
            winner_color = turtle.pencolor()
                        
            if winner_color == user_guess:
                print(f"You Win! The {winner_color} turtle is a winner")
            else:
                print(f"You lose! The {winner_color} turtle is a winner")
            
        distance = random.randint(0,10)
        turtle.forward(distance)
    
while game_start:
    random_distance()

screen.exitonclick()
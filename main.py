import turtle
from turtle import Turtle, Screen
import pandas as pd

# Constants
FONT = ("lobster", 8)


# Set the screen
screen = Screen()
screen.title("India State game")
screen.setup(width=505, height=590)
# screen.screensize(canvwidth=505, canvheight=590)

# Loading images
image = "Images\india_map.gif"
screen.addshape(image)

# Making turtle to display that image
image_display = Turtle()
image_display.shape(image)

# Getting the co-ordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# Read the data from the .csv file
states_data = pd.read_csv("Data\India States.csv")
# Get the state data
states = states_data["state"].to_list()

# Score Tracker
score = 0

# Loop key
game_is_on = True

# Update the states guessed
guessed_states = []

while len(states) < 30:
    answer = screen.textinput(
        title=f"{score}/29 Guess the State !", prompt="What's the state name?").title()
    if answer == "Exit":
        states_left = []
        for state in states:
            if state not in guessed_states:
                states_left.append(state)
        missing_data = pd.DataFrame(states_left)
        missing_data.to_csv("Export\States_left.csv")
        # with open("day 25\\India State Game\\States_left.csv", mode='a') as file:
        #     file.write(str(states_left))
        break
    if answer in states:
        score += 1
        guessed_states.append(answer)
        # get the correct state co-ordinates
        states_cordinate = states_data[states_data.state == answer]
        # Get state X & Y co-ordinate
        state_x = states_cordinate["x"]
        state_y = states_cordinate["y"]
        # Convert the Pandas Data series into int
        cord_x = int(state_x)
        cord_y = int(state_y)
        # Write the data onto map
        plotter = Turtle()
        plotter.penup()
        plotter.hideturtle()
        # Send the plotter to correct co-ordinates
        plotter.goto(x=cord_x, y=cord_y)
        # Write the state name
        plotter.write(arg=f"{answer}", align="center", font=FONT)

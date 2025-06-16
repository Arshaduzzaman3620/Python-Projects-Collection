import turtle
import pandas as pd

# Set up screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load the image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the CSV data
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    if answer_state is None or answer_state.title() == "Exit":
        break

    answer_state = answer_state.title()

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center", font=("Arial", 10, "normal"))

# Save missing states to a CSV
missing_states = [state for state in all_states if state not in guessed_states]
state_to_learn = pd.DataFrame(missing_states)
state_to_learn.to_csv("states_to_learn.csv")

screen.mainloop()

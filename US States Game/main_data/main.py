import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S Game")
image = "main_data/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()

states_df = pd.read_csv("main_data/50_states.csv")
states_name = states_df["state"] #Get the column which contains the name of the states

guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/{len(states_name)} Guess the state", prompt="What's another state's name?")
    user_answer = user_answer.title()

    if user_answer == "Exit":
        missing_states = []

        for state in states_name.values:
            if state in guessed_states:
                pass
            missing_states.append(state)

        new_data = pd.DataFrame(missing_states) #Create a new dataframa with the missing states data
        new_data.to_csv("main_data/missing_states.csv", index=False)
        break

    if user_answer in states_name.values:
        guessed_states.append(user_answer)
        row = states_df.loc[states_df["state"] == user_answer] #Locates the row which state is equal to the user's asnwer
        x = row["x"].values[0] #Get the value from the "x" of the row (.values[0] get the value itself, otherwise it will just get the index of the row)
        y = row["y"].values[0] #Same, but for "y"
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(x, y)
        pen.write(user_answer, align="center", font=('Arial', 10, "normal"))
    pass

print(missing_states)
screen.mainloop()


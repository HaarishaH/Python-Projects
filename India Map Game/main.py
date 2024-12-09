import turtle


screen=turtle.Screen()
screen.setup(600,600)
screen.title('Indian States')
image = 'indian_map.gif'
screen.addshape(image)
turtle.shape(image)

import pandas as pd
d = pd.read_csv('states_names.csv')
all_states = d['states'].tolist()

guessed_state =[]

while len(guessed_state) < 30:
    prompt = screen.textinput(f"{len(guessed_state)}/30 States correct ",'Whats another state name').title()

    if prompt =='Exit':
        break


    if prompt in all_states and prompt not in guessed_state:
        guessed_state.append(prompt)
        correctstate = turtle.Turtle()
        correctstate.hideturtle()
        correctstate.penup()
        answer = d[d.states == prompt]
        correctstate.goto(answer.x.item(),answer.y.item())
        correctstate.write(prompt)

missed_states = [state for state in all_states if state not in guessed_state]
missed_states.append(len(missed_states))


df = pd.DataFrame(missed_states, columns = ['states'])
df.to_csv('missed_states', index = False)



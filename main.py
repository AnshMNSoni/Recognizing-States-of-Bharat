import turtle
import pandas as pd

ALIGNMENT = 'Center'
FONT = ('Courier', 14, 'bold')

screen = turtle.Screen()
screen.title('Political Map of Bharat')
image = "./Recognizing-States-of-Bharat/image.gif"
screen.setup(1000, 1000)
screen.addshape(image)
turtle.shape(image)

score = 0
game_is_on = True
while game_is_on:
    new_Turtle  = turtle.Turtle()
    new_Turtle.hideturtle()
    user = screen.textinput(f'{score}/28 Guessed', 'Enter State Name:').title()
    data = pd.read_csv('./Recognizing-States-of-Bharat/states.csv')
    state_name = data['state']
    
    count = 0
    for name in state_name:
        if (user == name):
            score += 1
            x = data['x'][count]
            y = data['y'][count]
            new_Turtle.penup()
            new_Turtle.goto(x, y)
            new_Turtle.color('red')
            new_Turtle.write(name, font=FONT, align=ALIGNMENT)
        count += 1

screen.exitonclick()
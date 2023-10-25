import turtle as tl
from functools import partial
from random import randint


window = tl.Screen()
window.bgpic('background.gif')
window.addshape("apple.gif")

example_turtle = tl.Turtle()
keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num_apples = 5
list_apples = []

for apples in range(num_apples):
    list_apples.append(tl.Turtle())


for apple in list_apples:
    apple.shape("apple.gif")
    if apple.heading() != 270:
        apple.setheading(270)


def new_pos(active_apple):
    last_x,last_y = active_apple.pos()
    new_x,new_y = randint(0,200),randint(50,100)
    while abs(new_x - last_x) < 10:
        new_x = randint(0,200)
    while abs(new_y - last_y) < 10:
        new_y = randint(0,200)
    active_apple.goto(new_x,new_y)
    active_apple.showturtle()

def falling_apple(active_apple):
    active_apple.forward(100)
    active_apple.hideturtle()
    new_pos(active_apple)

def pressed():
  for i in keys:
    tl.onkey(partial(falling_apple,i),i)

# falling_apple()

tl.onkeypress(pressed)
tl.listen()
window.mainloop()
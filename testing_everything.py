import turtle as tl
from functools import partial
from random import randint


window = tl.Screen()
window.bgpic('background.gif')
window.addshape("apple.gif")


keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
using_keys = []

applesintree = {}
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
    new_x,new_y = randint(0,200),randint(50,120)
    while abs(new_x - last_x) < 20:
        new_x = randint(0,200)
    while abs(new_y - last_y) < 20:
        new_y = randint(0,200)
    active_apple.goto(new_x,new_y)
    
    


def falling_apple(active_apple,key):
    active_apple.forward(100)
    active_apple.hideturtle()
    active_apple.clear()

    applesintree.pop(key)

    

    

    new_pos(active_apple)

    index_letter = randint(0,(len(keys)- 1))
    if len(keys) > len(list_apples):
        applesintree[keys[index_letter]] = [active_apple]
    
        using_keys.append(keys[index_letter])
        active_apple.write(f"{keys[index_letter]}",False,"center",("Arial",20,"normal"))
        keys.remove(keys[index_letter])
        active_apple.showturtle()

# example_turtle.clear()
def key_pressed(key_pressed):
    # print(key_pressed)
    
    if key_pressed in applesintree:
        using_keys.remove(key_pressed)
        
        tl.onkey(None,key_pressed)
        print(key_pressed,applesintree[key_pressed])

        active_apple = applesintree[key_pressed][0]
        falling_apple(active_apple,key_pressed)


def pressed():
  for i in using_keys:
    tl.onkey(partial(key_pressed,i),i)

for apple in list_apples:
    print(apple)
    apple.up()
    index_letter = randint(0,(len(keys)- 1))
    new_pos(apple)
    applesintree[keys[index_letter]] = [apple]
    using_keys.append(keys[index_letter])
    apple.write(f"{keys[index_letter]}",False,"center",("Arial",20,"normal"))
    keys.remove(keys[index_letter])

tl.onkeypress(pressed)
tl.listen()
window.mainloop()
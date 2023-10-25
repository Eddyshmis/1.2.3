#   a123_apple_1.py
import turtle as trtl
from random import randint
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
print(apple.heading())


num_apples = 5
list_apples = []
for apples in range(num_apples):
  list_apples.append(trtl.Turtle())


if apple.heading() != 270:
  apple.setheading(270)

#-----functions-----

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  index_letter = randint(0,len(keys))
  active_apple.write(f"{keys[index_letter]}",False,"center",("Arial",20,"normal"))
  wn.update()

def drop_apple():
  apple.forward(100)
  # draw_apple(apple)







def pressed():
  for i in keys:
    trtl.onkey(drop_apple,i)
# given a turtle, set that turtle to be shaped by the image file


#-----function calls-----


for apple in list_apples:
  draw_apple(apple)
  if apple.heading() != 270:
    apple.setheading(270)

trtl.onkeypress(pressed)

trtl.listen()
wn.mainloop()
# Setup
import turtle as trtl
import random

trtl.colormode(255)

count = 0
Drawerfor = 15

drawer_turtle = [] # 0 is the drawer, 1 is the maze mover/runner

# Making Turtles
count = 0
while count < 2:
  Drawer = trtl.Turtle()
  drawer_turtle.append(Drawer)
  count = count + 1
  
# Setting Drawer Turtle
drawer_turtle[0].penup()
drawer_turtle[0].goto(0, 0)
drawer_turtle[0].pendown()
drawer_turtle[0].speed(0)

# Setting Door Width Value
door = 30

############## Definitions ##############
def draw_wall(length):
   # Draw a wall
   if length <= 45:
     drawer_turtle[0].forward(length)
  
   # Draw a wall with a door
   elif length > 45:
     r = random.randint(0, length - door)
     drawer_turtle[0].forward(r)
     drawer_turtle[0].penup()
     drawer_turtle[0].forward(door) 
     drawer_turtle[0].pendown()
     drawer_turtle[0].forward(length - (r + door))

   # Draw a wall with a door and barrier






# Drawing Randomized Maze
while count < 21:
  draw_wall(Drawerfor)
  drawer_turtle[0].left(90)
  Drawerfor = Drawerfor + 15
  count = count + 1


# Drawing Final Line of Maze and Exit
#drawer_turtle[0].left(90)
drawer_turtle[0].forward(Drawerfor - 30)
drawer_turtle[0].left(90)
drawer_turtle[0].forward(30)

drawer_turtle[0].hideturtle()


# Setting Player Turtle At Beginning
drawer_turtle[1].penup()
drawer_turtle[1].shape("turtle")
drawer_turtle[1].color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
drawer_turtle[1].right(180)
drawer_turtle[1].forward(3)
drawer_turtle[1].right(90)
drawer_turtle[1].forward(10)
drawer_turtle[1].left(90)

#moving and turning fucntion for
def turn_right():
 drawer_turtle[1].right(10)
def turn_left():
 drawer_turtle[1].left(10)
def forward():
 drawer_turtle[1].forward(10)
def backward():
 drawer_turtle[1].backward(10)

wn = trtl.Screen()

count = 1
#Movement controls for the maze player 100	
wn.onkeypress(turn_right, "d") 
wn.onkeypress(turn_left, "a") 
wn.onkeypress(forward, "w") 
wn.onkeypress(backward, "s")  

wn = trtl.Screen()
wn.listen()
wn.mainloop()

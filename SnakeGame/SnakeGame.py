''' Aditya Tiwari
    22/11/2021
    12:30pm '''

# snake Game using python



import turtle
import random
import time

delay=0.1
score=0
highestScore=0

# Snake-bodies
bodies=[]

#Getting a screen / canvas
s=turtle.Screen()
s.title("My Sname Game")
s.bgcolor("gray")
s.setup(width=600,height=600)


# Creating snake's head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"


# Snake's food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.fillcolor("yellow")
food.penup()
food.ht()
food.goto(0,200)
food.st()


#Score Board
sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("blue")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score:0 | highestScore:0")

def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def movestop():
    head.direction="stop"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
        

# Event handling - key mappings
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")


# Main loop
while True:
    s.update() #this is to update the screen
    # check collission with border
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)
        
    # check collission with food
    if head.distance(food)<20:
        #move the food to new random place
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        # increase the length of the snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("black")
        body.fillcolor("white")
        bodies.append(body)  # append new body everytime

        #increase the score
        score+=10

        #change delay
        delay=0.0001
        # update the heighestScore
        if score>highestScore:
            highestScore=score
        sb.clear()
        sb.write(f"Score: {score}     |     highestScore:{highestScore}")
    #move the snake bodies
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)

    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()
    
    # check collission with snake's body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()

            score=0
            delay=0.1

            #update the score board
            sb.clear()
            sb.write(f"Score:{score}    |     highestScore:{highestScore}")
    time.sleep(delay)
s.mainloop()

# The End

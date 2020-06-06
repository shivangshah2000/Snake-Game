import turtle
import os
import time
import random

wn=turtle.Screen()
wn.bgcolor("green")
wn.title("Snake Game")
wn.tracer(0)

pen=turtle.Turtle()
pen.penup()
pen.pensize(10)
pen.setposition(-255,-255)
pen.color("red")
pen.pendown()
pen.speed(0)

for i in range(0,4):
    pen.fd(510)
    pen.lt(90)

pen.hideturtle()


head=turtle.Turtle()
head.speed(0)
head.setheading(90)
head.shape("square")
head.penup()
head.goto(0,0)
head.color("black")
head.direction="stop"
head.showturtle()

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
x=random.randint(-240,240)
y=random.randint(-240,240)
food.penup()
food.shapesize(0.75,0.75)
food.setposition(x,y)
food.color("yellow")

body=[]

score=turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,280)
score.write("Score: 0 ", align="center", font=("Courier", 24, "normal"))

flag=0

def color_food():
    l=["yellow","red","blue","gold","black","navy","cyan","turquoise","white","brown","chocolate","darkgreen","orange","violet","maroon","magenta"]
    k=random.randint(0,len(l)-1)
    food.color(l[k])
    

def go_up():
    if head.direction !="down":
        head.direction="up"
def go_down():
    if head.direction !="up":
        head.direction="down"
def go_left():
    if head.direction !="right":
        head.direction="left"
def go_right():
    if head.direction !="left":
        head.direction="right"
    
delay=0.1

def move():
    global flag
    
    if head.direction=="up" :
        y=head.ycor()
        
        if y>=239:
            flag=1  
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        
        if y<=-239:
            flag=1
        head.sety(y-20)
    if head.direction=="left" :
        x=head.xcor()
        
        if x<=-239:
            flag=1
        head.setx(x-20)
    if head.direction=="right" :
        x=head.xcor()
        
        if x>=239:
            flag=1
        head.setx(x+20)
    
turtle.listen()
turtle.onkey(go_up,"Up")
turtle.onkey(go_down,"Down")
turtle.onkey(go_right,"Right")
turtle.onkey(go_left,"Left")

cnt=0
while True:
    wn.update() 
    if head.distance(food)<20:
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("grey")
        new_segment.shape("square")
        new_segment.penup()
        body.append(new_segment)
        cnt+=1
        if cnt%2==0:
            delay-=0.01
        x=random.randint(-240,240)
        y=random.randint(-240,240)
        food.goto(x,y)
        color_food()
        score.clear()
        score.write("Score: {} ".format(cnt), align="center", font=("Courier",24,"normal"))

    for i in range((len(body)-1),0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].setposition(x,y)

    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
    move()

    for i in body:
        if head.distance(i)<3:
            flag=1
    time.sleep(delay)
    if flag==1:
        print("Game Over "+ str(cnt))
        break
wn.mainloop()
    


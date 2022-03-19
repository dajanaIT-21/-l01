import turtle
import random

aken = turtle.Screen()
aken.setup(300,300)
aken.title("Harjutus01")

colors = ('black','blue','red','green')
turn = 0
spikes = 8
size = 10


for i in range(spikes):
    kk = turtle.Turtle()
    kk.color(random.choice(colors))
    kk.left(turn)
    kk.forward(100)
    turn+=45
    

turtle.exitonclick()
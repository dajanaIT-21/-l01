#3
import turtle


aken = turtle.Screen()
aken.setup(300,300)
aken.title("KT")
angle = 0
k1 = turtle.Turtle()



for i in range(3):
    k1.rt(angle)
    k1.forward(100)
    angle=120


    
    
turtle.exitonclick()

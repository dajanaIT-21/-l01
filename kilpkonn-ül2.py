import turtle
 

aken = turtle.Screen()
aken.setup(300,300)
 

t = turtle.Turtle()
for i in range(0,8):
    t.forward(100)
    t.right(144)
 




color = input("Sisesta värv mida soovid kasutada(inglise keeles): ")
lenght = int(input("Sisesta külje pikkus: "))



for i in range(1):
    kk = turtle.Turtle()
    kk.color(color)
    kk.forward(lenght)
    kk.left(120)
    kk.forward(lenght)
    kk.left(120)
    kk.forward(lenght)
    
turtle.exitonclick()

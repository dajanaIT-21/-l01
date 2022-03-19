from turtle import *
#ül nr11
ekraan = Screen()
ekraan.setup(width=750, height=500)
shape('turtle')


def kolmnurk(length=150):
    for i in range(3):
        forward(length)
        left(120)


for i in range(10):
    kolmnurk()
    right(36)
    speed(10)

done()
    
    

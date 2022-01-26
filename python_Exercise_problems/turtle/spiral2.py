#import turtle
import colorsys
import turtle 

#setup turtle pen
t=turtle.Pen()

#change the speed of the turtle
t.speed(10)

#changes the background color
turtle.bgcolor('black')

t.pensize(2)
n=36
h=0

#make spiral_web
for x in range(50):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.left(10)
    for j in range(5):
        t.forward(200)
        t.left(144)

turtle.done()


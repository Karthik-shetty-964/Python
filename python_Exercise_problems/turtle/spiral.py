#import turtle
import turtle 

#defining colors
colors=['red', 'yellow', 'green', 'purple','blue','orange']

#setup turtle pen
t=turtle.Pen()

#change the speed of the turtle
t.speed(10)

#changes the background color
turtle.bgcolor('black')

#make spiral_web
for x in range(200):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

turtle.done()


from setup.graph import *
penSize(1)
zero = (250, 300)
x = zero[0]
y = zero[1]

brushColor("yellow")
circle(x, y, 90) 
penSize(20)
line(x-50, y+50, x+50, y+50)
penSize(10)
line(x-80, y-80, x-15, y-35)
line(x+90, y-60, x+15, y-35)
penSize(1)
brushColor('red')
circle(x-40, y-30, 15)
circle(x+40, y-30, 11)
brushColor("black")
circle(x-40, y-30, 7)
circle(x+40, y-30, 5)


run()



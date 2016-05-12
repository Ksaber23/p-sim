from graphics import *
from time import sleep
import math

angle = input('Enter angle (0 - 90 degrees)')
power = input('Enter power (0 - 100)')

win = GraphWin("Window", 1000, 400)
pt = Point(5, 350)
pt.draw(win)

txt = Text(Point(25,50), "Launch")
txt1 = Text(Point(25,20), "3")
txt2 = Text(Point(25,30), "2")
txt3 = Text(Point(25,40), "1")

#win.getMouse()

txt1.draw(win)
#sleep(1)
txt2.draw(win)
#sleep(1)
txt3.draw(win)
#sleep(1)
txt.draw(win)



vY = 0
vX = 0
vel = 0

for x in range(0, 40):
	pt = Point(pt.x+(vX*.05), pt.y-(vY*.05))
	pt.draw(win)
	vX = vel * (math.cos(math.radians(angle)))
	vY = vel * (math.sin(math.radians(angle)))
	vel = vel + (power/33)
	sleep(0.05)
while (pt.y < 350):
	pt = Point(pt.x+(vX*.05), pt.y-(vY*0.05))
	pt.draw(win)
	vY = vY - (9.81*.05)
	sleep(0.05)

win.getMouse()
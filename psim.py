from graphics import *
from time import sleep
import math
from random import randint


targetX = randint(50,900)
targetY = 348
status = 0

vY = float(0)
vX = float(0)
vel = float(0)

win = GraphWin("Window", 1000, 400)
pt = Point(5, 350)
pt.draw(win)
box = Rectangle(Point(targetX-30,targetY-10),Point(targetX+30,targetY+10))
box.draw(win)

txt = Text(Point(25,50), "Launch")
txt1 = Text(Point(25,20), "3")
txt2 = Text(Point(25,30), "2")
txt3 = Text(Point(25,40), "1")
txtVel = Text(Point(70,70), "Velocity:" + str(vel))

#win.getMouse()
angle = input('Enter angle (0 - 90 degrees)')
power = input('Enter power (0 - 100)')
power = float(power)

txt1.draw(win)
sleep(.2)
txt1.undraw()
txt2.draw(win)
sleep(.2)
txt2.undraw()
txt3.draw(win)
sleep(.2)
txt.draw(win)

#sleeptime = .05
sleeptime = .035

for x in range(0, 40):
	pt = Point(pt.x+(vX*sleeptime), pt.y-(vY*sleeptime))
	pt.draw(win)
	vX = vel * (math.cos(math.radians(angle)))
	vY = vel * (math.sin(math.radians(angle)))
	velold = vel
	vel = vel + (power/33)
	if vel != velold:
		txtVel.undraw()
		txtVel = Text(Point(70,70), "Velocity:" + str(int(vel)))
		txtVel.draw(win)
	sleep(sleeptime)
velold = vel
while (pt.y < 350):
	pt = Point(pt.x+(vX*sleeptime), pt.y-(vY*sleeptime))
	pt.draw(win)
	vY = vY - (9.81*sleeptime)
	if (pt.x > box.p1.x) and  (pt.x < box.p2.x):
		if (pt.y > box.p1.y) and  (pt.y < box.p2.y):
			status = 1
	if vel != velold:
		txtVel.undraw()
		txtVel = Text(Point(70,70), "Velocity:" + str(int(vel)))
		txtVel.draw(win)
	sleep(sleeptime)
if status == 0:
	print "Loser"
else:
	print "Winner"
win.getMouse()
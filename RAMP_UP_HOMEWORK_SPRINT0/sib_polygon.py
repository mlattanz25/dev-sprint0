# Polygon excercise from Week 0

# Name: Michael Lattanzio


from TurtleWorld import * 

world = TurtleWorld()			
bob = Turtle()				



#Excersise 2: This is where you put code to move bob

#1.)
def square (t):
	for i in range(4):
		fd (t, 100)
		lt (t)

	square (bob)

#2.) 
def square (t, length):
    for i in range(4):
		fd (t, length)
		lt (t)
 	
 	square (bob, 50)

 #3:)
def polygon (t, n, length):
	angle = 360.0 / n
	for i in range(n):
		fd(t, length)
		lt(t, angle)

	polygon (bob, 8, 50)

#Excersise 3

#1)
def circle (t, r):
	circumference = 2 * math.pi * r
	n = 50
	length = circumference / n

	polygon (t, n, length)


#2)

def arc (t, r, angle)
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 
	step_length = arc_length / n
	step_angle = float(angle) / n

	for i in range(n):
		fd (t, step_length)
		lt (t, step_angle)

























wait_for_user()					

# Create a program that that draws a square, circle, and shape of your choosing!
# Initialize the turtle shape to be a turtle and the color to be green.
from turtle import * # And this is another

# Inputting here
# Processing here
# Outputting here

shape("turtle")
color("green")
speed(1)
setup(500,500) # Setup the turtle window size

# Create a circle that contains the following:
# 1. Fill color of your choosing
# 2. Pen Color in a contrasting color
# 3. Pen Size needs to be 10
# 4. Size needs to be 100 pixels
# 5. Drawn at 200, 100

# Move to points designated on rubric (200,100)
penup()
goto(200,100)

#Make the circle
pendown()
pensize(10)
pencolor("yellow")
fillcolor("purple")
begin_fill()
circle(100)
end_fill()

# Change the turtle to green again
color("green")

# Create a Square that contains the following:
# 1. Fill color of your choosing
# 2. Pen Color in a contrasting color
# 3. Pen Size needs to be 5
# 4. Size needs to be 200 pixels
# 5. Drawn at -200, -200

# Move to points designated on rubric
penup()
goto(-200,-200)

#Make the square
pendown()
pensize(5)
pencolor("red")
fillcolor("green")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

# Change the turtle to green again
color("green")

# Create a shape that isn't a square or circle and contains the following:
# 1. Different location from the others
# 2. Different fill color from the others
# 3. Different pen color from the others
# 4. Different pen size from the others
# 4. Size different from the others

# Move to random set of points
penup()
goto(300,-150)

# Create a triangle
pendown()
pensize(3)
pencolor("orange")
fillcolor("blue")
begin_fill()
left(90)
forward(175)
left(135)
forward(175)
left(45)
forward(175)
left(45)
forward(175)
left(135)
forward(250)
end_fill()

# Move turtle to (0,0)
penup()
goto(0,0)
left(90)

# Change the turtle to green again
color("green")

# This is here to keep the program open
done()
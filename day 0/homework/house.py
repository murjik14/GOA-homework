from turtle import *




speed(20)
width(7)
begin_fill()
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square


#door

forward(70)
color ("black")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
#roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#win N1

penup()
goto(30, 160)
pendown()

color("cyan")
begin_fill()
left(120)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()
#winN2

penup()
goto(170, 160)
pendown()

color("cyan")
begin_fill()
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

exitonclick()
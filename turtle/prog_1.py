import turtle

turtle.bgcolor("black")
turtle.speed(0)
step1 = 3
step2 = 0.6
step3 = 2.4
colors = ["red","orange","blue","cyan","green","yellow"]
for i in range(360):
    turtle.forward(i*3 / step1 + 1)
    
    turtle.left(360 / step1 + 1)
    if i % 2 != 0:
        turtle.right(360 / step1 + 1)
       
    turtle.pencolor(colors[i%6])
turtle.color("black")
turtle.goto(600, -260)


for i in range(108):
   turtle.forward(i*0.6 / step2 + 0.2)
   
   turtle.left(72 / step2 + 0.2)
   turtle.right(108 / step2 + 0.2)
   turtle.pencolor(colors[i%6])
turtle.color("black")
turtle.goto(-600, -260)
for i in range(108):
   turtle.forward(i*0.6 / step2 + 0.2)
   
   turtle.left(72 / step2 + 0.2)
   turtle.right(108 / step2 + 0.2)
   turtle.pencolor(colors[i%6])
turtle.color("black")   
turtle.goto(-600, 260)
for i in range(140):
    turtle.forward(i*2.4 / step3 + 0.3)
    turtle.left(140 / step3 + 0.3)
    turtle.pencolor(colors[i%6])
turtle.color("black")
turtle.goto(600, 260)
for i in range(140):
    turtle.forward(i*2.4 / step3 + 0.3)
    turtle.left(140 / step3 + 0.3)
    turtle.pencolor(colors[i%6])

    
   
turtle.done()
from turtle import *

t = Turtle()
t.speed(0)
t.color('black')
t.pensize(5)
t.shape('turtle')
t.screen.setup(1200, 1200)

# туловище

t.up()
t.left(90)
t.forward(300)
t.right(90)
t.down()
t.circle(-250)

# голова

t.circle(-180)

# глаза

t.up()
t.right(90)
t.forward(100)
t.right(90)
t.forward(60)
t.down()
t.circle(50)
t.up()
t.right(180)
t.forward(120)
t.down()
t.circle(-50)
t.up()
t.right(90)
t.forward(50)
t.right(90)
t.forward(15)
t.down()
t.begin_fill()
t.circle(15)
t.end_fill()
t.up()
t.forward(90)
t.down()
t.begin_fill()
t.circle(15)
t.end_fill()

# нос

t.up()
t.left(100)
t.forward(70)
t.left(80)
t.down()
t.begin_fill()
t.forward(60)
t.right(90)
t.circle(-30, 180)
t.end_fill()

# уши

t.up()
t.forward(220)
t.left(10)
t.down()
t.forward(170)
t.circle(40, 180)
t.forward(180)
t.up()
t.left(80)
t.forward(220)
t.left(90)
t.down()
t.forward(180)
t.circle(40, 180)
t.forward(160)

# лапы

t.up()
t.forward(500)
t.down()
t.begin_fill()
t.circle(70)
t.right(90)
t.up()
t.forward(60)
t.down()
t.right(90)
t.circle(70)
t.end_fill()



# Необходимо, чтобы окно не закрывалось само, а только по клику
t.screen.exitonclick()
t.screen.mainloop()

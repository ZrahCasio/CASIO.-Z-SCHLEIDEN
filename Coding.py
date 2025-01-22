

from turtle import*
bgcolor('black')
speed(0)
pensize(2)

for i in range(500):
    color('purple')
    up()
    goto(-8,25)
    forward(i)
    right(859)
    down()

    fillcolor('red')
    begin_fill()
    circle(15,320)
    end_fill()
    bk(1/2)
    rt(6)

done()
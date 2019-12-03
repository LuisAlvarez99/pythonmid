import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()
s.setup(width=1.0,height=1.0,startx=0,starty=0)
def main():
    t.hideturtle()
    t.speed("normal")
    s.bgcolor("blue")
    t.pu()
    t.setpos(-150, -50)
    t.write("""
    Midterm project
    Cancer Constellation
    Luis Alvarez
    """,font = ("Arial",46,"normal"))
    time.sleep(2)
    s.clearscreen()
    t.showturtle()
    draw()
    s.clearscreen()
    pic()

def pic():
    s.setup(width=.3, height=.6, startx=0, starty=0)
    s.bgpic("candraw.gif")


def draw():
    s.setup(width=.8, height=.7, startx=0, starty=0)
    t.speed("slow")
    t.color("white")
    s.bgpic('cancer.gif')
    t.pendown()
    t.goto(-80, 210)
    t.dot(7, 'white')
    t.goto(-68, 38)
    t.dot(7, 'white')
    t.goto(80, 210)
    t.dot(7, 'white')
    t.pu()
    t.goto(-68, 38)
    t.pd()
    t.goto(-70, -38)
    t.dot(7, 'white')
    t.write('this is one of our points')
    t.goto(-145, -168)
    t.dot(7, 'white')
    t.pu()
    t.goto(-70, -38)
    t.pd()
    t.goto(85, -245)
    t.dot(7, 'white')


main()

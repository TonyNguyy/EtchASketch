from turtle import Turtle, Screen

tony = Turtle()
screen = Screen()

def move_forward():
    tony.forward(10)

def move_back():
    tony.backward(10)

def move_clockwise():
    tony.right(10)

def move_counter():
    tony.left(10)

def clear():
    screen.clear()
    tony.penup()
    tony.home()
    tony.pendown()

screen.listen()
screen.onkey(key = "w", fun= move_forward)
screen.onkey(key="s", fun= move_back)
screen.onkey(key="d", fun= move_clockwise)
screen.onkey(key="a", fun= move_counter)
screen.onkey(key="c", fun= clear)


screen.exitonclick()
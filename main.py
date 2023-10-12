import turtle

drawing_board=turtle.Screen()
drawing_board.bgcolor("light blue")

drawing_board.title("Python Turtle")

turtle_instance=turtle.Turtle()

drawing_board.listen()

def turtle_forward():
    turtle_instance.forward(100)
drawing_board.onkey(fun=turtle_forward,key="space")

turtle.mainloop()
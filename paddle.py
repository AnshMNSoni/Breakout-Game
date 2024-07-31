from turtle import Turtle, Screen

POSITION = [(-60,-300), (-40,-300), (-20,-300), (0,-300)]

screen = Screen()


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_reflector()
        
        
    def create_reflector(self):
        screen.tracer(0)
        for seg in POSITION:
            new_turtle = Turtle('square')
            new_turtle.penup()
            new_turtle.color('white')  
            new_turtle.goto(seg)  
            self.segments.append(new_turtle)
        screen.update()
            
    
    def on_right(self):
        if self.segments[-1].xcor() < 470:
            for turtles in range(len(self.segments) - 1):
                x = self.segments[turtles + 1].xcor()
                y = self.segments[turtles + 1].ycor()
                self.segments[turtles].goto(x, y)
            self.segments[-1].fd(20)
            screen.update()
        
    
    def on_left(self):
        if self.segments[0].xcor() > -470:
            self.segments[0].setheading(180)
            for turtles in range(len(self.segments) - 1, 0, -1):
                x = self.segments[turtles - 1].xcor()
                y = self.segments[turtles - 1].ycor()
                self.segments[turtles].goto(x, y)
            self.segments[0].fd(20)
            self.segments[0].setheading(0)
            screen.update()
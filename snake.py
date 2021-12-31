from turtle import Turtle

class Snake:

    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        x = 0
        y = 0
        for _ in range(3):
            self.segments.append(Turtle("square"))
            self.segments[_].penup()
            self.segments[_].color("white")
            self.segments[_].setx(x)
            self.segments[_].sety(y)
            x -= 20
            # y-=20

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            position = (self.segments[index - 1].pos()[0], self.segments[index - 1].pos()[1])
            self.segments[index].goto(position)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() == 0:
            self.head.left(90)
        elif self.head.heading() == 180:
            self.head.right(90)

    def down(self):
        if self.segments[0].heading() == 0:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].left(90)

    def right(self):
        if self.segments[0].heading() == 90:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 270:
            self.segments[0].left(90)

    def left(self):
        if self.segments[0].heading() == 90:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 270:
            self.segments[0].right(90)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create()
        self.head = self.segments[0]
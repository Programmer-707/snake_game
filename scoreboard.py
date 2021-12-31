from turtle import Turtle
FONT = ("Courier", 14, "normal")
ALIGNMENT = "center"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.update_board()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def update_board(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score {self.high_score}", align=ALIGNMENT, font=FONT)


    def increase(self):
        self.score += 1
        self.update_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_board()
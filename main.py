from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

done = False
while not done:
    screen.update()
    time.sleep(0.2)
    snake.move()
# DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

# DETECT COLLISION WITH WALL
    if (snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280
        or snake.head.ycor() < -280):
        print("hit the wall")
        scoreboard.reset()
        snake.reset()

# DETECT COLLISION WITH WALL
    for index in range(1, len(snake.segments)):
        if snake.segments[index].position() == snake.head.position():
            print("eat itself")
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
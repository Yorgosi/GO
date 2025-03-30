score = 0
from turtle import *
class Sprite(Turtle):
    def __init__(self, x, y, step = 10, shape = 'circle', color = 'black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.step = step
        self.shape(shape)
        self.color(color)
    def move_up(self):
        self.goto(self.xcor(),self.ycor()+self.step)
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())
    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True
        else:
            return False
    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))
    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)
player = Sprite(0, -100, 10, 'circle', 'yellow')
point = Sprite(0, 150, 0, 'triangle', 'green')
enemy1 = Sprite(0, 120, 10, 'square', 'red')
enemy1.set_move(-200, 120, 200, 120)
enemy2 = Sprite(0, 90, 10, 'square', 'red')
enemy2.set_move(-200, 90, 200, 90)
enemy3 = Sprite(0, 1000, 10, 'square', 'red')
enemy3.set_move(-200, 1000, 200, 1000)
scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_down, 'Down')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
player.is_collide(point)
while score < 3:
    enemy1.make_step()
    enemy2.make_step()
    enemy3.make_step()
    if player.is_collide(point):
        score += 1
        player.goto(0, -100)
        enemy3.goto(0,80)
        enemy3.set_move(-200, 60, 200, 60)
    if player.is_collide(enemy1) or player.is_collide(enemy2) or player.is_collide(enemy3):
        score = 0
        player.goto(0, -100)
        enemy3.goto(0, 1000)
        enemy3.set_move(-200, 1000, 200, 1000)
    if score == 3:
        enemy1.hideturtle()
        enemy2.hideturtle()
        enemy3.hideturtle()
        point.hideturtle()
        player.goto(-100,0)
        player.color('green')
        player.write("Победа", font=("Verdana", 15, "normal"))
scr.mainloop()
exitonclick()

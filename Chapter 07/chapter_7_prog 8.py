#Step 1: Import the libraries
#### Developing Snake game in python
import turtle
import time
import random
import threading

#Step 2: Set the initial values
delay = 0.1
final = 0
# Score
flag = 0
score = 0
high_score = 0
a,b,n,m = 1000,1000,1000,1000
z,i,t,eat = 0,0,0,0

#Step 3: Set up the screen
ts = turtle.Screen()
ts.title("Snake Game")
ts.bgcolor("light green")
wid,hgt = 600,600
ts.setup(width=wid, height=hgt)
ts.tracer(0)  # Turns off the screen updates


#Step 4: Create snake head

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"
st = 1


#Step 5: Create snake food (round ball)

food_1 = turtle.Turtle()
food_1.speed(0)
food_1.shape("circle")
food_1.color("red")
food_1.penup()
food_1.goto(0, 100)
a1 = food_1.xcor()
b1 = food_1.ycor()

ff = 0
food_2 = turtle.Turtle()
food_2.speed(0)
food_2.shape("circle")
food_2.shapesize(2, 2, 1)
food_2.color("brown")
food_2.penup()
food_2.goto(1000, 1000)
segments = []

#Step 6: Create welcome screen
# Pen
load = turtle.Turtle()
load.speed(0)
load.shape("circle")
load.shapesize(0.2, 0.2, 1)
load.color("black")
load.penup()
load.goto(0, -25)

draw = turtle.Turtle()
draw.speed(0)
draw.shape("square")
draw.color("black")
draw.penup()
draw.hideturtle()
draw.goto(0, 0)
draw.write("welcome to my world!! \n            -Python", align="center", font=("Times New Roman", 24, "normal"))

time.sleep(1.5)
draw.clear()
load.goto(1000,1000)
draw.goto(0, 260)
draw.write("Score: 0  High Score: 0", align="center", font=("Times New Roman", 24, "normal"))


#Step 7: Write the functions to control the directions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def coll_border():
    global score, delay, head, z, final
    if head.xcor() > 280 or head.xcor() < -290 or head.ycor() > 260 or head.ycor() < -290:
        z = 1
        final = score
        score = 0

        # Reset the delay
        delay = 0.1


def coll_food():
    global delay, score, high_score, food_1, head, a, b, flag, i, m, n, t, eat, a1, b1

    for j in segments:
        if j.distance(a1, b1) < 5:
            j.shapesize(1.5, 1.5, 1)
            # j.color("black")
        else:
            j.shapesize(1, 1, 1)

    if head.distance(food_1) < 50 or head.distance(food_2) < 30:
        head.shapesize(1.5, 1.5, 1)
    else:
        head.shapesize(1, 1, 1)

    if head.distance(food_1) < 15:
        # Move the food to a random spot
        head.shapesize(1, 1, 1)
        a1 = food_1.xcor()
        b1 = food_1.ycor()
        a = random.randint(-280, 280)
        b = random.randint(-280, 220)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
    if flag != 1:
        ran = random.randint(1, 10)

        if i % ran == 0 and i % 70 == 0 and i != 0 and head.xcor() != 0:
            while True:
                m = random.randint(-280, 280)
                n = random.randint(-280, 220)
                if m != food_1.xcor() and n != food_1.ycor():
                    t = 1
                    flag = 1
                    break

    if flag == 1:
        if head.distance(food_2) < 25:
            # Move the food to a random spot
            flag = 0
            t = 0
            eat = 1
            # Shorten the delay
            delay -= 0.001

            # Increase the score
            score += 20

            if score > high_score:
                high_score = score


def coll_body():
    global z, score, delay, segments, final
    for segment in segments:
        if segment.distance(head) < 20:
            z = 1
            # Reset the score
            final = score
            score = 0
            # Reset the delay
            delay = 0.1


def do1():
    global z
    head.goto(0, 0)
    head.direction = "stop"
    # time.sleep(1)

    for i in segments:
        i.goto(1000, 1000)

    segments.clear()

    draw.clear()
    head.color("light blue")
    food_1.color("light blue")
    food_2.color("light blue")

    draw.goto(0, 0)
    ts.update()

    draw.write("Game Over!! \n Score:{}".format(final), align="center",
              font=("Times New Roman", 24, "normal"))
    time.sleep(1.5)
    food_1.goto(0, 100)

    head.color("black")
    food_1.color("red")
    food_2.color("brown")

    draw.goto(0, 260)
    # score = 0
    draw.clear()

    draw.write("Score: {}  High Score: {}".format(score, high_score), align="center",
              font=("Times New Roman", 24, "normal"))
    z = 0


def do2():
    global a, b, a1, b1

    # last.goto(a1, b1)
    food_1.goto(a, b + 1)

    # Add a segment
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("circle")
    new_segment.color("green")
    new_segment.penup()
    segments.append(new_segment)
    draw.clear()
    draw.write("Score: {}  High Score: {}".format(score, high_score), align="center",
              font=("Times New Roman", 24, "normal"))
    a,b = 1000,1000

# Keyboard bindings
ts.listen()
ts.onkeypress(go_up, "Up")
ts.onkeypress(go_down, "Down")
ts.onkeypress(go_left, "Left")
ts.onkeypress(go_right, "Right")

if __name__ == "__main__":
    while True:
        ts.update()

        t1 = threading.Thread(target=coll_border)
        t2 = threading.Thread(target=coll_food)
        t3 = threading.Thread(target=coll_body)
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
        if z == 1:
            do1()

        if a < wid:
            do2()

        if flag == 1:
            if m < hgt:
                food_2.goto(m, n)
                m = 1000
                n = 1000
            else:
                t = t + 1

            if t > 40:
                food_2.goto(1000, 1000)
                flag = 0
                t = 0
                draw.clear()
                draw.write("Score: {} High Score: {}".format(score, high_score), align="center",
                          font=("Times New Roman", 24, "normal"))
        if eat == 1:
            draw.clear()
            draw.write("Score: {} High Score: {}".format(score, high_score), align="center",
                      font=("Times New Roman", 24, "normal"))
            eat = 0
            food_2.goto(1000, 1000)

        if t != 0:
            draw.clear()
            if t:
                if ff == 0:
                    if st == 1:
                        food_2.shapesize(1.75, 1.75, 1)
                        st = 2
                    elif st == 2:
                        food_2.shapesize(1.5, 1.5, 1)
                        st = 3
                    else:
                        food_2.shapesize(1, 1, 1)
                        ff = 1
                else:
                    if st == 3:
                        food_2.shapesize(1.5, 1.5, 1)
                        st = 2
                    elif st == 2:
                        food_2.shapesize(1.75, 1.75, 1)
                        st = 1
                    else:
                        food_2.shapesize(2, 2, 2)
                        ff = 0

            draw.write("Score:{} HighScore:{} time:{}".format(score, high_score, 40 - t), align="center",
                      font=("Times New Roman", 24, "normal"))

        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()

            segments[index].goto(x, y)
            # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
            if segments[0].distance(a1, b1) < 5:
                segments[0].shapesize(1.5, 1.5, 1)
            else:
                segments[0].shapesize(1, 1, 1)

        move()
        i = i + 1
        time.sleep(delay)

ts.mainloop()
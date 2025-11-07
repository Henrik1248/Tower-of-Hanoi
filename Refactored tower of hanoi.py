import turtle
import time

#Game Setup

wn = turtle.Screen()
wn.setup(width = 1200,height=500)
wn.bgcolor("light blue")
wn.title("Tower of Hanoi Game!")
wn.update()

#Pen

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0,-200)
pen.color("black")
pen.write("Get all the disks to the pole on the other end in size order. Start when I say.(127 is the best score!).",align = "center",font = ("Courier",12,"normal"))


#Poles

pole1 = turtle.Turtle()
pole1.shape("square")
pole1.penup()
pole1.shapesize(stretch_len = 0.6,stretch_wid = 14)
pole1.color("brown")
pole1.goto(-300,0)

pole2 = turtle.Turtle()
pole2.shape("square")
pole2.penup()
pole2.shapesize(stretch_len = 0.6,stretch_wid = 14)
pole2.color("brown")
pole2.goto(0,0)

pole3 = turtle.Turtle()
pole3.shape("square")
pole3.penup()
pole3.shapesize(stretch_len = 0.6,stretch_wid = 14)
pole3.color("brown")
pole3.goto(300,0)

base = turtle.Turtle()
base.penup()
base.shape("square")
base.color("brown")
base.shapesize(stretch_len = 40,stretch_wid = 1)
base.goto(0,-150)

#Disks

x = 0.8

disk1 = turtle.Turtle()
disk1.penup()
disk1.shape("square")
disk1.color("black")
disk1.shapesize(stretch_wid = x,stretch_len = 3)
disk1.goto(-300,-10)


disk2 = turtle.Turtle()
disk2.penup()
disk2.shape("square")
disk2.color("white")
disk2.shapesize(stretch_wid = x,stretch_len = 4)
disk2.goto(-300,-30)

disk3 = turtle.Turtle()
disk3.penup()
disk3.shape("square")
disk3.color("white")
disk3.shapesize(stretch_wid = x,stretch_len = 5)
disk3.goto(-300,-50)

disk4 = turtle.Turtle()
disk4.penup()
disk4.shape("square")
disk4.color("white")
disk4.shapesize(stretch_wid = x,stretch_len = 6)
disk4.goto(-300,-70)

disk5 = turtle.Turtle()
disk5.penup()
disk5.shape("square")
disk5.color("white")
disk5.shapesize(stretch_wid = x,stretch_len = 7)
disk5.goto(-300,-90)

disk6 = turtle.Turtle()
disk6.penup()
disk6.shape("square")
disk6.color("white")
disk6.shapesize(stretch_wid = x,stretch_len = 8)
disk6.goto(-300,-110)

disk7 = turtle.Turtle()
disk7.penup()
disk7.shape("square")
disk7.color("black")
disk7.shapesize(stretch_wid = x,stretch_len = 9)
disk7.goto(-300,-130)

turns = turtle.Turtle()
turns.hideturtle()
turns.penup()
turns.goto(1000,0)

disks = [disk1, disk2, disk3, disk4, disk5, disk6, disk7]

pole1 = [disk7,disk6,disk5,disk4,disk3,disk2,disk1]
pole2 = []
pole3 = []

max1 = pole1[2]
max2 = 1000
max3 = 1000

up = turtle.Turtle()
up.penup()
up.hideturtle()
up.goto(0,1000)

p1height = turtle.Turtle()
p1height.penup()
p1height.hideturtle()
p1height.goto(1000,10)

p2height = turtle.Turtle()
p2height.penup()
p2height.hideturtle()
p2height.goto(1000,-130)

p3height = turtle.Turtle()
p3height.penup()
p3height.hideturtle()
p3height.goto(1000,-130)

#up 0 = down
#up 1 = up

#Actions

pencil = turtle.Turtle()
pencil.hideturtle()
pencil.penup()
pencil.goto(300,200)
pencil.color("black")
s = str(turns.ycor())
t = "Turns: " + s
pencil.write(t,align = "center",font = ("Courier",30,"normal"))
#Helpful info = {turtle.shapesize()[0,1 or 2] gives the width or length of the turtle, not sure which number(0,1, or 2 is for which one tho so just test for which is which)}

pen.goto(0,-232)
pen.write("Start now!",align = "center",font = ("Courier",15,"normal"))

def up1():
    if up.xcor()==0:
        x = -1
        for p in pole1:
            x+=1
        if x >= 0:
            pole1[x].goto(pole1[x].xcor(),170)
            pole1.remove(pole1[x])
            up.goto(1,1000)
            p1height.goto(1000,p1height.ycor()-20)

            
        else:
            print("Invalid Move")
    else:
        print("Invalid Move")


def up2():
    if up.xcor()==0:
        x = -1
        for p in pole2:
            x+=1
        if x >= 0:
            pole2[x].goto(pole2[x].xcor(),170)
            pole2.remove(pole2[x])
            up.goto(1,1000)
            p2height.goto(1000,p2height.ycor()-20)

            
        else:
            print("Invalid Move")
    else:
        print("Invalid Move")

def up3():
    if up.xcor()==0:
        x = -1
        for p in pole3:
            x+=1
        if x >= 0:
            pole3[x].goto(pole3[x].xcor(),170)
            pole3.remove(pole3[x])
            up.goto(1,1000)
            p3height.goto(1000,p3height.ycor()-20)
        else:
            print("Invalid Move")
    else:
        print("Invalid Move")
        

def move():
    if up.xcor()==1:
        for disk in disks:
            if disk.ycor() == 170:
                if disk.xcor() == -300:
                    disk.goto(0,170)
                elif disk.xcor() == 0:
                    disk.goto(300,170)
                else:
                    disk.goto(-300,170)
    else:
        print("Invalid Move")



i = 30
def down():
    if up.xcor() == 0:
        print("Invalid Move")
    elif up.xcor() == 1:
        for disk in disks:
            if disk.ycor() == 170:
                if disk.xcor() == -300:
                    x = -1
                    for p in pole1:
                        x+=1
                    if x == -1:
                        turns.goto(1000,turns.ycor()+1)
                        disk.goto(disk.xcor(),-130)
                        pole1.append(disk)
                        p1height.goto(1000,p1height.ycor()+20)
                        up.goto(0,1000)
                        pencil.clear()
                        pencil.goto(300,200)
                        s = str(turns.ycor())
                        t = "Turns: " + s
                        pencil.write(t,align = "center",font = ("Courier",i,"normal"))
                   
                    else:
                        if disk.shapesize()[1]<pole1[x].shapesize()[1]:
                            turns.goto(1000,turns.ycor()+1)
                            disk.goto(disk.xcor(),p1height.ycor())
                            pole1.append(disk)
                            up.goto(0,1000)
                            p1height.goto(1000,p1height.ycor()+20)
                            pencil.clear()
                            pencil.goto(300,200)
                            s = str(turns.ycor())
                            t = "Turns: " + s
                            pencil.write(t,align = "center",font = ("Courier",i,"normal"))


                        else:
                            print("Invalid Move")
                elif disk.xcor() == 0:
                    x = -1
                    for p in pole2:
                        x+=1
                    if x == -1:
                        turns.goto(1000,turns.ycor()+1)
                        disk.goto(disk.xcor(),-130)
                        pole2.append(disk)
                        p2height.goto(1000,p2height.ycor()+20)
                        up.goto(0,1000)
                        pencil.clear()
                        pencil.goto(300,200)
                        s = str(turns.ycor())
                        t = "Turns: " + s
                        pencil.write(t,align = "center",font = ("Courier",i,"normal"))
        
                    else:
                        if disk.shapesize()[1]<pole2[x].shapesize()[1]:
                            turns.goto(1000,turns.ycor()+1)
                            disk.goto(disk.xcor(),p2height.ycor())
                            pole2.append(disk)
                            up.goto(0,1000)
                            p2height.goto(1000,p2height.ycor()+20)
                            pencil.clear()
                            pencil.goto(300,200)
                            s = str(turns.ycor())
                            t = "Turns: " + s
                            pencil.write(t,align = "center",font = ("Courier",i,"normal"))


                        else:
                            print("Invalid Move")
                else:
                    x = -1
                    for p in pole3:
                        x+=1
                    if x == -1:
                        turns.goto(1000,turns.ycor()+1)
                        disk.goto(disk.xcor(),-130)
                        pole3.append(disk)
                        p3height.goto(1000,p3height.ycor()+20)
                        up.goto(0,1000)
                        pencil.clear()
                        pencil.goto(300,200)
                        s = str(turns.ycor())
                        t = "Turns: " + s
                        pencil.write(t,align = "center",font = ("Courier",i,"normal"))

                    else:
                        if disk.shapesize()[1]<pole3[x].shapesize()[1]:
                            turns.goto(1000,turns.ycor()+1)
                            disk.goto(disk.xcor(),p3height.ycor())
                            pole3.append(disk)
                            up.goto(0,1000)
                            p3height.goto(1000,p3height.ycor()+20)
                            pencil.clear()
                            pencil.goto(300,200)
                            s = str(turns.ycor())
                            t = "Turns: " + s
                            pencil.write(t,align = "center",font = ("Courier",i,"normal"))
               

                        else:
                            print("Invalid Move")
    if disk1.xcor() == 300 and disk1.ycor() == -10:
        wn.clear()
        wn.bgcolor("green")
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(0,0)
        pen.color("black")
        x = str(turns.ycor())
        z = "Congratulations, you completed it in: " + x + " turns!"
        pen.write(z,align = "center",font = ("Courier",25,"normal"))
        balluno = turtle.Turtle()
        balluno.penup()
        balluno.shape("circle")
        balluno.color("blue")
        balluno.goto(0,-150)

        balldos = turtle.Turtle()
        balldos.penup()
        balldos.shape("circle")
        balldos.color("blue")
        balldos.goto(0,150)

        ball3 = turtle.Turtle()
        ball3.penup()
        ball3.shape("circle")
        ball3.color("blue")
        ball3.goto(-300,-150)

        ball4 = turtle.Turtle()
        ball4.penup()
        ball4.shape("circle")
        ball4.color("blue")
        ball4.goto(-300,150)

        ball5 = turtle.Turtle()
        ball5.penup()
        ball5.shape("circle")
        ball5.color("blue")
        ball5.goto(300,-150)

        ball6 = turtle.Turtle()
        ball6.penup()
        ball6.shape("circle")
        ball6.color("blue")
        ball6.goto(300,150)

        x = 1
        z = -1
        for p in range(0,1000):
            wn.bgcolor("light green")
            wn.bgcolor("green")
            for d in range(0,55):
                balluno.shapesize(stretch_wid = x,stretch_len = x)
                balldos.shapesize(stretch_wid = x,stretch_len = x)
                ball3.shapesize(stretch_wid = x,stretch_len = x)
                ball4.shapesize(stretch_wid = x,stretch_len = x)
                ball5.shapesize(stretch_wid = x,stretch_len = x)
                ball6.shapesize(stretch_wid = x,stretch_len = x)
                time.sleep(0.01)
                wn.bgcolor("light green")
                time.sleep(0.01)
                wn.bgcolor("green")
                x+=0.2
                time.sleep(0.01)
            for d in range(0,55):
                balluno.shapesize(stretch_wid = x,stretch_len = x)
                balldos.shapesize(stretch_wid = x,stretch_len = x)
                ball3.shapesize(stretch_wid = x,stretch_len = x)
                ball4.shapesize(stretch_wid = x,stretch_len = x)
                ball5.shapesize(stretch_wid = x,stretch_len = x)
                ball6.shapesize(stretch_wid = x,stretch_len = x)
                time.sleep(0.01)
                wn.bgcolor("light green")
                time.sleep(0.01)
                wn.bgcolor("green")
                x -= 0.2
                time.sleep(0.001)
    
                        


#key presses

wn.listen()

wn.onkeypress(up1,"a")
wn.onkeypress(up2,"s")
wn.onkeypress(up3,"d")
wn.onkeypress(move,"space")
wn.onkeypress(down,"x")



turtle.done()

    




#
import intrographics

def press(key):
    if  key == "Up":
        bird.dy= -3 #bird.dy is a variable
    elif key == "Down":
        bird.dy = 3

def timer1():
    y = random.randint(-125,0) #to randomly vary the y 
    pipes = window.rectangle(550,y,100,250)
    pipes.fill("green")
    pipes.group("pipe")
    
    pipes= window.rectangle(550,y+400,100,250)
    pipes.fill("green")
    pipes.group("pipe")
    
def timer2():
    bird.move(0, bird.dy) #to create a smooth move.........bird.move is a function
    for pipes in window.all("pipe"):
        pipes.move(-3,0)
        if  pipes.left <= window.left:
            window.remove(pipes)
        elif bird.overlaps(pipes):
            text = window.text(bird.left, bird.top, "Game Over!")
            window.remove(bird)

window = intrographics.window(600,400)
box1= window.rectangle(180,0,20,20)
box2= window.rectangle(0,0,20,20)
bird.dy = 0
window.on_key_press(press)

window.on_timer(3000,timer1)
window.on_timer(30,timer2)
window.open() 
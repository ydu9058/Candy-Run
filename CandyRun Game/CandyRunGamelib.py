from gamelib import *

game = Game(800,600,"Candy Run")

bk = Image("bk.jpg",game)

bk.resizeTo(game.width, game.height)
game.setBackground(bk)

person = Animation("running.png",8,game,648/8,104,3)
    

while not game.over:
    game .processInput()
    game.scrollBackground("left",1)
    person.draw()
    person.move()

    if keys.Pressed[K_UP]:
        person.y -= 1
        
    if keys.Pressed[K_LEFT]:
        person.x -= 1
       

    if keys.Pressed[K_DOWN]:
        person.y -= -1

    if keys.Pressed[K_RIGHT]:
        person.x -= -1

    if person.isOffScreen("all"):
        game.over = True
        

    game.update(30)


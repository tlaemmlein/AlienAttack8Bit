# Run with: pgzrun Hallo.py

import pgzrun


WIDTH = 800
HEIGHT = 600
RED = 200, 0, 0
BOX = Rect((20, 20), (100, 100))

ship = Actor("ship")
ship.pos = 370,500

def draw():
    screen.clear()
    #screen.draw.circle((400, 300), 30, 'white')
    #screen.draw.rect(BOX, RED)
    ship.draw()
    #screen.blit('ship', (370, 500))

def update():
    if keyboard.left:
        #print("links")
        ship.x = ship.x - 5
        if (ship.x < 0):
            ship.x = 0
    elif keyboard.right:
        #print("rechts")
        ship.x = ship.x + 5
        if (ship.x > WIDTH):
            ship.x = WIDTH
    elif keyboard.up:
        print("Feuer")


pgzrun.go()

# def draw():
#     screen.draw.text("Hier ist Erik", topleft=(20, 10))
#     screen.draw.text("Aber hier ", topleft=(20, 30))

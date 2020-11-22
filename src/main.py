# Run with: pgzrun Hallo.py

import pgzrun


WIDTH = 1500
HEIGHT = 800
RED = 200, 0, 0
BOX = Rect((20, 20), (100, 100))

ship = Actor("ship")
ship.pos = 370,HEIGHT-(ship.height/2.0)

anzahl_aliens = 25
aliens=[]
alien_abstand = 60

for x in range(anzahl_aliens):
    alien = Actor("alien")
    alien.pos = (30+alien_abstand*x),30
    aliens.append(alien)


def draw():
    screen.clear()
    ship.draw()
    for x in range(anzahl_aliens):
        aliens[x].draw()


def update():
    if keyboard.left:
        #print("links")
        ship.x = ship.x - 4
        if (ship.x < 0):
            ship.x = 0
    elif keyboard.right:
        #print("rechts")
        ship.x = ship.x + 4
        if (ship.x > WIDTH):
            ship.x = WIDTH

def on_key_up(key):
    if key == keys.SPACE:
        print("Feuer")

pgzrun.go()

# def draw():
#     screen.draw.text("Hier ist Erik", topleft=(20, 10))
#     screen.draw.text("Aber hier ", topleft=(20, 30))

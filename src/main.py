# Run with: pgzrun Hallo.py

import pgzrun


# Globale Initianisierung
WIDTH = 1500
HEIGHT = 800
score = 0

ship = Actor("ship")
ship.pos = 370,HEIGHT-(ship.height/2.0)

anzahl_aliens = 25
aliens=[]
alien_abstand = 60

rockets=[]

for x in range(anzahl_aliens):
    alien = Actor("alien")
    alien.pos = (30+alien_abstand*x),30
    aliens.append(alien)

def bewege_rockets():
    print("bewege " + str(len(rockets)) + " rockets")
    for r in rockets:
        r.y = r.y - 5
    clock.schedule(bewege_rockets, 0.01)

clock.schedule(bewege_rockets, 0.01)

# Ende globale initializierung

def draw():
    global score
    screen.clear()
    ship.draw()
    for x in range(anzahl_aliens):
        aliens[x].draw()
    screen.draw.text("Punkte: " + str(score), color="yellow", topleft=(5, 1))
    
    for r in rockets:
        r.draw()     

def update():
    global score
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
    for r in rockets:
        for a in aliens:
            rocket_shoot_alien = r.colliderect(a)
            if rocket_shoot_alien:
                score =score + 1

def on_key_up(key):
    if key == keys.SPACE:
        rocket = Actor("rocket")
        rocket.pos = ship.x, ship.y -25
        rockets.append(rocket)
        print("Feuer")

pgzrun.go()

# Run with: pgzrun Hallo.py

import pgzrun


# Globale Initianisierung
WIDTH = 1500
HEIGHT = 600
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
    alien.status = 0
    aliens.append(alien)

def update_rockets():
    global rockets, score, aliens
    for r in rockets:
        r.y = r.y - 5
        if (r.y <0):
            r.status=1
            continue
        for a in aliens:
            rocket_shoot_alien = r.colliderect(a)
            if rocket_shoot_alien:
                r.status=1
                a.status = 1
                score =score + 1
    rockets = listCleanup(rockets)
    aliens = listCleanup(aliens)
    #print("Anzahl rockets: " + str(len(rockets)))

def listCleanup(l):
    newList = []
    for i in range(len(l)):
        if l[i].status == 0: newList.append(l[i])
    return newList

# Ende globale initializierung

def draw():
    global score, aliens
    screen.clear()
    ship.draw()
    for a in aliens:
        a.draw()
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
    update_rockets()            

def on_key_up(key):
    if key == keys.SPACE:
        rocket = Actor("laser")
        rocket.pos = ship.x, ship.y -25
        rocket.status = 0
        rockets.append(rocket)
        print("Feuer")

pgzrun.go()

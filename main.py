import pygame
import sys
import time

# Initialisierung von Pygame
pygame.init()

# Farben
schwarz = (0, 0, 0)
weiß = (255, 255, 255)

# Bildschirmgröße
breite, höhe = 1000, 600  # Vergrößerte Bildschirmgröße
bildschirm = pygame.display.set_mode((breite, höhe))
pygame.display.set_caption("Ping Pong Spiel")

# Schläger
schläger_breite, schläger_höhe = 15, 100
schläger1 = pygame.Rect(50, höhe // 2 - schläger_höhe // 2, schläger_breite, schläger_höhe)
schläger2 = pygame.Rect(breite - 50 - schläger_breite, höhe // 2 - schläger_höhe // 2, schläger_breite, schläger_höhe)

# Ball
ball = pygame.Rect(breite // 2 - 15, höhe // 2 - 15, 30, 30)
ball_speed = [11, 11]

# Spielgeschwindigkeit
geschwindigkeit = 9

# Startzeit
startzeit = time.time()

# Zähler für gewonnene Spiele
gewinnzähler_spieler1 = 0
gewinnzähler_spieler2 = 0

# Variable für die Geschwindigkeitsverdoppelung
geschwindigkeitsverdoppelung = False

# Hauptspiel-Schleife
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and schläger1.top > 0:
        schläger1.y -= geschwindigkeit
    if keys[pygame.K_s] and schläger1.bottom < höhe:
        schläger1.y += geschwindigkeit
    if keys[pygame.K_UP] and schläger2.top > 0:
        schläger2.y -= geschwindigkeit
    if keys[pygame.K_DOWN] and schläger2.bottom < höhe:
        schläger2.y += geschwindigkeit

    # Ballbewegung
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Kollision mit den Wänden
    if ball.top <= 0 or ball.bottom >= höhe:
        ball_speed[1] = -ball_speed[1]

    # Kollision mit den Schlägern
    if ball.colliderect(schläger1) or ball.colliderect(schläger2):
        ball_speed[0] = -ball_speed[0]

    # Ball zurücksetzen, wenn er das Spielfeld verlässt
    if ball.left <= 0:
        ball.x = breite // 2 - 15
        ball.y = höhe // 2 - 15
        print("Spieler 2 hat gewonnen!")
        gewinnzähler_spieler2 += 1
        if gewinnzähler_spieler2 == 3:
            print("Spieler 2 hat insgesamt dreimal gewonnen. Spiel beendet!")
            pygame.quit()
            sys.exit()

    elif ball.right >= breite:
        ball.x = breite // 2 - 15
        ball.y = höhe // 2 - 15
        print("Spieler 1 hat gewonnen!")
        gewinnzähler_spieler1 += 1
        if gewinnzähler_spieler1 == 3:
            print("Spieler 1 hat insgesamt dreimal gewonnen. Spiel beendet!")
            pygame.quit()
            sys.exit()

    # Zeit seit Spielstart
    vergangene_zeit = time.time() - startzeit

    # Geschwindigkeit erhöhen nach einer bestimmten Zeit
    if vergangene_zeit > 10 and not geschwindigkeitsverdoppelung:
        geschwindigkeit + 2
        geschwindigkeitsverdoppelung = True

    # Bildschirm leeren
    bildschirm.fill(schwarz)

    # Schläger und Ball zeichnen
    pygame.draw.rect(bildschirm, weiß, schläger1)
    pygame.draw.rect(bildschirm, weiß, schläger2)
    pygame.draw.ellipse(bildschirm, weiß, ball)

    # Bildschirm aktualisieren
    pygame.display.update()

    # Framerate einstellen
    pygame.time.Clock().tick(30)


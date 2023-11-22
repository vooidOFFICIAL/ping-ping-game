import pygame
import sys
import time

# Initialization of Pygame
pygame.init()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Screen size
width, height = 1000, 600  # Enlarged screen size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong Game")

# Paddles
paddle_width, paddle_height = 15, 100
paddle1 = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle2 = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Ball
ball = pygame.Rect(width // 2 - 15, height // 2 - 15, 30, 30)
ball_speed = [11, 11]

# Game speed
speed = 9

# Start time
start_time = time.time()

# Counter for won games
win_counter_player1 = 0
win_counter_player2 = 0

# Variable for speed doubling
speed_doubling = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= speed
    if keys[pygame.K_s] and paddle1.bottom < height:
        paddle1.y += speed
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= speed
    if keys[pygame.K_DOWN] and paddle2.bottom < height:
        paddle2.y += speed

    # Ball movement
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Collision with walls
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] = -ball_speed[1]

    # Collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] = -ball_speed[0]

    # Reset ball if it leaves the playing field
    if ball.left <= 0:
        ball.x = width // 2 - 15
        ball.y = height // 2 - 15
        print("Player 2 has won!")
        win_counter_player2 += 1
        if win_counter_player2 == 3:
            print("Player 2 has won three times in total. Game over!")
            pygame.quit()
            sys.exit()

    elif ball.right >= width:
        ball.x = width // 2 - 15
        ball.y = height // 2 - 15
        print("Player 1 has won!")
        win_counter_player1 += 1
        if win_counter_player1 == 3:
            print("Player 1 has won three times in total. Game over!")
            pygame.quit()
            sys.exit()

    # Time since the start of the game
    elapsed_time = time.time() - start_time

    # Increase speed after a certain time
    if elapsed_time > 10 and not speed_doubling:
        speed + 2
        speed_doubling = True

    # Clear the screen
    screen.fill(black)

    # Draw paddles and ball
    pygame.draw.rect(screen, white, paddle1)
    pygame.draw.rect(screen, white, paddle2)
    pygame.draw.ellipse(screen, white, ball)

    # Update the screen
    pygame.display.update()

    # Set the frame rate
    pygame.time.Clock().tick(30)

import math
import random

import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("space war")
background = pygame.image.load("space for war.jpg")
mixer.music.load("background.wav")
mixer.music.play(-5)
surface = pygame.image.load("ufo.png")
pygame.display.set_icon(surface)

score_value = 0
font = pygame.font.SysFont("resansbold.ttf", 30)
over_game = pygame.font.SysFont("resansbold.ttf", 60)
textX = 10
textY = 10


def game_over_text(x, y):
    game_over = font.render("GAME OVER " + str(score_value), True, (255, 255, 255))
    screen.blit(game_over, (x, y))


def show_score(x, y):
    score = over_game.render("score = " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


playerimg = pygame.image.load("arcade-game.png")
playerX = 370
playerY = 480
playerX_changed = 0

# multiple enemies
enemyimg = []
enemyX = []
enemyY = []
enemyX_changed = []
enemyY_changed = []
numb_of_enemies = 12

for i in range(numb_of_enemies):
    enemyimg.append(pygame.image.load("alien (3).png"))
    enemyX.append(random.randint(0, 730))
    enemyY.append(random.randint(50, 180))
    enemyX_changed.append(0.3)
    enemyY_changed.append(40)

bulletimg = pygame.image.load("bullet (1).png")
bulletX = 0
bulletY = 480
bulletX_changed = 0
bulletY_changed = 2
bullet_state = "ready"


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX - bulletX), 2) + math.pow((enemyY - bulletY), 2))
    if distance < 27:
        colusion_sound = mixer.Sound("explosion.wav")
        colusion_sound.play()
        return True
    else:
        return False


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (-3220, -2600))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_changed = -0.5
                # print("left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_changed = 0.5
                # print("right arrow is pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_changed = 0
                # print("key stroke is released")
    # player boundries to stay with in screen
    playerX += playerX_changed
    if playerX <= 0:
        playerX = 0
    elif playerX >= 740:
        playerX = 740
    # enemy move ment with in screen

    for i in range(numb_of_enemies):
        # game over text
        if enemyY[i] > 500:
            for i in range(numb_of_enemies):
                enemyY[i] = 2000
            game_over_text(200, 250)
            break

        enemyX[i] += enemyX_changed[i]
        if enemyX[i] <= 0:
            enemyX_changed[i] = 0.5
            enemyY[i] += enemyY_changed[i]
        elif enemyX[i] >= 740:
            enemyX_changed[i] = -0.5
            enemyY[i] += enemyY_changed[i]
        collusion = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collusion:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 730)
            enemyY[i] = random.randint(50, 180)

        enemy(enemyX[i], enemyY[i], i)
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_changed

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

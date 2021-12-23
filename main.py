import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("space war")
surface = pygame.image.load("ufo.png")
pygame.display.set_icon(surface)

playerimg = pygame.image.load("arcade-game.png")
playerX = 370
playerY = 480
playerX_changed = 0

enemyimg = pygame.image.load("alien (3).png")
enemyX = random.randint(0, 740)
enemyY = random.randint(0, 480)
enemyX_changed = 0

enemy1img = pygame.image.load("monster.png")
enemy1X = random.randint(0, 740)
enemy1Y = random.randint(0, 480)
enemy1X_changed = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def enemy1(x, y):
    screen.blit(enemy1img, (x, y))


running = True
while running:
    screen.fill((0, 0, 0))

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_changed = 0
                # print("key stroke is released")
    playerX += playerX_changed
    if playerX <= 0:
        playerX = 0
    elif playerX >= 740:
        playerX = 740
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    enemy1(enemy1X, enemy1Y)
    pygame.display.update()

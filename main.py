import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("space war")
background = pygame.image.load("space for war.jpg")
surface = pygame.image.load("ufo.png")
pygame.display.set_icon(surface)

playerimg = pygame.image.load("arcade-game.png")
playerX = 370
playerY = 480
playerX_changed = 0

enemyimg = pygame.image.load("alien (3).png")
enemyX = random.randint(0, 740)
enemyY = random.randint(0, 480)
enemyX_changed = 0.3
enemyY_changed = 40

enemy1img = pygame.image.load("monster.png")
enemy1X = random.randint(0, 740)
enemy1Y = random.randint(0, 480)
enemy1X_changed = 0.3
enemy1Y_changed = 70

bulletimg = pygame.image.load("bullet (1).png")
bulletX = 0
bulletY = 480
bulletX_changed = 0
bulletY_changed = 10
bullet_state = "ready"


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def enemy1(x, y):
    screen.blit(enemy1img, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+16, y+10))


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
                fire_bullet(playerX, bulletY)

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
    enemyX += enemyX_changed
    if enemyX <= 0:
        enemyX_changed = 0.3
        enemyY += enemyY_changed
    elif enemyX >= 740:
        enemyX_changed = -0.3
        enemyY += enemyY_changed
    enemy1X += enemy1X_changed
    if enemy1X <= 0:
        enemy1X_changed = 0.3
        enemy1Y += enemy1Y_changed
    elif enemy1X >= 740:
        enemy1X_changed = -0.3
        enemy1Y += enemy1Y_changed
    if bullet_state == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_changed

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    enemy1(enemy1X, enemy1Y)
    pygame.display.update()

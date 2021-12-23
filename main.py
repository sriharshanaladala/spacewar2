import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("space war")
background = pygame.image.load("space for war.jpg")
surface = pygame.image.load("ufo.png")
pygame.display.set_icon(surface)

score = 0

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
bulletY_changed = 5
bullet_state = "ready"


def is_collision1(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX-bulletX), 2) + math.pow((enemyY-bulletY), 2))
    if distance < 27:
        return True
    else:
        return False


def is_collision2(enemy1X, enemy1Y, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemy1X-bulletX), 2) + math.pow((enemy1Y-bulletY), 2))
    if distance < 27:
        return True
    else:
        return False


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
                if bullet_state == "ready":
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
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_changed

    collusion1 = is_collision1(enemyX, enemyY, bulletX, bulletY)
    if collusion1:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        enemyX = random.randint(0, 740)
        enemyY = random.randint(0, 480)
        print(score)
    collusion2 = is_collision2(enemy1X, enemy1Y, bulletX, bulletY)
    if collusion2:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        enemy1X = random.randint(0, 740)
        enemy1Y = random.randint(0, 480)
        print(score)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    enemy1(enemy1X, enemy1Y)
    pygame.display.update()

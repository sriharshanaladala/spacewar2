import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("space war")
surface = pygame.image.load("ufo.png")
pygame.display.set_icon(surface)

playerimg = pygame.image.load("arcade-game.png")
playerX = 370
playerY = 480
playerX_changed = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_changed = -0.1
                # print("left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_changed = 0.1
                # print("right arrow is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_changed = 0
                # print("key stroke is released")
    playerX += playerX_changed
    player(playerX, playerY)
    pygame.display.update()

import pygame

pygame.init()

window = pygame.display.set_mode((900, 700))
pygame.display.set_caption("My new game")

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

spaceship = pygame.image.load("icon.png")
spaceship_x = 200
spaceship_y = 300


def display_spaceship(x, y):
    window.blit(spaceship, (x, y))


bg = pygame.image.load("Background.jpg")

gameon = True
while gameon:
    window.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            spaceship_x -= 100
        if keys[pygame.K_RIGHT]:
            spaceship_x += 100
        if keys[pygame.K_UP]:
            spaceship_y -= 100
        if keys[pygame.K_DOWN]:
            spaceship_y += 100

        display_spaceship(spaceship_x, spaceship_y)
        pygame.display.update()

pygame.quit()

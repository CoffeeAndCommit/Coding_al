import pygame
import sys

pygame.init()

display = pygame.display.set_mode((400, 400), pygame.RESIZABLE)

display.fill((255, 255, 255))

GREEN = (0, 255, 0)

# Filled circle
pygame.draw.circle(display, GREEN, (300, 300), 50)

# Hollow circle (thickness = 3)
pygame.draw.circle(display, GREEN, (100, 100), 50, 3)

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            pygame.display.toggle_fullscreen()

pygame.quit()
sys.exit()
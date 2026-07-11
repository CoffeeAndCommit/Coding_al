import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

pygame.display.set_caption("Basic Pygame Intro!")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((173, 216, 230))
    pygame.display.flip()
    
    # Cap the frame rate at 60 FPS to prevent the CPU from freezing/locking up
    clock.tick(60)

pygame.quit()
sys.exit()
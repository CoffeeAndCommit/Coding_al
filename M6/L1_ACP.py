import pygame

# Initialize pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((800, 500))

# Set window title
pygame.display.set_caption("My First Game Screen")

# Colors
BLUE = (50, 150, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont("Arial", 40)

# Game loop
running = True
while running:
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(BLUE)

    # Add text
    text = font.render("My First Game Screen", True, WHITE)
    screen.blit(text, (220, 200))

    # Draw a rectangle
    pygame.draw.rect(screen, BLACK, (350, 300, 100, 60))

    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()
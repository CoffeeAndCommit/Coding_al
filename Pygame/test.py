import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Star")

# Colors
WHITE = (255, 255, 255)
BLUE = (30, 144, 255)
BROWN = (139, 69, 19)
YELLOW = (255, 215, 0)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 36)

# Basket settings
basket_width = 120
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 50
basket_speed = 8

# Star settings
star_radius = 15
star_x = random.randint(star_radius, WIDTH - star_radius)
star_y = 0
star_speed = 5

# Score
score = 0

# Clock
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)

    # ---------------- Events ----------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------------- Keyboard ----------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        basket_x -= basket_speed

    if keys[pygame.K_RIGHT]:
        basket_x += basket_speed

    # Keep basket inside window
    if basket_x < 0:
        basket_x = 0

    if basket_x > WIDTH - basket_width:
        basket_x = WIDTH - basket_width

    # ---------------- Move Star ----------------
    star_y += star_speed

    # Catch star
    basket_rect = pygame.Rect(
        basket_x,
        basket_y,
        basket_width,
        basket_height
    )

    star_rect = pygame.Rect(
        star_x - star_radius,
        star_y - star_radius,
        star_radius * 2,
        star_radius * 2
    )

    if basket_rect.colliderect(star_rect):
        score += 1
        star_x = random.randint(star_radius, WIDTH - star_radius)
        star_y = 0

    # Missed star
    if star_y > HEIGHT:
        star_x = random.randint(star_radius, WIDTH - star_radius)
        star_y = 0

    # ---------------- Draw ----------------
    screen.fill(BLUE)

    # Basket
    pygame.draw.rect(
        screen,
        BROWN,
        (basket_x, basket_y, basket_width, basket_height)
    )

    # Star (yellow circle)
    pygame.draw.circle(
        screen,
        YELLOW,
        (star_x, star_y),
        star_radius
    )

    # Score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (20, 20))

    # Update screen
    pygame.display.flip()

pygame.quit()
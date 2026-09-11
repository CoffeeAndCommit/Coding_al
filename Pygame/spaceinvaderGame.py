import pygame
import random
import math

# -------------------- Initialize --------------------
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

# -------------------- Colors --------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
BLUE = (50, 150, 255)

# -------------------- Player --------------------
player_width = 60
player_height = 20

player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 6

player_dx = 0

# -------------------- Bullet --------------------
bullet_width = 6
bullet_height = 18

bullet_x = 0
bullet_y = player_y
bullet_speed = 10
bullet_state = "ready"

# -------------------- Enemies --------------------
enemy_size = 40
enemy_speed = 3
enemy_drop = 40
num_enemies = 6

enemies = []

for i in range(num_enemies):
    enemies.append({
        "x": random.randint(50, WIDTH - 50),
        "y": random.randint(40, 150),
        "dx": enemy_speed
    })

# -------------------- Score --------------------
score = 0

font = pygame.font.SysFont("Arial", 30)
game_over_font = pygame.font.SysFont("Arial", 70)

# -------------------- Functions --------------------

def draw_player():
    pygame.draw.rect(
        screen,
        BLUE,
        (player_x, player_y, player_width, player_height)
    )


def draw_enemy(enemy):
    pygame.draw.circle(
        screen,
        RED,
        (enemy["x"], enemy["y"]),
        enemy_size // 2
    )


def fire_bullet(x, y):
    pygame.draw.rect(
        screen,
        YELLOW,
        (x + player_width // 2 - 3, y, bullet_width, bullet_height)
    )


def collision(ex, ey, bx, by):
    distance = math.hypot(ex - (bx + player_width // 2), ey - by)
    return distance < 30


def show_score():
    txt = font.render(f"Score : {score}", True, WHITE)
    screen.blit(txt, (10, 10))


def game_over():
    txt = game_over_font.render("GAME OVER", True, WHITE)
    screen.blit(txt, (150, HEIGHT // 2 - 50))


# -------------------- Main Loop --------------------
running = True

while running:

    clock.tick(60)

    screen.fill(BLACK)

    # -------- Events --------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player_dx = -player_speed

            if event.key == pygame.K_RIGHT:
                player_dx = player_speed

            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_state = "fire"
                bullet_x = player_x
                bullet_y = player_y

        if event.type == pygame.KEYUP:

            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_dx = 0

    # -------- Player --------
    player_x += player_dx

    if player_x < 0:
        player_x = 0

    if player_x > WIDTH - player_width:
        player_x = WIDTH - player_width

    # -------- Bullet --------
    if bullet_state == "fire":

        fire_bullet(bullet_x, bullet_y)

        bullet_y -= bullet_speed

        if bullet_y < 0:
            bullet_state = "ready"
            bullet_y = player_y

    # -------- Enemies --------
    game_is_over = False

    for enemy in enemies:

        enemy["x"] += enemy["dx"]

        if enemy["x"] <= 20:
            enemy["dx"] = enemy_speed
            enemy["y"] += enemy_drop

        if enemy["x"] >= WIDTH - 20:
            enemy["dx"] = -enemy_speed
            enemy["y"] += enemy_drop

        if enemy["y"] > player_y - 20:
            game_is_over = True

        if bullet_state == "fire":

            if collision(enemy["x"], enemy["y"], bullet_x, bullet_y):

                bullet_state = "ready"
                bullet_y = player_y

                score += 1

                enemy["x"] = random.randint(50, WIDTH - 50)
                enemy["y"] = random.randint(40, 150)

        draw_enemy(enemy)

    # -------- Draw --------
    draw_player()

    show_score()

    if game_is_over:
        game_over()

    pygame.display.update()

pygame.quit()
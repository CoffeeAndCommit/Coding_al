import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 600
GRID_SIZE = 20

GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
FPS = 5

# Colors
BLACK = (20, 20, 20)
GREEN = (0, 220, 0)
DARK_GREEN = (0, 150, 0)
RED = (220, 50, 50)
WHITE = (255, 255, 255)

font = pygame.font.SysFont(None, 36)


def random_food(snake):
    while True:
        pos = (
            random.randint(0, GRID_WIDTH - 1),
            random.randint(0, GRID_HEIGHT - 1),
        )
        if pos not in snake:
            return pos


def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def reset_game():
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = (1, 0)
    food = random_food(snake)
    score = 0
    return snake, direction, food, score


snake, direction, food, score = reset_game()
game_over = False

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:
                    snake, direction, food, score = reset_game()
                    game_over = False
            else:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

    if not game_over:
        head_x, head_y = snake[0]
        dx, dy = direction

        new_head = (head_x + dx, head_y + dy)

        # Collision with walls
        if (
            new_head[0] < 0
            or new_head[0] >= GRID_WIDTH
            or new_head[1] < 0
            or new_head[1] >= GRID_HEIGHT
        ):
            game_over = True

        # Collision with self
        elif new_head in snake:
            game_over = True

        else:
            snake.insert(0, new_head)

            if new_head == food:
                score += 1
                food = random_food(snake)

                # Increase speed every 5 points
                FPS = 10 + score // 5
            else:
                snake.pop()

    # Draw
    screen.fill(BLACK)

    # Draw snake
    for segment in snake:
        x = segment[0] * GRID_SIZE
        y = segment[1] * GRID_SIZE

        pygame.draw.rect(
            screen,
            GREEN,
            (x, y, GRID_SIZE, GRID_SIZE),
        )

        pygame.draw.rect(
            screen,
            DARK_GREEN,
            (x + 2, y + 2, GRID_SIZE - 4, GRID_SIZE - 4),
        )

    # Draw food
    fx = food[0] * GRID_SIZE
    fy = food[1] * GRID_SIZE

    pygame.draw.ellipse(
        screen,
        RED,
        (fx + 2, fy + 2, GRID_SIZE - 4, GRID_SIZE - 4),
    )

    draw_text(f"Score: {score}", WHITE, 10, 10)
    draw_text(f"Speed: {FPS}", WHITE, 420, 10)

    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        game_over_text = font.render("GAME OVER", True, RED)
        restart_text = font.render("Press R to Restart", True, WHITE)

        screen.blit(
            game_over_text,
            (
                WIDTH // 2 - game_over_text.get_width() // 2,
                HEIGHT // 2 - 40,
            ),
        )

        screen.blit(
            restart_text,
            (
                WIDTH // 2 - restart_text.get_width() // 2,
                HEIGHT // 2 + 10,
            ),
        )

    pygame.display.flip()

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 8
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // 3
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 100, 255)
RED = (255, 80, 80)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

player = "X"
game_over = False
winner = None

font = pygame.font.SysFont(None, 60)


def draw_lines():
    screen.fill(WHITE)

    # Vertical lines
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    # Horizontal lines
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
            center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2

            if board[row][col] == "O":
                pygame.draw.circle(screen, BLUE, (center_x, center_y), CIRCLE_RADIUS, CIRCLE_WIDTH)

            elif board[row][col] == "X":
                offset = SQUARE_SIZE // 4
                pygame.draw.line(
                    screen,
                    RED,
                    (center_x - offset, center_y - offset),
                    (center_x + offset, center_y + offset),
                    CROSS_WIDTH
                )
                pygame.draw.line(
                    screen,
                    RED,
                    (center_x + offset, center_y - offset),
                    (center_x - offset, center_y + offset),
                    CROSS_WIDTH
                )


def mark_square(row, col):
    global player

    if board[row][col] is None:
        board[row][col] = player
        if player == "X":
            player = "O"
        else:
            player = "X"


def check_winner():
    global game_over, winner

    # Check rows
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            winner = board[row][0]
            game_over = True
            return

    # Check columns
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            winner = board[0][col]
            game_over = True
            return

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winner = board[0][0]
        game_over = True
        return

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        winner = board[0][2]
        game_over = True
        return

    # Check draw
    full = True
    for row in board:
        for cell in row:
            if cell is None:
                full = False

    if full:
        winner = "Draw"
        game_over = True


def show_result():
    if winner == "Draw":
        text = font.render("Draw! Press R", True, BLACK)
    else:
        text = font.render(f"{winner} Wins! Press R", True, BLACK)

    screen.blit(text, (130, HEIGHT // 2 - 30))


def restart_game():
    global board, player, game_over, winner

    board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = "X"
    game_over = False
    winner = None
    draw_lines()


draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = event.pos

            clicked_row = mouse_y // SQUARE_SIZE
            clicked_col = mouse_x // SQUARE_SIZE

            if board[clicked_row][clicked_col] is None:
                mark_square(clicked_row, clicked_col)
                check_winner()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

    draw_lines()
    draw_figures()

    if game_over:
        show_result()

    pygame.display.update()
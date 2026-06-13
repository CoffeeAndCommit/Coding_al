import pygame
import sys
import random

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
pygame.display.set_caption("Tic-Tac-Toe vs Computer")

board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

human = "X"
computer = "O"
player = human

game_over = False
winner = None

font = pygame.font.SysFont(None, 60)


def draw_lines():
    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

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
                pygame.draw.line(screen, RED,
                                 (center_x - offset, center_y - offset),
                                 (center_x + offset, center_y + offset),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, RED,
                                 (center_x + offset, center_y - offset),
                                 (center_x - offset, center_y + offset),
                                 CROSS_WIDTH)


def check_winner():
    global game_over, winner

    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            winner = board[row][0]
            game_over = True
            return

    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            winner = board[0][col]
            game_over = True
            return

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winner = board[0][0]
        game_over = True
        return

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        winner = board[0][2]
        game_over = True
        return

    full = True
    for row in board:
        for cell in row:
            if cell is None:
                full = False

    if full:
        winner = "Draw"
        game_over = True


def computer_move():
    global player

    empty_squares = []

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                empty_squares.append((row, col))

    if empty_squares:
        row, col = random.choice(empty_squares)
        board[row][col] = computer

    player = human


def show_result():
    if winner == "Draw":
        text = font.render("Draw! Press R", True, BLACK)
    elif winner == human:
        text = font.render("You Win! Press R", True, BLACK)
    else:
        text = font.render("Computer Wins! Press R", True, BLACK)

    screen.blit(text, (90, HEIGHT // 2 - 30))


def restart_game():
    global board, player, game_over, winner

    board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = human
    game_over = False
    winner = None


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if player == human:
                mouse_x, mouse_y = event.pos
                clicked_row = mouse_y // SQUARE_SIZE
                clicked_col = mouse_x // SQUARE_SIZE

                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = human
                    check_winner()

                    if not game_over:
                        player = computer
                        computer_move()
                        check_winner()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

    draw_lines()
    draw_figures()

    if game_over:
        show_result()

    pygame.display.update()
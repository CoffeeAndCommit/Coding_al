import pygame

def main():
    # Initialize pygame
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Rectangle and Text Demo')

    # Define colors
    BACKGROUND = (30, 30, 30)   # dark gray
    RECT_COLOR = (0, 125, 255)   # blue-ish rectangle
    TEXT_COLOR = (255, 255, 255)  # white text

    # Font for rendering text
    font = pygame.font.SysFont('Arial', 28)
    text_surface = font.render('Hello Pygame!', True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))

    # Rectangle parameters
    rect = pygame.Rect(200, 200, 200, 100)  # x, y, width, height

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill background
        screen.fill(BACKGROUND)
        # Draw rectangle
        pygame.draw.rect(screen, RECT_COLOR, rect)
        # Blit text
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()

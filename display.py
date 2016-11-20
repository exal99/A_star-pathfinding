import pygame

pygame.init()

RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

GRID_HEIGT = 10
GRID_WIDTH = 10

def draw_grid(display):
    size = display.get_size()
    rect_size = (size[0] // GRID_WIDTH, size[1] // GRID_HEIGT)
    for x in range(rect_size[0], size[0], rect_size[0]):
        pygame.draw.line(display, WHITE, (x, 0), (x, size[1]))
    for y in range(rect_size[1], size[1], rect_size[1]):
        pygame.draw.line(display, WHITE, (0, y), (size[0], y))

def main():
    gameDisplay = pygame.display.set_mode((800,800))
    pygame.display.set_caption("A* pathfinding")
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_grid(gameDisplay)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()

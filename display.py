import pygame

pygame.init()

RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

GRID_HEIGT = 10
GRID_WIDTH = 10

def draw_grid(display, grid):
    size = display.get_size()
    rect_size = (size[0] // GRID_WIDTH, size[1] // GRID_HEIGT)
    for x in range(rect_size[0], size[0], rect_size[0]):
        pygame.draw.line(display, WHITE, (x, 0), (x, size[1]))
    for y in range(rect_size[1], size[1], rect_size[1]):
        pygame.draw.line(display, WHITE, (0, y), (size[0], y))
    for x, row in enumerate(grid):
        for y, pos in enumerate(row):
            rect = pygame.Rect(x * GRID_WIDTH + 2, y * GRID_WIDTH + 2, rect_size[0] - 2, rect_size[1] - 2)
            if not pos:
                pygame.draw.rect(display, RED, rect)
            else:
                pygame.draw.rect(display, GREEN, rect)

def draw(mouseDown, grid, pos):
    if mouseDown:
        x,y = pos
        gridX = x//GRID_WIDTH
        gridY = y//GRID_HEIGT
        grid[gridX][gridY] = not grid[gridX][gridY]
        

def main():
    gameDisplay = pygame.display.set_mode((800,800))
    pygame.display.set_caption("A* pathfinding")
    clock = pygame.time.Clock()
    running = True
    mouseDown = False
    grid = [[True for e in range(GRID_HEIGT)] for e in range(GRID_WIDTH)]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseDown = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouseDown = False
            if event.type == pygame.MOUSEMOTION:
                draw(mouseDown, grid, event.pos)
        draw_grid(gameDisplay, grid)
        pygame.display.update()
        clock.tick(6000)

if __name__ == '__main__':
    main()

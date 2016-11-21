import pygame
import functools
import pathfinding

pygame.init()

RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

GRID_HEIGT = 50
GRID_WIDTH = 50

DRAW_COLORS = {
    1: BLUE,
    2: WHITE,
    3: GREEN,
    4: RED,
    10: (255, 0, 255)
}

DEFAULT_GRID = 3

def numKey_pressed(num, *, current_pen, **kwargs):
    current_pen.clear()
    current_pen.append(num)
    print("Pen changed")

def startPathFind(*, grid, **kwargs):
    start_pos = (-1, -1)
    end_pos = (-1, -1)
    non_walkable = []
    for x, row in enumerate(grid):
        for y, pos in enumerate(row):
            if pos == 1 and start_pos == (-1, -1):
                start_pos = (x, y)
            if pos == 2 and end_pos == (-1, -1):
                end_pos = (x, y)
            if pos == 4:
                non_walkable.append((x, y))
    pathfind_grid = pathfinding.makeGrid(len(grid), len(grid[0]), non_walkable)
    pathfinding.pathfind(start_pos, end_pos, pathfind_grid)
    path = pathfinding.getPath(end_pos, pathfind_grid)
    for pos in path:
        grid[pos[0]][pos[1]] = 10

def clear(*, grid, **kwargs):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y] = DEFAULT_GRID
    

BINDINGS = {
    48 + e: functools.partial(numKey_pressed, e) for e in range(10) #K_0 = 48, K_1 = 49 ... K_9 = 57
}
BINDINGS[pygame.K_RETURN] = startPathFind
BINDINGS[pygame.K_c] = clear

def draw_grid(display, grid, rect_size):
    size = display.get_size()
    
    for x in range(rect_size[0], size[0], rect_size[0]):
        pygame.draw.line(display, WHITE, (x, 0), (x, size[1]))
    for y in range(rect_size[1], size[1], rect_size[1]):
        pygame.draw.line(display, WHITE, (0, y), (size[0], y))
    for x, row in enumerate(grid):
        for y, pos in enumerate(row):
            rect = pygame.Rect(x * rect_size[0] + 1, y * rect_size[1] + 1, rect_size[0] - 2, rect_size[1] - 2)
            if pos in DRAW_COLORS:
                pygame.draw.rect(display, DRAW_COLORS[pos], rect)
            else:
                pygame.draw.rect(display, BLACK, rect)

def draw(mouseDown, grid, pos, rect_size, last_draw, pen):
    if mouseDown:
        x,y = pos
        gridX = x//rect_size[0]
        gridY = y//rect_size[1]
        if (gridX, gridY) != last_draw:
            grid[gridX][gridY] = pen[0]
            return gridX, gridY
    return last_draw


def keypressHandler(event, pen, grid):
    try:
        BINDINGS[event.key](current_pen = pen, grid = grid)
    except KeyError:
        return




def main():
    gameDisplay = pygame.display.set_mode((800,800))
    pygame.display.set_caption("A* pathfinding")
    clock = pygame.time.Clock()
    running = True
    mouseDown = False
    grid = [[DEFAULT_GRID for e in range(GRID_HEIGT)] for e in range(GRID_WIDTH)]
    size = gameDisplay.get_size()
    rect_size = (size[0] // GRID_WIDTH, size[1] // GRID_HEIGT)
    last_draw = (-1, -1)
    pen = [1]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseDown = True
                    draw(mouseDown, grid, event.pos, rect_size, last_draw, pen)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouseDown = False
            if event.type == pygame.MOUSEMOTION:
                last_draw = draw(mouseDown, grid, event.pos, rect_size, last_draw, pen)
            if event.type == pygame.KEYDOWN:
                keypressHandler(event, pen, grid)
        draw_grid(gameDisplay, grid, rect_size)
        pygame.display.update()
        clock.tick(6000)
        


if __name__ == '__main__':
    main()

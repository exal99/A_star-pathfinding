class Node:
    def __init__(self, gCost, hCost, parent, x, y, walkable = True):
        self.gCost = gCost #from start
        self.hCost = hCost #to finnish
        self.parent = parent
        self.walkable = walkable
        self.x = x
        self.y = y
        self._fCost = gCost + hCost
    
    @property
    def fCost(self):
        return self.hCost + self.gCost
    
    def __lt__(self, other):
        if isinstance(other, Node):
            return self.fCost < other.fCost or (self.fCost == other.fCost and self.hCost < other.hCost)
        else:
            return super().__lt__(other)
    
    def __hash__(self):
        return id(self)
    
    def __repr__(self):
        return str(self.__dict__)
    

def makeGrid(width, height, non_walkable):
    return [[Node(float('inf'), float('inf'), None, x, y, (x,y) not in non_walkable) for y in range(height)] for x in range(width)]

def getDist(fromPos, toPos):
    if isinstance(fromPos, Node) and isinstance(toPos, Node):
        deltaX = abs(fromPos.x - toPos.x)
        deltaY = abs(fromPos.y - toPos.y)
    else:
        deltaX = abs(fromPos[0] - toPos[0])
        deltaY = abs(fromPos[1] - toPos[1])
    return deltaX * 14 + 10 * (deltaY - deltaX) if deltaX < deltaY else deltaY * 14 + 10 * (deltaX - deltaY)

def pathfind(fromPos, toPos, grid):
    openSet = []
    closedSet = set()
    openSet.append(grid[fromPos[0]][fromPos[1]])
    grid[fromPos[0]][fromPos[1]].gCost = 0
    
    while True:
        current = getLowest(openSet)
        closedSet.add(openSet.pop(openSet.index(current)))
        
        if current == grid[toPos[0]][toPos[1]]:
            return True
        
        for neighbour in getNeighbour(current, grid):
            if neighbour in closedSet or not neighbour.walkable:
                continue
            newMovementCost = current.gCost + getDist(current, neighbour)
            if neighbour not in openSet or newMovementCost < neighbour.gCost:
                neighbour.gCost = newMovementCost
                neighbour.hCost = getDist((neighbour.x, neighbour.y), toPos)
                neighbour.parent = current
                if neighbour not in openSet:
                    openSet.append(neighbour)
            
def getPath(toPos, grid):
    path = []
    current = grid[toPos[0]][toPos[1]]
    while current is not None:
        path.append((current.x, current.y))
        current = current.parent
    return path


def getNeighbour(node, grid):
    width = len(grid)
    height = len(grid[0])
    for xOff in range(-1, 2):
        for yOff in range(-1, 2):
            if (xOff == 0 and yOff == 0) or node.x + xOff < 0 or  node.x + xOff >= width or node.y + yOff < 0 or node.y + yOff >= height:
                continue
            else:
                yield grid[node.x + xOff][node.y + yOff]

def getLowest(nodes):
    lowest = nodes[0]
    for node in nodes[1:]:
        if node < lowest:
            lowest = node
    return lowest
    

def make_node(fCost, hCost, parent, walkable):
    node = {"fCost": fCost,
            "hCost": hCost,
            "parent": parent,
            "walkable": walkable
    }
    node["gCost"] = getGCost(node)
    return node

def getGCost(node):
    return node["fCost"] + node["hCost"]


def updateHCost(node, newHCost):
    node["hCost"] = newHCost
    node["gCost"] = getGCost(node)

def updateFCost(node, newF):
    node["fCost"] = newF
    node["gCost"] = getGCost(node)

def updateParent(node, newPar):
    node["parent"] = newPar

def makeGrid(width, height, non_walkable):
    return [[make_node(float('inf'), float('inf'), None, (x,y) not in non_walkable) for y in range(height)] for x in range(width)]


def getDist(fromPos, toPos):
    deltaX = abs(fromPos[0] - toPos[0])
    deltaY = abs(fromPos[1] - toPos[1])
    return deltaX * 14 + 10 * (deltaY - deltaX) if deltaX < deltaY else deltaY * 14 + 10 * (deltaX - deltaY)

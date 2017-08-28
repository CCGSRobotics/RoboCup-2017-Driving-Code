from definintions import *
import time
from scipy.misc import imread

class orderSet(list):
    def __sub__(self, y):
        x = self
        for item in y:
            if item in x:
                x.remove(item)
        return x

def lookFor(value, pixel):
    # r = list(range(colour - 10, colour - 11))
    i = 0
    for p in pixel:
        if p != value:
            return False
        i += 1
        if i == 3: break
    return True

def lookForColour(value, index, pixel):
    return pixel[index] == value

class Reader(object):

    def __init__(self, filename):
        # self.file = open(filename)
        self.img = imread(filename)

    def generate_terrain(self):
        terrain = []
        start = (0,0)
        i = j = 0
        for row in self.img:
            terrain.append([])
            for pixel in row:
                if lookFor(0, pixel):
                    terrain[len(terrain)-1].append(1)
                elif lookFor(255, pixel):
                    terrain[len(terrain)-1].append(0)
                elif lookForColour(255, 1, pixel):
                    terrain[len(terrain)-1].append(2)
                elif lookForColour(255, 2, pixel):
                    terrain[len(terrain)-1].append(0)
                    self.start = (i,j)
                j += 1
            i += 1
            self.terrain = terrain
                                                   
        
    def create_adj_list(self):
        grid = self.terrain
        new = {}
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                adj = []
                def make_adj(a, b):
                    if a < 0 or b < 0:
                        return False
                    try:
                        if grid[a][b] == 0 or grid[a][b] == 2:
                            adj.append((a, b))
                    except:
                        pass
                # print(new)
                make_adj(x+1, y)
                make_adj(x-1, y)
                make_adj(x, y+1)
                make_adj(x, y-1)
                new[(x, y)] = orderSet(adj)
        self.adj_list = new

    def bfs(self, start=(0, 0)):
        grid = self.terrain
        visited, queue = orderSet(), [start]
        while queue:
            vertex = queue.pop(0)
            # print(visited, '>', vertex)
            if vertex not in visited:
                visited.append(vertex)
                if grid[vertex[0]][vertex[1]] == 2:
                    self.path = visited
                    return
                queue.extend(self.adj_list[vertex] - visited)

    def starting_direction(self, a, b):
        # Initialises a direction to begin the relay_action function
        if a[1] < b[1]:
            return 'east'
        elif a[0] < b[0]:
            return 'south'
        elif a[1] > b[1]:
            return 'west'
        elif a[0] > b[0]:
            return 'north'

    def relay_action(self):
        # Creates a list of directions to traverse the maze
        print(self.path)
        actions = []
        direction = self.starting_direction(self.path[0], self.path[1])
        for x in range(len(self.path)-1):
            a, b = self.path[x], self.path[x+1]
            xval1 = a[1]
            xval2 = b[1]
            yval1 = b[0]
            yval2 = a[0]
            if direction == "east":
                if xval1 > xval2:
                    actions.append("backward")
                elif xval2 > xval1:
                    actions.append("forward")
                elif yval1 > yval2:
                    actions.append("right")
                    actions.append("forward")
                    direction = "south"
                elif yval2 > yval1:
                    actions.append("left")
                    actions.append("forward")
                    direction = "north"
            elif direction == "south":
                if yval1 > yval2:
                    actions.append("forward")
                elif yval2 > yval1:
                    actions.append("backward")
                elif xval1 > xval2:
                    actions.append("right")
                    actions.append("forward")
                    direction = "west"
                elif xval2 > xval1:
                    actions.append("left")
                    actions.append("forward")
                    direction = "east"
            elif direction == "north":
                if yval1 < yval2:
                    actions.append("forward")
                elif yval2 < yval1:
                    actions.append("backward")
                elif xval1 < xval2:
                    actions.append("right")
                    actions.append("forward")
                    direction = "east"
                elif xval2 < xval1:
                    actions.append("left")
                    actions.append("forward")
                    direction = "west"
            elif direction == "west":
                if xval1 < xval2:
                    actions.append("backward")
                elif xval2 < xval1:
                    actions.append("forward")
                elif yval1 < yval2:
                    actions.append("right")
                    actions.append("forward")
                    direction = "north"
                elif yval2 < yval1:
                    actions.append("left")
                    actions.append("forward")
                    direction = "south"

            self.actions = actions

        def act(self):
        # Communicates with servos to traverse path in real life
            print(self.actions)
            for action in self.actions:
                if action == 'forward':
                    LWheels(200)
                    RWheels(-200)
                elif action == 'left':
                    RWheels(-360)
                    LWheels(0)
                elif action == 'right':
                    LWheels(360)
                    RWheels(0)
                elif action == 'backward':
                    LWheels(-200)
                    RWheels(200)
                time.sleep(3)
                LWheels(0)
                RWheels(0)


if __name__ == '__main__':
    f = Reader('Maze 1.png')
    # print(f.img)
    f.generate_terrain()
    # for i in f.terrain: print(i)
    f.create_adj_list()
    # for i in f.adj_list: print(i, ':',f.adj_list[i])
    f.bfs(start=(10, 0))
    f.relay_action()
    print(f.actions)

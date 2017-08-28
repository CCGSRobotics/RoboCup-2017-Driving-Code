# from emuBot import
from definintions import *
import time

class orderSet(list):
    def __sub__(self, y):
        x = self
        for a in y:
            if a in x:
                x.remove(a)
        return x

class Reader(object):
    def __init__(self, filename):
        # Initialises the file to be read and processed
        # Terminates class instance if file cannot be found
        self.filename = filename
        try:
            self.file = open(filename)
        except IOError:
            print('Given file not found.')
    '''            
    def __del__(self):
        # Deletes the instance and prints exit message
        print('Read Object was removed with name ' + self.filename)
    '''
    def process_file(self):
        self.terrain = None
        raise NotImplementedError

    def set_adj_list(self):
        # Creates an adjacency list to allow the BFS to work
        if self.terrain is None:
            raise NotImplementedError
        grid = self.terrain
        print()
        new = {}
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 0 or grid[x][y]==2:
                    c = []
                    def make_c(a, b):
                        if a < 0 or b < 0:
                            return False
                        try:
                            if grid[a][b] == 0 or grid[a][b]==2:
                                c.append((a,b))
                        except:
                            return False
                    make_c(x+1, y)
                    make_c(x-1, y)
                    make_c(x, y+1)
                    make_c(x, y-1)
                    new[(x,y)] = orderSet(c)
        for x in new: print(x)
        print()
        self.adj_list = new

    def bfs(self, start=(0,0)):
        # Finds a path through the maze
        grid = self.terrain
        visited, queue = orderSet(), [start]
        while queue:
            #print('a' + str(queue))
            vertex = queue.pop(0)
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
        print(self.actions)
        print(len(actions),len(self.path))

    def act(self):
        # Communicates with servos to traverse path in real life
        print(self.actions)
        for action in self.actions:
            if action == 'forward':
                LWheels(200)
                RWheels(-200)
            elif action == 'left':
                RWheels(-530)
                LWheels(0)
            elif action == 'right':
                LWheels(530)
                RWheels(0)
            elif action == 'backward':
                LWheels(-200)
                RWheels(200)
            time.sleep(3)
            LWheels(0)
            RWheels(0)

    
class ImageReader(Reader):
    def __init__(self, filename):
        from scipy.misc import imread
        self.img = imread(filename)
    '''
    def process_file(self):
        # Processes the image into a np.ndarray
        try:
            from scipy.misc import imread
        except ImportError:
            print('Module not installed on system.')
            self.__del__()
        self.terrain = imread(self.file)
    '''
    
    def look_rgb(self, val):
        # Returns a tuple of the co-ordinates of all pixels that
        # matches the rgb value given. Returns False if not found
        i = 0
        j = 0
        matches = []
        for row in self.process_file():
            for pixel in row:
                if list(pixel) == val:
                    matches.append((i, j))
                j += 1
            i += 1
        if matches:
            return matches
        return False

    def generate_terrain(self):
        terrain = []
        start = tuple()
        i = j = 0
        for row in self.img:
            terrain.append([])
            for pixel in row:
                # print(pixel)
                if ImageReader.look_colour(0, pixel):
                    # print('black')
                    terrain[len(terrain)-1].append(1)
                elif ImageReader.look_colour(255, pixel):
                    # print('white')
                    terrain[len(terrain)-1].append(0)
                elif ImageReader.look_colour2(255, 1, pixel):
                    # print('Green')
                    terrain[len(terrain)-1].append(2)
                elif ImageReader.look_colour2(255, 2, pixel):
                    # print('Blue')
                    terrain[len(terrain)-1].append(0)
                    start = (i,j)
                j += 1
            i += 1
        self.terrain = terrain
        return start

    @staticmethod
    def look_colour(colour, pixel):
        r = list(range(colour - 10, colour + 11))
        for p in pixel:
            if p not in r:
                return False
        return True
    @staticmethod
    def look_colour2(colour, index, pixel):
        r = list(range(colour - 10, colour + 11))
        return pixel[index] in r
                    

class FileReader(Reader):
    def process_file(self):
        self.terrain = [ [int(i) for i in line.strip()] for line in self.file ]
        print(self.terrain)

class TraverseFile:
    def __init__(self, m, start):
        maze = FileReader(m + '.txt')
        maze.process_file()
        maze.set_adj_list()
        maze.bfs(start=start)
        maze.relay_action()
        a = input('Are you sure you want to proceed? ')
        if a == 'yes':
            maze.act()

if __name__ == '__main__':
    # x = TraverseFile('maze', (0, 1))
    y = ImageReader('Maze 1.png')
    y.generate_terrain()
    y.set_adj_list()
    y.bfs(start=(10, 0))
    print(y.path)

    '''x = ImageReader('13x13.jpg')
    s = x.generate_terrain()
    #for i in x.terrain: print(i)
    x.set_adj_list()
    #print(x.adj_list)
    for i in x.adj_list: print(i)
    x.bfs(start=s)
    x.relay_action()
    x.act()
    '''

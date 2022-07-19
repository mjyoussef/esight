from PIL import Image
import numpy as np

def to_array(file):
    img = Image.open(file)
    return np.asarray(img)

def contrast(p1, p2):
    return (0.3 * p1[0] + 0.59 * p1[1] + 0.11 * p1[2]) \
        - (0.3 * p2[0] + 0.59 * p2[1] + 0.11 * p2[2])

def createEmptyMap(len, width, val):
    map = []
    for i in range(len):
        row = []
        for j in range(width):
            row.append(val)
        map.append(row)
    return map

class Parser:
    def __init__(self, image, base, border_color, threshold):
        self.image = to_array(image)
        self.base = to_array(base)
        self.visited = createEmptyMap(len(image), len(image[0]), False)
        self.border_color = border_color
        self.threshold = threshold
    
    def parse(self):
        for i in range(len(self.image)):
            for j in range(len(self.image[i])):
                if (not self.visited[i][j] and contrast(self.image[i][j], self.base[i][j]) >= self.threshold):
                    temp = createEmptyMap(len(self.image), len(self.image[0]), 0)
                    self.search(i, j, temp)

                    # find a convex hull over the border regions in temp
                    # update the image using the convex hull outline in temp


    def search(self, row, column, map):
        if map[row][column] == 0:
            if contrast(self.image[row][column], self.base[row][column]) >= self.threshold:
                map[row][column] = 1
                if row > 0:
                    self.search(row - 1, column, map)
                if row < len(self.image) - 1:
                    self.search(row + 1, column, map)
                if column > 0:
                    self.search(row, column - 1, map)
                if column < len(self.image[0]) - 1:
                    self.search(row, column + 1, map)
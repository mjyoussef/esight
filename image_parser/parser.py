from PIL import Image
import numpy as np
import initializer as init

class Parser:
    def __init__(self, image, base, border_color, threshold):
        self.image = image
        self.base = base
        self.annotated_img = init.initializeImg(image, base)
        self.border_color = border_color
        self.threshold = threshold
    
    def parse(self):
        for i in range(len(self.annotated_img)):
            for j in range(len(self.annotated_img[i])):
                if (self.annotated_img[i][j].contrast >= self.threshold):
                    self.search(i, j)

    def search(self, row, column):
        if self.annotated_img[row][column].seen:
            pass
        elif self.annotated_img.contrast >= self.threshold:
            if row != 0:
                self.search(row - 1, column)
            if row != len(self.annotated_img) - 1:
                self.search(row + 1, column)
            if column != 0:
                self.search(row, column - 1)
            if column != len(self.annotated_img[0]) - 1:
                self.search(row, column + 1)
        else:
            self.base[row][column] = self.border_color
        
        self.annotated_img[row][column].seen = True
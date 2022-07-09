from PIL import Image
import numpy as np

class Pixel:
    "stores the difference in pixel brightness"

    def __init__(self, b1, b2):
        self.contrast = b1 - b2
        self.seen = False

def initializeImg(file, base):
    "compares an image's brightness against that of a base image"
    img = Image.open(file)
    arr = np.asarray(img)

    output = []
    for i in range(len(arr)):
        row = []
        for j in arr[i]:
            b1 = 0.3 * arr[i][j][0] + 0.59 * arr[i][j][1] + 0.11 * arr[i][j][2]
            b2 = 0.3 * base[i][j][0] + 0.59 * base[i][j][1] + 0.11 * base[i][j][2]
            row.append(Pixel(b1, b2))
        output.append(row)
    return output
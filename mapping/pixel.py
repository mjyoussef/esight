from PIL import Image
import numpy as np

class Pixel:
    "stores the difference in pixel brightness"
    highlighters = {
        "green" : [0, 128, 0],
        "yellow": [255, 255, 0],
        "orange": [255, 165, 0],
        "red": [255, 0, 0]
    }

    def __init__(self, b1, b2):
        self.brightness = b1
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
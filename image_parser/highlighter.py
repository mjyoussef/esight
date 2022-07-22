def highlight(image, temp, color):
    min = len(temp[0])
    max = -1

    nw = len(temp[0])
    sw = -1

    ne = len(temp[0])
    se = -1

    prevLower = None
    prevUpper = None

    # fill in lower/upper boundary
    for col in range(len(temp[0])):
        for lower in range(len(temp)):
            if (temp[lower][col] == 1):
                image[lower][col] = color

                # make sure lower boundary is connected
                if (prevLower != None):
                    if (prevLower < lower):
                        for row in range(prevLower+1, lower):
                            image[row][col] = color
                    if (prevLower > lower):
                        for row in range(lower+1, prevLower):
                            image[row][col-1] = color
                prevLower = lower

                for upper in reversed(range(len(temp))):
                    if (temp[upper][col] == 1):
                        image[upper][col] = color
                        if (col < min):
                            min = col
                            nw = lower
                            sw = upper
                        if (col > max):
                            max = col
                            ne = lower
                            se = upper
                        
                        # make sure upper boundary is connected
                        if (prevUpper != None):
                            if (prevUpper < upper):
                                for row in range(prevUpper+1, upper):
                                    image[row][col-1] = color
                            if (prevUpper > upper):
                                for row in range(upper+1, prevUpper):
                                    image[row][col] = color
                        prevUpper = upper
                        break
                break

    # update west/east boundary
    for row in range(nw, sw+1):
        image[row][min] = color
    for row in range(ne, se+1):
        image[row][max] = color


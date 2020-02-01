import random
f = open ("pic.ppm", "w")

f.write ("P3 500 500 255")

color = [][]

def placecolors (size):
    red, green, blue
    for i in range (500):
        for j in range (500):
            if j < 500/3:
                red = 255
                green = Random.randint (256)
                blue = Random.randint (256)
            elif j < (500/3)*2:
                red = Random.randint (256)
                green = 255
                blue = Random.randint (256)
            else:
                red = Random.randint (256)
                green = Random.randint (256)
                blue = 255
        color [i][0] = red
        color [i][1] = green
        color [i][2] = blue
        f.write (red + " " + green + " " + blue)

f = open ("pic.ppm", "v")

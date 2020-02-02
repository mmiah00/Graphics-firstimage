import random
f = open ("pic.ppm", "w")

f.write ("P3 500 500 255")

color = []

def placecolors ():
    red, green, blue = 0,0,0
    for i in range (500):
        for j in range (500):
            if j < 500/3:
                red = 255
                green = random.randint (0,256)
                blue = random.randint (0,256)
            elif j < (500/3)*2:
                red = random.randint (0,256)
                green = 255
                blue = random.randint (0,256)
            else:
                red = random.randint (0,256)
                green = random.randint (0,256)
                blue = 255
        colors = [red, green, blue]
        color.append (colors)
        f.write (str (red) + " " + str (green) + " " + str (blue) + " ")

placecolors ()

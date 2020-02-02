import random
f = open ("pic.ppm", "w")

f.write ("P3 500 500 255 ")

color = []

# def placecolors ():
#     for i in range (500*500):
#         red = random.randint (1,255)
#         green = random.randint (1,255)
#         blue = random.randint (1,255)
#         f.write (str (red) + " " + str (green) + " " + str (blue) + " ")

colors = []

def placecolors ():
    for y in range (500):
        for x in range (500):
            if pow (y + 250, 2) - pow (x + 250, 2) == 10:
                color = [255, 0, 0]
                colors.append (color)
            else:
                color = [0, 255, 0]
                colors.append (color)

def toFile ():
    for i in range (len (colors)):
        f.write (str (colors[i][0]) + " " + str (colors[i][1]) + str (colors[i][2]) + " ")

placecolors ()
toFile ()

import random
f = open ("pic.ppm", "w")

f.write ("P3 500 500 255 ")

colors = []

def placecolors ():
    for i in range (500):
        for j in range (500):
            if pow (i - 250, 2) - pow (j - 250, 2) > 2500:
                f.write ("255 " + str (random.randint (0, 255)) + " " + str (random.randint (0,255)) + " ")
            else:
                f.write ("0 0 0 ")

placecolors ()
f.close ()

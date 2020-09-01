from setup.graph import *
def backgraundFunc(weight, height):
    n = 0
    for i in range(weight//25):
        line(25*n, 0, 25*n, height)
        n += 1
    n = 0
    for i in range(height//25):
        line(0, 25*n, weight, 25*n)
        n += 1


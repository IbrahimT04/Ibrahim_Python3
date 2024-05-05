import math
import time
from ctypes.wintypes import RGB
from math import sin, cos
from tkinter import *

nScreenWidth = 450
nScreenHeight = 300
nMapWidth = 16
nMapHeight = 16
edgeColor = "red"

fPlayerX = 8.00
fPlayerY = 8.00
fPlayerA = 0.0
fFOV = 3.14159 / 4.0
fDepth = 16.0
fSpeed = 1.0
elapsedTime = 0

g_map = "################"
g_map += "#..............#"
g_map += "#..............#"
g_map += "#..............#"
g_map += "#..######......#"
g_map += "#..............#"
g_map += "#..............#"
g_map += "#..............#"
g_map += "#..............#"
g_map += "#...####.......#"
g_map += "#..............#"
g_map += "#........###...#"
g_map += "#..............#"
g_map += "#.....####.....#"
g_map += "#..............#"
g_map += "################"

tp1 = time.time()
tp2 = time.time()
screen = [[() for i in range(nScreenHeight)] for j in range(nScreenWidth)]


def main():
    global tp2, tp1, fPlayerX, fPlayerY, fPlayerA, elapsedTime

    tp2 = time.time()
    elapsedTime = tp2 - tp1
    tp1 = tp2
    for x in range(0, nScreenWidth):
        fRayAngle = (fPlayerA - fFOV / 2.0) + (float(x) / float(nScreenWidth)) * fFOV
        fStepSize = 0.1
        fDistanceToWall = 0.0
        bHitWall = False
        bBoundary = False
        fEyeX = sin(fRayAngle)
        fEyeY = cos(fRayAngle)

        while not bHitWall and fDistanceToWall < fDepth:
            fDistanceToWall += fStepSize
            nTestX = int(fPlayerX + fEyeX * fDistanceToWall)
            nTestY = int(fPlayerY + fEyeY * fDistanceToWall)

            if nTestX < 0 or nTestX >= nMapWidth or nTestY < 0 or nTestY >= nMapHeight:
                bHitWall = True
                fDistanceToWall = fDepth
            else:
                if g_map[int(nTestX * nMapWidth + nTestY)] == '#':
                    bHitWall = True
                    p = []

                    for tx in range(0, 2):
                        for ty in range(0, 2):
                            vx = float(nTestX + tx - fPlayerX)
                            vy = float(nTestY + ty - fPlayerY)
                            d = math.sqrt(vx * vx + vy * vy)
                            dot = (fEyeX * vx / d) + (fEyeY * vy / d)
                            p.append([d, dot])

                    p.sort()
                    fBound = 0.01

                    if math.acos(p[0][1]) < fBound:
                        bBoundary = True
                    if math.acos(p[1][1]) < fBound:
                        bBoundary = True
                    if math.acos(p[2][1]) < fBound:
                        bBoundary = True

        nCeiling = float(nScreenHeight / 2.0) - nScreenHeight / float(fDistanceToWall)
        nFloor = nScreenHeight - nCeiling
        shade = 0
        color = ()
        if fDistanceToWall < fDepth:
            shade = int(fDistanceToWall * 255 / 16)
        else:
            shade = 0

        for y in range(0, nScreenHeight):
            if y <= nCeiling:
                color = (0, 0, 0)

            elif nCeiling < y <= nFloor:
                color = (255, (255 - shade), 255) if bBoundary else ((255 - shade), (255 - shade), 255)
            else:
                shade = int(255 * (y - nScreenHeight / 2.0) / (nScreenHeight / 2.0))
                color = (shade, 255, shade)
            screen[x][y] = color

    for y in range(0, nScreenHeight):
        for x in range(0, nScreenWidth):
            canvas.create_rectangle(x * 2, y * 2, x * 2 + 2, y * 2 + 2, fill=rgb(screen[x][y]), tag="block")


def rgb(color):
    return "#{:02x}{:02x}{:02x}".format(*color)


def move(direction):
    global fPlayerX, fPlayerY, fPlayerA, elapsedTime, g_map, nMapWidth

    if direction == 'left':
        fPlayerA -= (fSpeed * 1.00) * elapsedTime
    elif direction == 'right':
        fPlayerA += (fSpeed * 1.00) * elapsedTime
    elif direction == 'forward':
        fPlayerX += sin(fPlayerA) * fSpeed * 0.2 * elapsedTime
        fPlayerY += cos(fPlayerA) * fSpeed * 0.2 * elapsedTime
        if g_map[int(fPlayerX) * nMapWidth + int(fPlayerY)] == '#':
            fPlayerX -= sin(fPlayerA) * fSpeed * 0.2 * elapsedTime
            fPlayerY -= cos(fPlayerA) * fSpeed * 0.2 * elapsedTime
    elif direction == 'back':
        fPlayerX -= sin(fPlayerA) * fSpeed * 0.2 * elapsedTime
        fPlayerY -= cos(fPlayerA) * fSpeed * 0.2 * elapsedTime
        if g_map[int(fPlayerX) * nMapWidth + int(fPlayerY)] == '#':
            fPlayerX += sin(fPlayerA) * fSpeed * 0.2 * elapsedTime
            fPlayerY += cos(fPlayerA) * fSpeed * 0.2 * elapsedTime

    window.after(2000, main)


def look(angle):
    pass


"""def on_mouse_click(event):
    window.config(cursor='none')"""

window = Tk()
window.title("!!! FPS GAME !!!")
window.resizable(False, False)
window.config(cursor='cross')

canvas = Canvas(window, bg="#000000", height=nScreenHeight * 2, width=nScreenWidth * 2)
canvas.pack()

window.update()

window.bind('<Left>', lambda event: move('left'))
window.bind('<Right>', lambda event: move('right'))
window.bind('<Up>', lambda event: move('forward'))
window.bind('<Down>', lambda event: move('back'))
#window.bind("<Motion>", look)
# window.bind("<Button-1>", on_mouse_click)

main()

window.mainloop()

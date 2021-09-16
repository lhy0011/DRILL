from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def drawGrass():
    clear_canvas_now()
    grass.draw_now(400, 30)

def quadrilateral_motion(x, y):
    while x < 770:
        drawGrass()
        character.draw_now(x, y)
        x += 2
        delay(0.01)
    while y < 560:
        drawGrass()
        character.draw_now(x, y)
        y += 2
        delay(0.01)
    while x > 30:
        drawGrass()
        character.draw_now(x, y)
        x -= 2
        delay(0.01)
    while y > 90:
        drawGrass()
        character.draw_now(x, y)
        y -= 2
        delay(0.01)
    while x < 400:
        drawGrass()
        character.draw_now(x, y)
        x += 2
        delay(0.01)
    
def circular_motion(x, y):
    for i in range(0, 360):
        angle =  i * 2 * math.pi / 360
        x += math.cos(angle) * 4
        y += math.sin(angle) * 4
        drawGrass()
        character.draw_now(x, y)
        delay(0.01)

x = 400
y = 90
while (True):
    quadrilateral_motion(x, y)
    circular_motion(x, y)
    




from pico2d import *
import random
WIDTH, HEIGHT = 1280, 1024

def draw_hand():
    global running
    global touch
    global x, y
    global touch
    global hand_x, hand_y
    hand_x = random.randint(100, 1100)
    hand_y = random.randint(100, 900)
    touch = False

open_canvas(WIDTH, HEIGHT)

ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
touch = True
x, y = WIDTH // 2, HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    if touch == True:
        draw_hand()
    ground.draw(WIDTH // 2, HEIGHT // 2)
    if x < hand_x:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif x > hand_x:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    hand.draw(hand_x, hand_y)
    update_canvas()

    frame = (frame + 1) % 8
    if x > hand_x:
        x -= 1
    if y > hand_y:
        y -= 1
    if x < hand_x:
        x += 1
    if y < hand_y:
        y += 1
    if x == hand_x and y == hand_y:
        touch = True
    delay(0.001)



close_canvas()
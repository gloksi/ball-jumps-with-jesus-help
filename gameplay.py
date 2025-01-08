import pygame as pg
import random
from physics.ball import Ball

new_ball = Ball([577, 273], [random.randint(-20, 20), random.randint(-20, 20)])

surface = pg.display.set_mode((1183, 586))
surface.blit(pg.image.load("pics/bg.png"), (0, 0))
pg.display.set_caption('Jesus and a ball')
pg.display.set_icon(pg.image.load("pics/icon.png"))

pg.init()
new_ball.render(surface)

while True:
    pg.display.flip()
    pg.time.Clock().tick(15)

    surface.blit(pg.image.load("pics/bg.png"), (0, 0))
    new_ball.update_pos()
    new_ball.render(surface)
pg.quit()

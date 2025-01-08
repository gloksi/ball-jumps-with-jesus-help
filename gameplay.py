import pygame as pg
from physics.ball import Ball

new_ball = Ball([500, 50], 1)

surface = pg.display.set_mode((1183, 586))
surface.blit(pg.image.load("pics/bg.png"), (0, 0))
pg.display.set_caption('Jesus and a ball')
pg.display.set_icon(pg.image.load("pics/icon.png"))

pg.init()
new_ball.render(surface)
while True:
    pg.display.flip()
    pg.time.Clock().tick(5)

pg.quit()


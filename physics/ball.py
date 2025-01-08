import pygame as pg

class Ball:
    def __init__(self, coords, vel):
        self.coords = coords
        self.vel = vel

    def getCoords(self):
        return self.coords
    
    def getVel(self):
        return self.vel
    
    def setCoords(self, coords):
        self.coords = coords
    
    def setVel(self, vel):
        self.vel = vel

    def render(self, surface):
        pg.draw.circle(surface, "blue", (self.coords[0], self.coords[1]), 20)

    def update_pos(self):
        self.coords = (self.coords[0] + self.vel[0], self.coords[1] - self.vel[1])
        
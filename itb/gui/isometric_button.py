import pygame

from itb.gui.colours import *


class IsometricButton:
    def __init__(self, x, y, width, height, color, callback=None, update_colour=None):
        self.once = False
        self.coords = (None, None)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = (color[0] + 50, color[1] + 50, color[2] + 50)
        self.pressed_color = (color[0] - 50, color[1] - 50, color[2] - 50)
        self.is_hovered = False
        self.is_pressed = False

        self.iso_left = self.x - (self.width / 2)
        self.iso_top = self.y + (self.height / 3)
        self.iso_right = self.x + (self.width / 2)
        self.iso_bottom = self.y - (self.height / 3)

        if callback is not None:
            self.callback = callback

        if update_colour is not None:
            self.update_colour = update_colour

    def callback(self, *args):
        raise NotImplementedError

    def update_colour(self, *args):
        raise NotImplementedError

    def draw(self, screen):
        x, y = self.coords
        if self.is_pressed:
            color = self.pressed_color
            if not self.once:
                try:
                    self.callback(x, y)
                except NotImplementedError:
                    pass
                self.once = True
        elif self.is_hovered:
            self.once = False
            color = self.hover_color
        else:
            self.once = False

            #  set the colour to something other than white
            if (c := self.update_colour(x, y)) != None:
                color = c
            else:
                color = self.color

        pygame.draw.polygon(
            screen,
            color,
            [
                (self.iso_left, self.y),
                (self.x, self.iso_top),
                (self.iso_right, self.y),
                (self.x, self.iso_bottom),
            ],
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.is_mouse_over(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_mouse_over(event.pos):
                self.is_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.is_pressed = False

    def sign(self, p1x, p1y, p2x, p2y, px, py):
        return (px - p1x) * (p2y - p1y) - (py - p1y) * (p2x - p1x)

    def is_point_inside_quadrilateral(self, x, y, x1, y1, x2, y2, x3, y3, x4, y4):
        b1 = self.sign(x1, y1, x2, y2, x, y) < 0
        b2 = self.sign(x2, y2, x3, y3, x, y) < 0
        b3 = self.sign(x3, y3, x4, y4, x, y) < 0
        b4 = self.sign(x4, y4, x1, y1, x, y) < 0

        return (b1 == b2) and (b2 == b3) and (b3 == b4)

    def is_mouse_over(self, pos):
        x, y = pos

        b1 = self.sign(self.iso_left, self.y, self.x, self.iso_top, x, y) < 0
        b2 = self.sign(self.x, self.iso_top, self.iso_right, self.y, x, y) < 0
        b3 = self.sign(self.iso_right, self.y, self.x, self.iso_bottom, x, y) < 0
        b4 = self.sign(self.x, self.iso_bottom, self.iso_left, self.y, x, y) < 0

        return (b1 == b2) and (b2 == b3) and (b3 == b4)

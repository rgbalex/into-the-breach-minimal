import pygame
import os
from dotenv import load_dotenv

# get version from .env
load_dotenv()
VERSION = os.getenv("VERSION")


# Initialize Pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 1027 / 2 * 3
SCREEN_HEIGHT = 1000 / 4 * 5

print(f"Setting screen dimensions to {SCREEN_WIDTH}x{SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption(f"AGENT DIFFICULTY TESTER VERSION v{VERSION}")

# Define some colors
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)


# Define the button class
class IsometricButton:
    def __init__(self, x, y, width, height, color):
        self.once = False
        self.coords = (None, None)
        # anchored at the middle of the object
        self.x = x
        self.y = y
        # cartesian width and height of object
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

    def draw(self, screen):
        if self.is_pressed:
            color = self.pressed_color
            if not self.once:
                print(self.coords)
                self.once = True
        elif self.is_hovered:
            self.once = False
            color = self.hover_color
        else:
            self.once = False
            color = self.color

        # Draw the button
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
        # check if the mouse is over the button
        x, y = pos

        b1 = self.sign(self.iso_left, self.y, self.x, self.iso_top, x, y) < 0
        b2 = self.sign(self.x, self.iso_top, self.iso_right, self.y, x, y) < 0
        b3 = self.sign(self.iso_right, self.y, self.x, self.iso_bottom, x, y) < 0
        b4 = self.sign(self.x, self.iso_bottom, self.iso_left, self.y, x, y) < 0

        return (b1 == b2) and (b2 == b3) and (b3 == b4)


# Create a grid of buttons
pad_vertical = 1.1
pad_horizontal = 1.1
offset_vertical = (SCREEN_HEIGHT / 2) + 100
offset_horizontal = SCREEN_WIDTH / 8
measure = IsometricButton(8196, 8196, 150, 150, GREY)


board = [[None for _ in range(8)] for _ in range(8)]
for i in range(len(board)):
    for j in range(len(board)):
        x = (i + j) * (measure.width / 2)
        y = (j - i) * (measure.height / 3)

        x = x * pad_horizontal
        y = y * pad_vertical

        x += offset_horizontal
        y += offset_vertical

        button = IsometricButton(x, y, measure.width, measure.height, GREY)
        button.coords = (i, j)
        board[j][i] = button

font = pygame.font.Font(None, 36)


def draw_title(screen):
    title = font.render(f"Agent Difficulty Tester Version v{VERSION}", True, WHITE)
    text_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(title, text_rect)


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for row in board:
            for button in row:
                button.handle_event(event)

    # Draw everything
    screen.fill(BLACK)
    for row in board:
        for button in row:
            button.draw(screen)

    # add title text
    draw_title(screen)

    pygame.display.flip()

# Quit Pygame
pygame.quit()

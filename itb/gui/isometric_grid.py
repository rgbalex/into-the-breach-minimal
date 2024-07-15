import pygame
import os
from dotenv import load_dotenv

# get version from .env
load_dotenv()
VERSION = os.getenv("VERSION")


# Initialize Pygame
pygame.init()


class IsometricGrid:
    def __init__(self, screen_width, screen_height):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.buttons = []
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.font = pygame.font.Font(None, 36)

    def create_button(self, x, y, width, height, color):
        button = IsometricButton(x, y, width, height, color)
        self.buttons.append(button)
        return button

    def create_board(
        self, measure, pad_horizontal, pad_vertical, offset_horizontal, offset_vertical
    ):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                x = (i + j) * (measure.width / 2)
                y = (j - i) * (measure.height / 3)

                x = x * pad_horizontal
                y = y * pad_vertical

                x += offset_horizontal
                y += offset_vertical

                button = self.create_button(x, y, measure.width, measure.height, GREY)
                button.coords = (i, j)
                self.board[j][i] = button

    def draw_sides(self):
        pad_vertical = 5
        for i in range(8):
            item: IsometricButton = self.board[i][0]
            pygame.draw.polygon(
                self.screen,
                GREY_DARK,
                [
                    (item.iso_left - 4, item.y + pad_vertical),
                    (item.iso_left - 4, item.iso_top + pad_vertical),
                    (item.x - 4, item.iso_top + (item.iso_top - item.y) + pad_vertical),
                    (item.x - 4, item.iso_top + pad_vertical),
                ],
            )

        pad_vertical = 5
        for i in range(8):
            item: IsometricButton = self.board[7][i]
            pygame.draw.polygon(
                self.screen,
                WHITE,
                [
                    (item.iso_right + 4, item.y + pad_vertical),
                    (item.iso_right + 4, item.iso_top + pad_vertical),
                    (item.x + 4, item.iso_top + (item.iso_top - item.y) + pad_vertical),
                    (item.x + 4, item.iso_top + pad_vertical),
                ],
            )

    def draw_axis_labels(self):
        text = self.font.render("X", True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3))
        self.screen.blit(text, text_rect)

        for i in range(8):
            text = self.font.render(f"{i}", True, BLACK)
            text_rect = text.get_rect(
                center=(self.board[0][i].x - 50, self.board[0][i].y)
            )
            self.screen.blit(text, text_rect)

        text = self.font.render("Y", True, WHITE)
        text_rect = text.get_rect(
            center=(SCREEN_WIDTH // 4, (2.6 * SCREEN_HEIGHT) // 3)
        )
        self.screen.blit(text, text_rect)

        for i in range(8):
            text = self.font.render(f"{i}", True, WHITE)
            text_rect = text.get_rect(
                center=(self.board[i][0].x - 45, self.board[i][0].y + 55)
            )
            self.screen.blit(text, text_rect)

    def draw_title(self):
        title = self.font.render(
            f"Agent Difficulty Tester Version v{VERSION}", True, WHITE
        )
        text_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 50))
        self.screen.blit(title, text_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            for row in self.board:
                for button in row:
                    button.handle_event(event)
        return True

    def draw(self):
        self.screen.fill(BLACK)
        for row in self.board:
            for button in row:
                button.draw(self.screen)
        self.draw_sides()
        self.draw_title()
        self.draw_axis_labels()
        pygame.display.flip()


class IsometricButton:
    def __init__(self, x, y, width, height, color):
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


# Set the screen dimensions
SCREEN_WIDTH = 1027 // 2 * 3
SCREEN_HEIGHT = 1000 // 4 * 5

print(f"Setting screen dimensions to {SCREEN_WIDTH}x{SCREEN_HEIGHT}")

# Set the title of the window
pygame.display.set_caption(f"AGENT DIFFICULTY TESTER VERSION v{VERSION}")

# Define some colors
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
GREY_DARK = (100, 100, 100)
BLACK = (0, 0, 0)

# Create the isometric grid
grid = IsometricGrid(SCREEN_WIDTH, SCREEN_HEIGHT)

# Create a measure button
measure = grid.create_button(8196, 8196, 150, 150, GREY)

# Create the board of buttons
grid.create_board(measure, 1.1, 1.1, SCREEN_WIDTH / 8, (SCREEN_HEIGHT / 2) + 100)

# Main loop
running = True
while running:
    running = grid.handle_events()
    grid.draw()

# Quit Pygame
pygame.quit()

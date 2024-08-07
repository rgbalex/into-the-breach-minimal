import os, pygame
from typing import Optional

from dotenv import load_dotenv

from itb.board import Board
from itb.entities import EntityDictionary
from itb.gui.isometric_button import IsometricButton
from itb.gui.colours import *


class IsometricGrid:
    entity_dict = EntityDictionary()

    def __init__(self, screen_width, screen_height, board: Board):
        load_dotenv()
        pygame.init()

        self.screen_width = screen_width
        self.screen_height = screen_height
        print(f"Setting screen dimensions to {screen_width}x{screen_height}")

        self.version = os.getenv("VERSION")
        pygame.display.set_caption(f"AGENT DIFFICULTY TESTER VERSION v{self.version}")

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.buttons = []
        self.display_board = [[None for _ in range(8)] for _ in range(8)]
        self.font = pygame.font.Font(None, 36)

        self.game_board: Board = board

    def run(self):
        self.create_board(
            1.1, 1.1, self.screen_width / 8, (self.screen_height / 2) + 100
        )
        running = True
        while running:
            running = self.handle_events()
            self.draw()
        pygame.quit()

    def calculate_entity_color(self, x, y) -> Optional[tuple[int, int, int]]:
        entity = self.game_board.get_entity_by_coords(x, y)
        if entity is not None:
            return self.entity_dict.get_default_colour(entity[0])
        return None

    def get_entity_by_coords(self, x, y) -> Optional[tuple[int]]:
        print(self.game_board.get_entity_by_coords(x, y))

    def create_button(self, x, y, width, height, color):
        button = IsometricButton(
            x,
            y,
            width,
            height,
            color,
            callback=self.get_entity_by_coords,
            update_colour=self.calculate_entity_color,
        )
        self.buttons.append(button)
        return button

    def create_board(
        self, pad_horizontal, pad_vertical, offset_horizontal, offset_vertical
    ):
        measure = self.create_button(8196, 8196, 150, 150, GREY)
        for i in range(len(self.display_board)):
            for j in range(len(self.display_board)):
                if self.game_board.get_tile(i, j) == 0:
                    self.display_board[j][i] = None
                    continue
                x = (i + j) * (measure.width / 2)
                y = (j - i) * (measure.height / 3)

                x = x * pad_horizontal
                y = y * pad_vertical

                x += offset_horizontal
                y += offset_vertical

                button = self.create_button(x, y, measure.width, measure.height, GREY)
                button.coords = (i, j)
                self.display_board[j][i] = button

    def draw_sides(self):
        pad_vertical = 5
        for i in range(8):
            item: IsometricButton = self.display_board[i][0]
            if item is None:
                continue
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
            item: IsometricButton = self.display_board[7][i]
            if item is None:
                continue
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
        text_rect = text.get_rect(
            center=(self.screen_width // 4, self.screen_height // 3)
        )
        self.screen.blit(text, text_rect)

        for i in range(8):
            if self.display_board[0][i] is None:
                continue
            text = self.font.render(f"{i}", True, BLACK)
            text_rect = text.get_rect(
                center=(self.display_board[0][i].x - 50, self.display_board[0][i].y)
            )
            self.screen.blit(text, text_rect)

        text = self.font.render("Y", True, WHITE)
        text_rect = text.get_rect(
            center=(self.screen_width // 4, (2.6 * self.screen_height) // 3)
        )
        self.screen.blit(text, text_rect)

        for i in range(8):
            if self.display_board[i][0] is None:
                continue
            text = self.font.render(f"{i}", True, WHITE)
            text_rect = text.get_rect(
                center=(
                    self.display_board[i][0].x - 45,
                    self.display_board[i][0].y + 55,
                )
            )
            self.screen.blit(text, text_rect)

    def draw_title(self):
        title = self.font.render(
            f"Agent Difficulty Tester Version v{self.version}", True, WHITE
        )
        text_rect = title.get_rect(center=(self.screen_width // 2, 50))
        self.screen.blit(title, text_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            for row in self.display_board:
                button: IsometricButton
                for button in row:
                    if button is None:
                        continue
                    button.handle_event(event)
        return True

    def draw(self):
        self.screen.fill(BLACK)
        for row in self.display_board:
            for button in row:
                if button is None:
                    continue
                button.draw(self.screen)
        self.draw_sides()
        self.draw_title()
        self.draw_axis_labels()
        pygame.display.flip()

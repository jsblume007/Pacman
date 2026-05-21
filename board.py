import pygame as pg
from constants import *

class Board:
    def __init__(self):
        self.grid = [
            "#################",
            "#...##.....##...#",
            "#.#.###.###.#.#.#",
            "#.#...........#.#",
            "#.#.###.#.###.#.#",
            "#.....#...#.....#",
            "###.#.#####.#.###",
            "#...............#",
            "###.#.#####.#.###",
            "#.....#...#.....#",
            "#.#.###.#.###.#.#",
            "#.#...........#.#",
            "#.#.###.###.#.#.#",
            "#...##.....##...#",
            "#################",
        ]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

        self.food = set()

        for row, line in enumerate(self.grid):
            for col, tile in enumerate(line):
                if tile == ".":
                    self.food.add((col, row))

    def window_size(self):
        return self.cols*TILE_SIZE, self.rows*TILE_SIZE

    def draw(self, surface):
        """Tegn brettet på den gitte pygame-flaten."""
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                rect = pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if tile == '#':
                    pg.draw.rect(surface, DARK_BLUE, rect, border_radius=5)

        # Tegner maten
        for col, row in self.food:
            x = col * TILE_SIZE + TILE_SIZE // 2
            y = row * TILE_SIZE + TILE_SIZE // 2

            pg.draw.circle(surface, YELLOW, (x, y), 4)


    def is_road(self, x: int, y: int) -> bool:
        """Returnerer True hvis posisjonen er fri for vegg."""
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
            return False
        return self.grid[y][x] != '#'
    
    def eat_food(self, col, row):
        """Fjerner mat hvis Pacman står på en rute med mat."""

        if (col, row) in self.food:
            self.food.remove((col, row))
            return 10

        return 0

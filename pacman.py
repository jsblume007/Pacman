from pathlib import Path
import pygame as pg
from constants import *

class PacMan:
    IMAGE_FILE = Path(__file__).parent / "sprites" / "pacman2.png"

    def getImageSpriteList(self, x_start, y_start, num_frames) -> list[pg.Surface]:
        full_image = pg.image.load(self.IMAGE_FILE)
        frame_width = 16
        
        # Dele opp bildet i frames, som lagres i en liste:
        frames = []
        for i in range(num_frames):
            # Bildene er kvadratiske - bruker frame widht både som høye og bredde:
            frame = full_image.subsurface(pg.Rect(x_start + i * frame_width, y_start, frame_width, frame_width))
            frames.append(frame)
        return frames
    

    def __init__(self, row, col):
        self.row = row
        self.col = col

        self.frames_hoyre = self.getImageSpriteList(0, 0, 4)
        self.frames_opp   = self.getImageSpriteList(0, 32, 4)
        self.frames_ned   = self.getImageSpriteList(0, 48, 4)

        self.frames = self.frames_hoyre
        self.current_frame = 0
        self.retning = "hoyre"  # "hoyre", "venstre", "opp", "ned"

    def move(self, dcol, drow, board):
        ny_col = self.col + dcol
        ny_row = self.row + drow
        if board.is_road(ny_col, ny_row):
            self.col = ny_col
            self.row = ny_row
            if dcol < 0:
                self.retning = "venstre"
                self.frames = self.frames_hoyre
            elif dcol > 0:
                self.retning = "hoyre"
                self.frames = self.frames_hoyre
            elif drow < 0:
                self.retning = "opp"
                self.frames = self.frames_opp
            elif drow > 0:
                self.retning = "ned"
                self.frames = self.frames_ned

    def draw(self, surface):

        current_frame_image = self.frames[self.current_frame]

        # Speiler bildet hvis Pacman går til venstre:
        if self.retning == "venstre":
            current_frame_image = pg.transform.flip(current_frame_image, True, False)

        # Sørg for at vi tegner midt i "Tile":
        mid = TILE_SIZE // 2
        rect = current_frame_image.get_rect()
        rect.center = (self.col * TILE_SIZE + mid , self.row * TILE_SIZE + mid)

        # Blit images på skjermen (der self.rect befinner seg):
        surface.blit(current_frame_image, rect)


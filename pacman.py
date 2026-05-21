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

        self.frames_idle = self.getImageSpriteList(0, 0, 4)
        # Bildet vi skal vise til å starte med er idle:
        self.frames = self.frames_idle
        # Om vi vil ha animasjon som går gjennom frames:
        self.current_frame = 0

        # Om vi vil speile bildet:
        self.venstre = False

    def move(self, dcol, drow, board):
        # Regner ut neste/ny posisjon
        ny_col = self.col + dcol
        ny_row = self.row + drow
        if board.is_road(ny_col, ny_row):
            self.col = ny_col
            self.row = ny_row
            if dcol < 0:    # Beveger seg til venstre
                self.venstre = True
            elif dcol > 0:  # Beveger seg til høyre
                self.venstre = False

    def draw(self, surface):

        # Få bildet fra en liste av bilder (om du vil bruke animasjon/sprites):
        current_frame_image = self.frames[self.current_frame]
        
        # Speiler bildet hvis det trengs:
        if self.venstre:
            current_frame_image = pg.transform.flip(current_frame_image, True, False)

        # Sørg for at vi tegner midt i "Tile":
        mid = TILE_SIZE // 2
        rect = current_frame_image.get_rect()
        rect.center = (self.col * TILE_SIZE + mid , self.row * TILE_SIZE + mid)

        # Blit images på skjermen (der self.rect befinner seg):
        surface.blit(current_frame_image, rect)


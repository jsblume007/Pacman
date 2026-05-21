import pygame as pg
from constants import *
from board import Board
from pacman import PacMan

pg.init()
board = Board()
vindu = pg.display.set_mode(board.window_size())
clock = pg.time.Clock()


pacman = PacMan(3, 4)
score = 0

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                pacman.move(0, -1, board)
            elif event.key == pg.K_DOWN:
                pacman.move(0, 1, board)
            elif event.key == pg.K_LEFT:
                pacman.move(-1, 0, board)
            elif event.key == pg.K_RIGHT:
                pacman.move(1, 0, board)

    # Tegn bakgrunn: (En slags "reset" av hele vinduet vårt)
    vindu.fill(BLACK)

    # Tegn brettet først, og pacman og andre ting "oppå":
    board.draw(vindu)

    # TODO: Oppdater objektene våre:
    score += board.eat_food(pacman.col, pacman.row)


    # Tegn objektene våre:
    pacman.draw(vindu)
    font = pg.font.SysFont("Arial", 24)
    score_text = font.render(f"Poeng: {score}", True, WHITE)
    vindu.blit(score_text, (10, 5))


    # Har alltid disse med til slutt:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame på en "ryddig måte":
pg.quit()

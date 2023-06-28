"""
Created on Tue Jun 27 23:35:00 2023

@author: Sami RAJICHI

@project: HangMan
"""

import pygame
import os


if __name__ == '__main__':
    pygame.init()
    HEIGHT, WIDTH = 800, 500
    pygame.display.set_mode((HEIGHT, WIDTH))
    pygame.display.set_caption('HangMan Game')

    FPS: int = 60
    clock = pygame.time.Clock()
    run: bool = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

"""
Created on Wed Jun 28 07:22:04 2023

@author: Sami RAJICHI

@project: Pygame Configuration Module
"""

import pygame


class PygameSetup:

    HEIGHT, WIDTH = 500, 800
    FPS: int = 60
    run: bool = True

    def __setup_display(self):
        pygame.init()
        self.win: object = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('HangMan Game')

    def __game_variables(self):
        self.images: list[object] = []
        # Set colors variables
        self.WHITE: tuple[int] = (255, 255, 255)
        self.BLACK: tuple[int] = (0, 0, 0)
        # Set buttons variables
        self.GAP: float = 15
        self.RADIUS: float = 20
        self.letters: list[tuple] = []
        self.startX: float = round(
            (self.WIDTH - (self.RADIUS*2 + self.GAP) * 13) / 2)
        self.startY: int = 375
        for i in range(26):
            x: float = self.startX + self.GAP*2 + \
                ((self.RADIUS*2 + self.GAP) * (i % 13))
            y: float = self.startY + ((self.RADIUS*2 + self.GAP) * (i // 13))
            self.letters.append((x, y, chr(65 + i)))
        # Set text fonts
        self.LETTER_FONT: pygame.Font = pygame.font.SysFont('comicsans', 28)

    def __init__(self):
        self.__setup_display()
        self.__game_variables()
        self.__load_images()

    def __event_trigger(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

    def __load_images(self):
        for i in range((7)):
            self.images.append(pygame.image.load(
                f'./images/hangman{str(i)}.png'))

    def __draw_button(self):
        for letter in self.letters:
            x, y, ltr = letter
            pygame.draw.circle(self.win, self.BLACK, (x, y), self.RADIUS, 2)
            text: pygame.Surface = self.LETTER_FONT.render(ltr, 1, self.BLACK)
            self.win.blit(text, (x - (text.get_width()/2),
                          y - (text.get_height()/2)))

    def __update_display(self, image: int):
        self.win.fill(self.WHITE)
        self.__draw_button()
        self.win.blit(self.images[image], (150, 100))
        pygame.display.update()

    def run(self, image: int):
        """
        This method tends to set the game loop and run the game
        """
        clock: object = pygame.time.Clock()
        self.__update_display(image)
        while self.run:
            clock.tick(self.FPS)
            self.__event_trigger()
        pygame.quit()

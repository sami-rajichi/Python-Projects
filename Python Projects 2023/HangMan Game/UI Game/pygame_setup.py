"""
Created on Wed Jun 28 07:22:04 2023

@author: Sami RAJICHI

@project: Pygame Configuration Module
"""

import pygame
from math import sqrt
from hangman import HangMan


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
        self.rectX: float = (self.WIDTH / 2) - 235
        self.rectY: float = (self.HEIGHT / 2) + 100
        self.rectWidth: float = 150
        self.rectHeight: float = 60
        self.play_again = True
        for i in range(26):
            x: float = self.startX + self.GAP*2 + \
                ((self.RADIUS*2 + self.GAP) * (i % 13))
            y: float = self.startY + ((self.RADIUS*2 + self.GAP) * (i // 13))
            self.letters.append([x, y, chr(65 + i), True])
        # Set text fonts
        self.LETTER_FONT: pygame.Font = pygame.font.SysFont('comicsans', 28)
        self.WORD_FONT = pygame.font.SysFont('comicsans', 46)
        self.TITLE_FONT = pygame.font.SysFont('comicsans', 60)

    def __init__(self):
        self.hangman = HangMan()
        self.__setup_display()
        self.__game_variables()
        self.__load_images()

    def __event_trigger(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                for letter in self.letters:
                    x, y, ltr, visible = letter
                    if visible:
                        distance: float = sqrt(
                            (x - mouseX)**2 + (y - mouseY)**2)
                        if distance <= self.RADIUS:
                            self.hangman.start_game(ltr)
                            letter[3] = False

    def __load_images(self):
        for i in range((7)):
            self.images.append(pygame.image.load(
                f'./images/hangman{str(i)}.png'))

    def __render_text(self, text: str, font: object, x: float, y: float):
        text: pygame.Surface = font.render(
            text, 1, self.BLACK)
        self.win.blit(text, (x - text.get_width()/2,
                      y - text.get_height()/2))

    def game_status(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if (mouseX > self.rectX and mouseX < self.rectX + self.rectWidth) and (mouseY > self.rectY and mouseY < self.rectY + self.rectHeight):
                    self.__game_variables()
                    self.__load_images()
                    self.hangman = HangMan()
                    self.play_again = True
                if (mouseX > self.rectX*2 + self.rectWidth and mouseX < self.rectX*2 + self.rectWidth*2) and (mouseY > self.rectY and mouseY < self.rectY + self.rectHeight):
                    self.run = False

    def __draw_play_again_button(self):
        pygame.draw.rect(self.win, self.BLACK,
                         (self.rectX, self.rectY, self.rectWidth, self.rectHeight), width=2)
        pygame.draw.rect(self.win, self.BLACK,
                         (self.rectX*2 + self.rectWidth, self.rectY, self.rectWidth, self.rectHeight), width=2)
        text: pygame.Surface = self.LETTER_FONT.render(
            'Play Again', 1, self.BLACK)
        self.win.blit(text, (self.rectX + (self.rectWidth - text.get_width()) / 2,
                      self.rectY + (self.rectHeight - text.get_height()) / 2))
        text: pygame.Surface = self.LETTER_FONT.render(
            'Quit', 1, self.BLACK)
        self.win.blit(text, (self.rectX*2 + self.rectWidth + (self.rectWidth - text.get_width()) / 2,
                      self.rectY + (self.rectHeight - text.get_height()) / 2))
        self.game_status()

    def __game_result(self, res: str):
        if res == 'win':
            self.win.fill(self.WHITE)
            self.__render_text('You WON !', self.TITLE_FONT,
                               (self.WIDTH/2), (self.HEIGHT/2) - 40)
            self.__draw_play_again_button()
        else:
            self.win.fill(self.WHITE)
            self.__render_text('Game Over !', self.TITLE_FONT,
                               (self.WIDTH/2), (self.HEIGHT/2) - 80)
            self.__render_text('The word was: ' + self.hangman.word, self.WORD_FONT,
                               (self.WIDTH/2), (self.HEIGHT/2))
            self.__draw_play_again_button()
        pygame.display.update()

    def __draw_button(self):
        for letter in self.letters:
            x, y, ltr, visible = letter
            if visible:
                pygame.draw.circle(self.win, self.BLACK,
                                   (x, y), self.RADIUS, 2)
                text: pygame.Surface = self.LETTER_FONT.render(
                    ltr, 1, self.BLACK)
                self.win.blit(text, (x - (text.get_width()/2),
                              y - (text.get_height()/2)))

    def __update_display(self, image: int):
        self.win.fill(self.WHITE)
        self.__draw_button()
        self.__render_text(self.hangman.word_completion,
                           self.WORD_FONT, (self.WIDTH / 2) + 100, (self.HEIGHT / 2) - 20)
        self.__render_text('HangMan Game',
                           self.TITLE_FONT, (self.WIDTH / 2), 40)
        self.win.blit(self.images[image], (150, 110))
        pygame.display.update()

    def run(self):
        """
        This method tends to set the game loop and run the game
        """
        clock: object = pygame.time.Clock()
        image: int = self.hangman.tries
        self.__update_display(image)
        while self.run:
            if self.play_again:
                clock.tick(self.FPS)
                image: int = self.hangman.tries
                self.__event_trigger()
                self.__update_display(image)
                if self.hangman.guessed or image == 0:
                    self.play_again = False
            else:
                if self.hangman.guessed:
                    pygame.time.delay(600)
                    self.__game_result('win')
                if image == 0:
                    self.__game_result('lose')
        pygame.quit()


if __name__ == '__main__':
    pygame_setup: PygameSetup = PygameSetup()
    pygame_setup.run()

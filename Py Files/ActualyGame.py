import pygame
from pygame import mixer
from pygame.font import SysFont

from pygameCButClass import CGame
from pygameO1ButClass import O1Game
from pygameLButClass import LGame
from pygameO2ButClass import OGame
from pygameRButClass import RGame

class GameMenu:
    def __init__(self):
        # Constants...
        mixer.init()
        self.width, self.height = 1000, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.stage = 0

        pygame.font.init()
        self.font = SysFont("comicsans", 30)
        self.font1 = SysFont("arial", 13)
        self.font2 = SysFont("comicsans", 75)

        # Load images...
        self.rainbow = pygame.transform.scale(pygame.image.load("rainbow.jpg"), (self.width, self.height))
        self.chaseGameUi = pygame.transform.scale(pygame.image.load("chaseNEW.png"), (300, 200))
        self.ostrichWhackUi = pygame.transform.scale(pygame.image.load("ostrichNEW.png"), (300, 200))
        self.drawingGameUi = pygame.transform.scale(pygame.image.load("LayoutNEW.png"), (300, 200))  # This is the drawing game
        self.obbyGameUi = pygame.transform.scale(pygame.image.load("obbyNEW.png"), (300, 200))
        self.raindropDodgeUi = pygame.transform.scale(pygame.image.load("rainNEW.png"), (300, 200))
        self.homeIconUi = pygame.transform.scale(pygame.image.load("homeIcon.jpg"), (50, 50))

        # Create buttons...
        self.chaseGameButton = pygame.Rect(25, 50, 300, 200)
        self.ostrichWhackButton = pygame.Rect(360, 50, 300, 200)
        self.drawingGameButton = pygame.Rect(695, 50, 300, 200)  # This is the drawing game
        self.obbyGameButton = pygame.Rect(200, self.height - 250, 300, 200)
        self.raindropDodgeButton = pygame.Rect(555, self.height - 250, 300, 200)
        self.homeIconButton = pygame.Rect(25, self.height - 75, 50, 50)
        
    def checkClick(self, button):
        mouse_pos = pygame.mouse.get_pos()
        return button.collidepoint(mouse_pos)

    def run(self):
        completeGameLoop = True
        while completeGameLoop:
            # Stage 0: Main menu
            if self.stage == 0:
                self.screen.blit(self.rainbow, (0, 0))
                self.screen.blit(self.homeIconUi, (25, (self.height - 75)))
                self.screen.blit(self.chaseGameUi, (25, 50))
                self.screen.blit(self.ostrichWhackUi, (360, 50))
                self.screen.blit(self.drawingGameUi, (695, 50))
                self.screen.blit(self.obbyGameUi, (200, self.height - 250))
                self.screen.blit(self.raindropDodgeUi, (555, self.height - 250))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        completeGameLoop = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.checkClick(self.chaseGameButton):
                            self.stage = 1
                        elif self.checkClick(self.ostrichWhackButton):
                            self.stage = 2
                        elif self.checkClick(self.drawingGameButton):
                            self.stage = 3
                        elif self.checkClick(self.obbyGameButton):
                            self.stage = 4
                        elif self.checkClick(self.raindropDodgeButton):
                            self.stage = 5
                        elif self.checkClick(self.homeIconButton):
                            self.stage = 0

            # Stage 1: Chasing game
            if self.stage == 1:
                game = CGame()
                result = game.runGame()
                if result == "home":
                    self.stage = 0

            # Stage 2: Ostrich Whack game
            if self.stage == 2:
                game = O1Game()
                result = game.runGame()
                if result == "home":
                    self.stage = 0

            # Stage 3: LuminaryDraw game
            if self.stage == 3:
                game = LGame()
                result = game.runGame()
                if result == "home":
                    self.stage = 0

            # Stage 4: Obby game
            if self.stage == 4:
                game = OGame()
                result = game.runGame()
                if result == "home":
                    self.stage = 0

            # Stage 5: Raindrop Dodge game
            if self.stage == 5:
                game = RGame()
                result = game.runGame()
                if result == "home":
                    self.stage = 0

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    menu = GameMenu()
    menu.run()

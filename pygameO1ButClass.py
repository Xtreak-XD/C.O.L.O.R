import pygame
import random
from pygame import mixer

class O1Game:
    def __init__(self):
        pygame.init()
        mixer.init()
        
        self.width, self.height = 1000, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.font.init()
        self.font = pygame.font.SysFont("comicsans", 30)
        self.font2 = pygame.font.SysFont("comicsans", 75)
        
        self.player = pygame.Rect((300, 250 , 50, 50))
        self.playerVel = 1
        self.playerWidth = 20
        self.playerHeight = 40
        
        self.whackAMoleUi = pygame.transform.scale(pygame.image.load("ostrichNEW.png"), (300, 200))
        self.whackAMoleButton = pygame.Rect((360, 50,300,200 ))
        
        self.homeIconUi = pygame.transform.scale(pygame.image.load("homeIcon.jpg"), (50, 50))
        self.homeIconButton = pygame.Rect(25, self.height - 75, 50, 50)
        
        self.bigText = self.font2.render("O", 10, "black")
        self.color = (100, 200, 100)
        self.score = 0
        self.run = True
        self.text1 = self.font.render("Ostrich Catch", 10, "black")
        self.text3 = self.font.render("Z to reset", 10, "black")
        self.moleCoordinates = []
        
        self.createMole = pygame.event.custom_type()
        pygame.time.set_timer(self.createMole, 1100)
        
        self.destroyMole = pygame.event.custom_type()
        pygame.time.set_timer(self.destroyMole, 3300)
        
        self.mole = pygame.transform.scale(pygame.image.load("mole.png"), (self.playerWidth + 50, self.playerHeight + 30))
        mixer.music.load("fryingPanAudio.mp3")

    def checkClick(self, button):
        mousePos = pygame.mouse.get_pos()
        return button.collidepoint(mousePos)

    def runGame(self):
        while self.run:
            self.bigText = self.font2.render("O", 10, "black")
            self.color = (218, 112, 214)
            self.run = True
            self.text1 = self.font.render("Ostrich Catch", 10, "black")
            self.text3 = self.font.render("Z to reset", 10, "black")
            self.moleCoordinates = []
            
            self.createMole = pygame.event.custom_type()
            pygame.time.set_timer(self.createMole, 1100)
            
            self.destroyMole = pygame.event.custom_type()
            pygame.time.set_timer(self.destroyMole, 3300)
            
            self.mole = pygame.transform.scale(pygame.image.load("mole.png"), (self.playerWidth + 50, self.playerHeight + 30))
            mixer.music.load("fryingPanAudio.mp3")
            
            while self.run:
                text2 = self.font.render("Score: " + str(self.score), 10, "black")
                
                self.screen.fill(self.color)
                self.screen.blit(self.bigText, (self.width/4 - self.text1.get_width()/2, self.height - 80 - self.text1.get_height()/2))
                self.screen.blit(self.homeIconUi, (25, (self.height-75)))
                self.screen.blit(self.text1, (self.width/2 - self.text1.get_width()/2, self.height - 50 - self.text1.get_height()/2))
                self.screen.blit(text2, (self.width/2 - text2.get_width()/2, 25 ))
                self.screen.blit(self.text3, (self.width - 980, self.height - 600))
                
                keys = pygame.key.get_pressed()
                if keys[pygame.K_z]:
                    self.moleCoordinates.clear()
                    self.score = 0
                
                for molCoord in self.moleCoordinates:
                    if len(self.moleCoordinates) > 0:
                        self.screen.blit(self.mole, molCoord)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == self.createMole:
                        if len(self.moleCoordinates) < 4:
                            moleCoords = (random.randint(0, self.width - (self.playerWidth + 50)), random.randint(25, self.height - 125 ))
                            self.moleCoordinates.append(moleCoords)
                    elif event.type == self.destroyMole:
                        if len(self.moleCoordinates) > 0:
                            del self.moleCoordinates[0]
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.checkClick(self.homeIconButton):
                            return "home"
                        for i in self.moleCoordinates:
                            if ((i[0] <= pygame.mouse.get_pos()[0] <= (i[0] + (self.playerWidth + 50))) and (i[1] <= pygame.mouse.get_pos()[1] <= (i[1] + (self.playerHeight + 30)))):
                                self.score = self.score + 1
                                self.moleCoordinates.remove(i)
                                mixer.music.play()
                pygame.display.update()
        pygame.quit()

#Start Game
if __name__ == "__main__":
    game = O1Game()
    game.runGame()

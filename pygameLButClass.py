import pygame

class LGame:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1000, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.stage = 0
        
        pygame.font.init()
        self.font = pygame.font.SysFont("comicsans", 30)
        self.font1 = pygame.font.SysFont("arial", 13)
        self.font2 = pygame.font.SysFont("comicsans", 75)

        self.blueButton = pygame.Surface((80, 40))
        self.blueButton.fill((0, 0, 255))
        self.buttonColor = "B"
        self.blueButtonCords = (100, 100)
        self.playerColor = "red"

        self.brushButton = pygame.Rect(900, 100, 24, 24)

        self.homeIconUi = pygame.transform.scale(pygame.image.load("homeIcon.jpg"), (50, 50))
        self.homeIconButton = pygame.Rect(25, self.height - 75, 50, 50)

        self.screen.fill((235, 230, 250))
        pygame.image.save(self.screen, "screenshot1.png")
        self.screenie = pygame.transform.scale(pygame.image.load("screenshot1.png"), (self.width, self.height))

        self.player = pygame.Rect((300, 250, 50, 50))
        self.playerVel = 1

        self.drawType = "keyboard"
        self.drawPlayer = "rect"
        self.drawBrushButton = "circle"
        self.color = (235, 230, 250)
        self.run = True
        self.text1 = self.font.render("Layout Likeness", 10, "black")
        self.text2 = self.font1.render("Z to reset", 10, "black")
        self.text3 = self.font1.render("G to toggle drawing", 10, "black")
        self.text4 = self.font1.render("Click the box to change color", 10, "black")
        self.text5 = self.font1.render("1 to switch from arrow keys to mouse controlling", 10, "black")
        self.text6 = self.font1.render("Click the circle/square to change the brush", 10, "black")
        self.bigText = self.font2.render("L", 10, "black")

        self.write = False
        self.drawingGameUi()

    def drawingGameUi(self):
        self.drawingGameUI = pygame.transform.scale(pygame.image.load("LayoutNEW.png"), (300, 200))
        self.drawingGameButton = pygame.Rect((695, 50, 300, 200))

    def coloredButton(self):
        if self.buttonColor == "R":
            self.blueButton.fill((0, 0, 255))
            self.buttonColor = "B"
            self.playerColor = "red"
        elif self.buttonColor == "B":
            self.blueButton.fill((0, 255, 0))
            self.buttonColor = "G"
            self.playerColor = "blue"
        elif self.buttonColor == "G":
            self.blueButton.fill((160, 32, 240))
            self.buttonColor = "P"
            self.playerColor = "green"
        elif self.buttonColor == "P":
            self.blueButton.fill((255, 165, 0))
            self.buttonColor = "OR"
            self.playerColor = "purple"
        elif self.buttonColor == "OR":
            self.blueButton.fill((255, 0, 0))
            self.buttonColor = "R"
            self.playerColor = "orange"

    def checkClick(self, button):
        mousePos = pygame.mouse.get_pos()
        return button.collidepoint(mousePos)

    def handEvents(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.checkClick(self.homeIconButton):
                    return "home"
                if self.checkClick(self.blueButton.get_rect(topleft=self.blueButtonCords)):
                    self.coloredButton()
                if self.checkClick(self.brushButton):
                    if self.drawPlayer == "rect":
                        self.drawPlayer = "circle"
                        self.drawBrushButton = "rect"
                    else:
                        self.drawPlayer = "rect"
                        self.drawBrushButton = "circle"
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_g:
                    if self.write:
                        pygame.image.save(self.screen, "screenshot1.png")
                        self.screenie = pygame.transform.scale(pygame.image.load("screenshot1.png"), (self.width, self.height))
                        self.write = False
                    else:
                        self.write = True
                if event.key == pygame.K_1:
                    self.drawType = "mouse" if self.drawType == "keyboard" else "keyboard"

        if keys[pygame.K_z]:
            self.screen.fill(self.color)
            pygame.image.save(self.screen, "screenshot1.png")
            self.screenie = pygame.transform.scale(pygame.image.load("screenshot1.png"), (self.width, self.height))

        if keys[pygame.K_LEFT] and self.player.x - self.playerVel >= 0:
            self.player.x -= self.playerVel
        if keys[pygame.K_RIGHT] and self.player.x + self.playerVel + self.player.width <= self.width:
            self.player.x += self.playerVel
        if keys[pygame.K_UP] and self.player.y - self.playerVel >= 0:
            self.player.y -= self.playerVel
        if keys[pygame.K_DOWN] and self.player.y + self.playerVel + self.player.height <= self.height:
            self.player.y += self.playerVel

    def draw(self):
        if not self.write:
            self.screen.blit(self.screenie, (0, 0))

        if self.drawBrushButton == "rect":
            pygame.draw.rect(self.screen, self.playerColor, self.brushButton)
        elif self.drawBrushButton == "circle":
            pygame.draw.circle(self.screen, self.playerColor, (self.brushButton.x + 12, self.brushButton.y + 12), 12)

        if self.drawType == "mouse":
            x, y = pygame.mouse.get_pos()
            if self.drawPlayer == "rect":
                pygame.draw.rect(self.screen, self.playerColor, (x, y, 50, 50))
            elif self.drawPlayer == "circle":
                pygame.draw.circle(self.screen, self.playerColor, (x, y), 12)
        elif self.drawType == "keyboard":
            if self.drawPlayer == "rect":
                pygame.draw.rect(self.screen, self.playerColor, self.player)
            elif self.drawPlayer == "circle":
                pygame.draw.circle(self.screen, self.playerColor, (self.player.x, self.player.y), 12)

        self.screen.blit(self.blueButton, self.blueButtonCords)
        self.screen.blit(self.text1, (self.width // 2 - self.text1.get_width() // 2, self.height - 50 - self.text1.get_height() // 2))
        self.screen.blit(self.text2, (self.width - 980, self.height - 600))
        self.screen.blit(self.text3, (self.width - 980, self.height - 580))
        self.screen.blit(self.text4, (self.width - 980, self.height - 560))
        self.screen.blit(self.text5, (self.width - 980, self.height - 540))
        self.screen.blit(self.text6, (self.width - 980, self.height - 520))
        self.screen.blit(self.bigText, (self.width // 4 - self.text1.get_width() // 2, self.height - 80 - self.text1.get_height() // 2))
        self.screen.blit(self.homeIconUi, (25, self.height - 75))

    def runGame(self):
        while self.run:
            self.handEvents()
            self.draw()
            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    game = LGame()
    game.runGame()

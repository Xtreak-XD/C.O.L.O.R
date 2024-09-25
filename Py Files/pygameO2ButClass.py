import pygame

class OGame:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        
        self.w, self.h = 1280, 720
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.clock = pygame.time.Clock()
        self.bgColor = (255, 165, 0)
        
        self.run = True
        
        self.circleSize = 15
        self.hitboxOffset = 5
        self.hitboxSize = self.circleSize * 2 + self.hitboxOffset * 2
        self.circleX = 15
        self.circleY = self.h - 50 - self.circleSize
        
        self.jump = False
        self.jumpMax = 20
        self.jumpCount = 0
        self.levels = []
        self.teleports = []
        self.secondTeleports = []
        
        self.font1 = pygame.font.SysFont("comicsans", 30)
        self.winText = self.font1.render("You Won, Congrats, Thanks for trying our code!", 10, "white")
        self.bigText = self.font1.render("O", 50, "white")
        self.text1 = self.font1.render("Obby Escape", 10, "white")
        
        self.homeIconUi = pygame.transform.scale(pygame.image.load("homeIcon.jpg"), (50, 50))
        self.homeIconButton = pygame.Rect(25, self.h - 75, 50, 50)
        
        self.levelMaker()
        self.teleport()

    def levelMaker(self):
        self.win = pygame.Rect(300, 15, 55, 60)
        self.levels.append(self.win)
        self.ogFloorY = self.h - 60
        floor = pygame.Rect(0, self.ogFloorY, self.w, 60)
        self.levels.append(floor)
        jump1 = pygame.Rect(125, 540, 60, 60)
        self.levels.append(jump1)
        jump2 = pygame.Rect(275, 480, 60, 60)
        self.levels.append(jump2)
        jump3 = pygame.Rect(0, 380, 160, 60)
        self.levels.append(jump3)
        path1 = pygame.Rect(300, 76, self.w - 300, 10)
        self.levels.append(path1)
        plat1y = pygame.Rect(280, 0, 20, 86)
        self.levels.append(plat1y)
        squarew = pygame.Rect(0, 310, 450, 19)
        self.levels.append(squarew)
        squarey = pygame.Rect(450, 310, 19, self.h - 319)
        self.levels.append(squarey)
        platform1 = pygame.Rect(self.w - 100, self.h - 123, 100, 10)
        self.levels.append(platform1)
        platform2 = pygame.Rect(self.w - 230, self.h - 180, 40, 40)
        self.levels.append(platform2)
        platform3 = pygame.Rect(self.w - 300, self.h - 315, 40, 40)
        self.levels.append(platform3)
        platform4 = pygame.Rect(self.w - 400, self.h - 380, 40, 40)
        self.levels.append(platform4)
        platform5 = pygame.Rect(self.w - 530, self.h - 230, 40, 40)
        self.levels.append(platform5)
        platform6 = pygame.Rect(self.w - 640, self.h - 320, 40, 40)
        self.levels.append(platform6)
        platform7 = pygame.Rect(469, 310, 51, 19)
        self.levels.append(platform7)
        platform8 = pygame.Rect(200, 180, 40, 40)
        self.levels.append(platform8)
        platform9 = pygame.Rect(0, 100, 155, 40)
        self.levels.append(platform9)

    def checkClick(self, button):
        mousePos = pygame.mouse.get_pos()
        return button.collidepoint(mousePos)

    def teleport(self):
        bTeleport = "pink", pygame.Rect(0, 380, 20, 5)
        self.teleports.append(bTeleport)
        bTeleport2 = "pink", pygame.Rect(self.w - 20, self.h - 123, 20, 5)
        self.secondTeleports.append(bTeleport2)
        aTeleport = "yellow", pygame.Rect(0, 100, 20, 5)
        self.teleports.append(aTeleport)
        aTeleport2 = "yellow", pygame.Rect(self.w - 25, 76, 20, 5)
        self.secondTeleports.append(aTeleport2)

    def teleportTo(self, hitbox, index):
        for _ in range(len(self.teleports)):
            hitbox.x, hitbox.y = self.secondTeleports[index][1].x, self.secondTeleports[index][1].y
            self.circleX, self.circleY = hitbox.x, hitbox.y

    def collision(self, hitbox):
        for obstacle in self.levels:
            if not obstacle == self.win:
                if hitbox.colliderect(obstacle):
                    if hitbox.bottom >= obstacle.top and hitbox.top <= obstacle.top:
                        hitbox.bottom = obstacle.top
                        self.circleY = hitbox.centery
                    elif hitbox.right >= obstacle.left and hitbox.left <= obstacle.left:
                        hitbox.right = obstacle.left
                        self.circleX = hitbox.centerx
                    elif hitbox.left <= obstacle.right and hitbox.right >= obstacle.right:
                        hitbox.left = obstacle.right
                        self.circleX = hitbox.centerx
                    elif hitbox.top <= obstacle.bottom:
                        hitbox.top = obstacle.bottom
                        self.circleY = hitbox.centery
                        self.jump = False

    def runGame(self):
        while self.run:
            self.clock.tick(60)
            self.screen.fill(self.bgColor)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.checkClick(self.homeIconButton):
                        self.screen = pygame.display.set_mode((1000, 600))
                        return "home"
                elif event.type == pygame.KEYDOWN:
                    if not self.jump and event.key == pygame.K_UP:
                        self.jump = True
                        self.jumpCount = self.jumpMax

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.circleX -= 5
            if keys[pygame.K_RIGHT]:
                self.circleX += 5
            if self.jump:
                self.circleY -= self.jumpCount
                if self.jumpCount > -self.jumpMax:
                    self.jumpCount -= 1
                else:
                    self.jump = False

            hitbox = pygame.Rect(self.circleX - self.circleSize - self.hitboxOffset,
                                  self.circleY - self.circleSize - self.hitboxOffset,
                                  self.hitboxSize, self.hitboxSize)
            for i in self.teleports:
                if hitbox.colliderect(i[1]):
                    index = self.teleports.index(i)
                    self.teleportTo(hitbox, index)

            self.collision(hitbox)

            check = False
            for obstacle in self.levels:
                if hitbox.colliderect(obstacle):
                    check = True
            if check == False:
                hitbox.y += 5
                self.circleY += 5

            if self.circleX < 0:
                self.circleX = 0
            elif self.circleX > self.w:
                self.circleX = self.w

            for obstacle in self.levels:
                pygame.draw.rect(self.screen, "black", obstacle)
                if obstacle == self.win:
                    pygame.draw.rect(self.screen, "green", obstacle)
                    if hitbox.colliderect(obstacle):
                        self.screen.blit(self.winText, (self.w / 2 - self.winText.get_width() / 2,
                        self.h / 2 - self.winText.get_height() / 2))
                        pygame.display.update()
                        pygame.time.delay(2000)
                        self.w, self.h = 1000, 600
                        self.screen = pygame.display.set_mode((1000, 600))
                        return "home"
            for numTeleport in self.teleports:
                pygame.draw.rect(self.screen, numTeleport[0], numTeleport[1])
            for numTeleport in self.secondTeleports:
                pygame.draw.rect(self.screen, numTeleport[0], numTeleport[1])
            
            self.screen.blit(self.homeIconUi, (15, (self.h-60)))
            self.screen.blit(self.bigText, (self.w/4 - self.text1.get_width()/2 - 75, self.h- 40 - self.bigText.get_height()/2))
            self.screen.blit(self.text1, (self.w/2 - self.text1.get_width()/2, self.h-40 - self.text1.get_height()/2))
            
            pygame.draw.circle(self.screen, "pink", (self.circleX, self.circleY), self.circleSize)

            pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    game = OGame()
    game.runGame()
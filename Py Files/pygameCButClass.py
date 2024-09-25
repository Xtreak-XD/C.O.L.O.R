import pygame
import random
import math

class CGame:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.w, self.h = 1000, 600
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.clock = pygame.time.Clock()
        self.bgColor = (0, 255, 255)
        self.runGamening = True

        self.heart = pygame.image.load("Heart.png").convert_alpha()
        self.heartWidth = self.heart.get_width()

        self.scoreFont = pygame.font.SysFont("Public Pixel", 30)

        self.font = pygame.font.SysFont("Times New Roman", 60)
        self.beginText = self.font.render("Click To Begin Game", False, "Blue")
        self.beginTextRect = self.beginText.get_rect()
        self.beginTextRect.center = (self.w // 2, self.h // 2)

        self.foodSize = 7
        self.enemySize = 15
        self.enemySpeed = 1.5
        
        self.homeIconUi = pygame.transform.scale(pygame.image.load("homeIcon.jpg"), (50, 50))
        self.homeIconButton = pygame.Rect(25, self.h - 75, 50, 50)

        self.spawnFoods = pygame.USEREVENT + 1
        pygame.time.set_timer(self.spawnFoods, 2500)

        self.spawnEnemies = pygame.USEREVENT + 2
        pygame.time.set_timer(self.spawnEnemies, 4500)

        pygame.display.set_caption("Pygame Game")

        self.restartGame()

    def restartGame(self):
        self.gameStart = False
        self.playerHealth = 3
        self.score = 0
        self.size = 10
        self.circleX = self.w // 2
        self.circleY = self.h // 2
        self.foods = []
        self.enemies = []
        self.hearts = []

    def placeHearts(self):
        heartX = 10
        for i in range(self.playerHealth):
            self.hearts.append(self.heart)
        for _ in range(self.playerHealth):
            self.screen.blit(self.heart, (heartX, 10))
            heartX += 60

    def checkClick(self, button):
        mousePos = pygame.mouse.get_pos()
        return button.collidepoint(mousePos)

    def placeScore(self):
        scoreText = self.scoreFont.render("Score: " + str(self.score), False, "Black")
        scoreTextWidth = scoreText.get_width()
        scoreTextRect = scoreText.get_rect()
        scoreTextRect.center = (self.w // 2, self.h // 2)
        self.screen.blit(scoreText, ((self.w - scoreTextWidth) - 50, 30))

    def spawnEnemy(self):
        enemyX = random.randrange(self.w)
        enemyY = random.randrange(self.h)
        self.enemies.append(pygame.Rect(enemyX, enemyY, self.enemySize, self.enemySize))

    def spawnFood(self):
        foodX = random.randrange(self.w)
        foodY = random.randrange(self.h)
        self.foods.append(pygame.Rect(foodX, foodY, self.foodSize, self.foodSize))

    def eatFood(self):
        for food in self.foods:
            distance = math.hypot(food.centerx - self.circleX, food.centery - self.circleY)
            if distance <= self.foodSize + self.size:
                self.foods.remove(food)
                self.size += 2
                self.score += 1

    def enemyChase(self):
        for enemy in self.enemies:
            dx = self.circleX - enemy.centerx
            dy = self.circleY - enemy.centery
            angle = math.atan2(dy, dx)
            moveX = math.cos(angle) * self.enemySpeed
            moveY = math.sin(angle) * self.enemySpeed
            
            enemy.centerx += moveX
            enemy.centery += moveY

    def enemyCaughtYou(self):
        for enemy in self.enemies:
            distance = math.hypot(enemy.centerx - self.circleX, enemy.centery - self.circleY)
            if distance <= self.enemySize + self.size:
                self.enemies.remove(enemy)
                self.playerHealth -= 1
        return self.playerHealth

    def gameOver(self):
        rBFont = pygame.font.SysFont("Times New Roman", 30)
        rButton = rBFont.render("Restart", False, "red")
        rBRect = rButton.get_rect()
        rBRect.center = ((self.w // 2), (self.h // 2) + 20)
        rBRectangle = pygame.draw.rect(self.screen, "grey", pygame.Rect(rBRect[0] - 2, rBRect[1] - 2, rBRect[2] + 5, rBRect[3] + 5))
        self.screen.blit(rButton, rBRect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    if rBRectangle.collidepoint(mousePos):
                        return True
            pygame.display.update()
    
    def runGame(self):
        while self.runGamening:
            self.screen.fill(self.bgColor)
            self.screen.blit(self.beginText, self.beginTextRect)
            self.screen.blit(self.homeIconUi, (25, (self.h-75)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.checkClick(self.homeIconButton):
                        return "home"
                    if self.gameStart:
                        continue
                    self.gameStart = True
                    self.beginText = self.font.render("", False, "Pink")
                elif event.type == self.spawnFoods:
                    if self.gameStart:
                        self.spawnFood()
                elif event.type == self.spawnEnemies:
                    if self.gameStart:
                        self.spawnEnemy()

            if self.gameStart:
                self.placeHearts()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.circleX -= 5
                if keys[pygame.K_RIGHT]:
                    self.circleX += 5
                if keys[pygame.K_UP]:
                    self.circleY -= 5
                if keys[pygame.K_DOWN]:
                    self.circleY += 5

                circle1 = pygame.draw.circle(self.screen, "blue", (self.circleX, self.circleY), self.size)

                for food in self.foods:
                    foodSpawned = pygame.draw.circle(self.screen, "yellow", food.center, self.foodSize)

                for enemy in self.enemies:
                    enemySpawned = pygame.draw.rect(self.screen, "red", enemy)

                if self.playerHealth == 0:
                    continue

                self.eatFood()
                self.placeScore()
                self.enemyChase()
                self.enemyCaughtYou()

            if self.playerHealth == 0:
                self.gameStart = False
                loosingText = self.font.render("You have lost all lives", False, "Red")
                loosingTextRect = loosingText.get_rect()
                loosingWidth = loosingText.get_width()
                loosingHeight = loosingText.get_height()
                loosingTextRect.center = ((self.w // 2), (self.h // 2) - loosingHeight // 2)
                self.screen.blit(loosingText, loosingTextRect)
                if self.gameOver():
                    self.restartGame()
                    continue

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = CGame()
    game.runGame()

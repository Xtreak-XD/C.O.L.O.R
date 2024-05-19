import pygame
import random
from pygame import mixer
import math
mixer.init()

WIDTH,HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
stage = 0

pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 30)
FONT1 = pygame.font.SysFont("arial", 13)
FONT2 = pygame.font.SysFont("comicsans", 75)

blueButton = pygame.Surface((80 , 40)) 
blueButton.fill((0, 0, 255))
buttonColor = "B"
blueButtonCords = (100, 100)
playerColor = "red"

brushButton = pygame.Rect(900, 100, 24, 24)

screen.fill((255,255,255))
pygame.image.save(screen, "screenshot1.png")
screenie = pygame.transform.scale(pygame.image.load("screenshot1.png"), (WIDTH, HEIGHT))

player = pygame.Rect((300, 250 , 50, 50))
PLAYER_VEL = 1
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 40
write = False

def coloredButton(buttonColor):
    if buttonColor == "R":
        blueButton.fill((0, 0, 255))
        buttonColor = "B"
        return "red", buttonColor
    elif buttonColor == "B":
        blueButton.fill((0,255,0))
        buttonColor = "G"
        return "blue", buttonColor
    elif buttonColor == "G":
        blueButton.fill((160, 32, 240))
        buttonColor = "P"
        return "green", buttonColor
    elif buttonColor == "P":
        blueButton.fill((255, 165, 0))
        buttonColor = "OR"
        return "purple", buttonColor
    elif buttonColor == "OR":
        blueButton.fill((255, 0, 0))
        buttonColor = "R"
        return "orange", buttonColor

def checkClick(button):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if ((button.x <= pygame.mouse.get_pos()[0] <= (button.x + button.width)) and (button.y <= pygame.mouse.get_pos()[1] <= (button.y + button.height))):
            return True

# Load images
homeIconUi = pygame.transform.scale(pygame.image.load("homeIcon.jpg"), (50, 50))
whackAMoleUi = pygame.transform.scale(pygame.image.load("ostrichNEW.png"), (300, 200))
drawingGameUi = pygame.transform.scale(pygame.image.load("LayoutNEW.png"), (300, 200))
dodgeRainDropsUi = pygame.transform.scale(pygame.image.load("rainNEW.png"), (300, 200))
agarioGameUi = pygame.transform.scale(pygame.image.load("chaseNEW.png"), (300, 200))

# Create buttons
homeIconButton = pygame.Rect(25, HEIGHT - 75, 50, 50)
whackAMoleButton = pygame.Rect(360, 50, 300, 200)
drawingGameButton = pygame.Rect(695, 50, 300, 200)
raindropsButton = pygame.Rect(360, HEIGHT - 250, 300, 200)
agarioButton = pygame.Rect(25, 50, 300, 200)

rainbow = pygame.transform.scale(pygame.image.load("rainbow.jpg"), (WIDTH, HEIGHT))

completegameloop = True
while completegameloop:
    if stage == 0:
        
        screen.blit(rainbow, (0,0))
        screen.blit(whackAMoleUi, (360, 50))
        screen.blit(drawingGameUi, (695, 50))
        screen.blit(dodgeRainDropsUi, (360, HEIGHT - 250))
        screen.blit(agarioGameUi, (25,50))
        screen.blit(homeIconUi, (25,(HEIGHT-75)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if checkClick(whackAMoleButton) == True:
                stage = 3
            if checkClick(drawingGameButton) == True:
                stage = 1
            if checkClick(raindropsButton) == True:
                stage = 4
            if checkClick(agarioButton) == True:
                stage = 2

        pygame.display.update()

    if stage == 1:
        drawtype = "keyboard"
        drawPlayer = "rect" 
        drawBrushButton = "circle"
        color = (255, 255, 255)
        run = True
        text1 = FONT.render("Layout Likeness", 10, "black")
        text2 = FONT1.render("Z to reset", 10, "black")
        text3 = FONT1.render("G to toggle drawing", 10, "black")
        text4 = FONT1.render("Click the box to change color", 10, "black")
        text5 = FONT1.render("1 to switch from arrow keys to mouse controlling",10,"black")
        text6 = FONT1.render("Click the circle/square to change the brush",10,"black")
        bigtext = FONT2.render("L", 10, "black")

        while run:

            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:
                screen.fill(color)
                pygame.image.save(screen, "screenshot1.png")
                screenie = pygame.transform.scale(pygame.image.load("screenshot1.png"), (WIDTH, HEIGHT))

            if write == False:
                screen.blit(screenie, (0,0))

            if drawBrushButton == "rect":
                pygame.draw.rect(screen, playerColor, (900, 100, 24, 24))
            elif drawBrushButton == "circle":
                pygame.draw.circle(screen, playerColor, (914, 114), 12)

            if drawtype == "mouse":                     
                if drawPlayer == "rect":
                    pygame.draw.rect(screen, playerColor, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 50, 50))
                elif drawPlayer == "circle":
                    pygame.draw.circle(screen, playerColor, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 12)
            elif drawtype == "keyboard":
                if drawPlayer == "rect":
                    pygame.draw.rect(screen, playerColor, player)
                elif drawPlayer == "circle":
                    pygame.draw.circle(screen, playerColor, (player.x, player.y), 12)

            screen.blit(blueButton, blueButtonCords)

            screen.blit(homeIconUi, (25,(HEIGHT-75)))
            
            screen.blit(text1, (WIDTH/2 - text1.get_width()/2, HEIGHT-50 - text1.get_height()/2))
            screen.blit(text2, (WIDTH - 980, HEIGHT - 600))
            screen.blit(text3, (WIDTH - 980, HEIGHT - 580))
            screen.blit(text4, (WIDTH - 980, HEIGHT - 560))
            screen.blit(text5, (WIDTH - 980, HEIGHT - 540))
            screen.blit(text6, (WIDTH - 980, HEIGHT - 520))
            screen.blit(bigtext, (WIDTH/4 - text1.get_width()/2, HEIGHT- 80 - text1.get_height()/2))
            

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL
            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
                player.x += PLAYER_VEL
            if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
                player.y -= PLAYER_VEL
            if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.width <= HEIGHT:
                player.y += PLAYER_VEL

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if (event.type == pygame.MOUSEBUTTONDOWN) and ((blueButtonCords[0] <= pygame.mouse.get_pos()[0] <= (blueButtonCords[0] + 80)) and (blueButtonCords[1] <= pygame.mouse.get_pos()[1] <= (blueButtonCords[1] + 40))):
                    playerColor, buttonColor = coloredButton(buttonColor)
                if event.type == pygame.KEYUP and event.key == pygame.K_g:
                    if write == True:
                        pygame.image.save(screen, "screenshot1.png")
                        screenie = pygame.transform.scale(pygame.image.load("screenshot1.png"), (WIDTH, HEIGHT))
                        write = False
                    elif write == False:
                        write = True
                if checkClick(homeIconButton) == True:
                    stage = 0 
                    run = False
                if checkClick(brushButton) == True:
                    if drawPlayer == "rect":
                        drawPlayer = "circle"
                        drawBrushButton = "rect"
                    elif drawPlayer == "circle":
                        drawPlayer = "rect"
                        drawBrushButton = "circle"
                if keys[pygame.K_1] and event.type == pygame.KEYUP:
                    if drawtype == "keyboard":
                        drawtype = "mouse"
                    elif drawtype == "mouse":
                        drawtype = "keyboard"

            pygame.display.update()

    if stage == 2:
        clock = pygame.time.Clock()
        
        text1 = FONT.render("Chase block", 10, "black")
        bigtext = FONT2.render("C", 10, "black")

        running = True

        heart = pygame.image.load("Heart.png").convert_alpha()
        heartWidth = heart.get_width()

        scoreFont = pygame.font.SysFont("Public Pixel", 30)

        font = pygame.font.SysFont("Times New Roman", 60)
        beginText = font.render("Click To Begin Game", False, "Blue")
        beginTextRect = beginText.get_rect()
        beginTextRect.center = (WIDTH // 2, HEIGHT // 2)

        foodSize = 7
        enemySize = 15
        enemySpeed = 1.5

        spawnFoods = pygame.USEREVENT + 1
        pygame.time.set_timer(spawnFoods, 2500)

        spawnEnemies = pygame.USEREVENT + 2
        pygame.time.set_timer(spawnEnemies, 4500)

        pygame.display.set_caption("Pygame Game")

        def restartGame():
            global gameStart, playerHealth, score, size, circleX, circleY, foods, enemies, hearts
            gameStart = False
            playerHealth = 3
            score = 0
            size = 10
            circleX = WIDTH // 2
            circleY = HEIGHT // 2
            foods = []
            enemies = []
            hearts = []

        def placeHearts():
            heartX = 10
            for i in range(3):
                hearts.append(heart)
            for _ in range(playerHealth):
                screen.blit(heart, (heartX, 10))
                heartX += 60

        def placeScore(score):
            scoreText = scoreFont.render("Score: " + str(score), False, "Black")
            scoreTextWidth = scoreText.get_width()
            scoreTextRect = scoreText.get_rect()
            scoreTextRect.center = (WIDTH // 2, HEIGHT // 2)
            screen.blit(scoreText, ((WIDTH - scoreTextWidth) - 50, 30))

        def spawnEnemy():
            enemyX = random.randrange(WIDTH)
            enemyY = random.randrange(HEIGHT)
            enemies.append(pygame.Rect(enemyX, enemyY, enemySize, enemySize))

        def spawnFood():
            foodX = random.randrange(WIDTH)
            foodY = random.randrange(HEIGHT)
            foods.append(pygame.Rect(foodX, foodY, foodSize, foodSize))

        def eatFood():
            global size, score
            for food in foods:
                distance = math.hypot(food.centerx - circleX, food.centery - circleY)
                if distance <= foodSize + size:  # Collision detected
                    mixer.music.load("nom-nom-nom_gPJiWn4.mp3")
                    mixer.music.play(0)
                    foods.remove(food)
                    size += 2
                    score += 1

        def enemyChase():
            for enemy in enemies:  # This code is from Revernos Technology on YouTube, lord and savior Revernos
                dx = circleX - enemy.centerx  # magnitudes of the vectors
                dy = circleY - enemy.centery
                # Calculates the position of the player relative to the enemies
                angle = math.atan2(dy, dx)
                moveX = math.cos(angle) * enemySpeed
                moveY = math.sin(angle) * enemySpeed
                
                enemy.centerx += moveX
                enemy.centery += moveY

        def enemyCaughtYou():
            global playerHealth
            for enemy in enemies:
                distance = math.hypot(enemy.centerx - circleX, enemy.centery - circleY)
                if distance <= enemySize + size:  # Collision detected
                    mixer.music.load("classic_hurt.mp3")                    
                    mixer.music.play(1)
                    enemies.remove(enemy)
                    playerHealth -= 1
            return playerHealth

        def gameOver():
            global running
            rBFont = pygame.font.SysFont("Times New Roman", 30)
            rButton = rBFont.render("Restart", False, "red")
            rBRect = rButton.get_rect()
            rBRect.center = ((WIDTH // 2), (HEIGHT // 2) + 20)
            rBRectangle = pygame.draw.rect(screen, "grey", pygame.Rect(rBRect[0] - 2, rBRect[1] - 2, rBRect[2] + 5, rBRect[3] + 5))
            screen.blit(rButton, rBRect)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mousePos = pygame.mouse.get_pos()
                        if rBRectangle.collidepoint(mousePos):
                            return True  # Indicate that the game should restart
                pygame.display.update()

        restartGame()
        while running:
            screen.fill("pink")
            screen.blit(beginText, beginTextRect)
            screen.blit(homeIconUi, (25,(HEIGHT-75)))
            screen.blit(text1, (WIDTH/2 - text1.get_width()/2, HEIGHT- 50 - text1.get_height()/2))
            screen.blit(bigtext, (WIDTH/4 - text1.get_width()/2, HEIGHT- 80 - text1.get_height()/2))
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if checkClick(homeIconButton) == True:
                        print("working")
                        stage = 0 
                        running = False
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if gameStart:
                        continue
                    gameStart = True
                    beginText = font.render("", False, "Pink")
                    
                elif event.type == spawnFoods:
                    if gameStart:
                        spawnFood()
                        
                elif event.type == spawnEnemies:
                    if gameStart:
                        spawnEnemy()

            if gameStart:
                placeHearts()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    circleX -= 5
                if keys[pygame.K_RIGHT]:
                    circleX += 5
                if keys[pygame.K_UP]:
                    circleY -= 5
                if keys[pygame.K_DOWN]:
                    circleY += 5

                circle1 = pygame.draw.circle(screen, "blue", (circleX, circleY), size)

                for food in foods:
                    foodSpawned = pygame.draw.circle(screen, "yellow", food.center, foodSize)

                for enemy in enemies:
                    enemySpawned = pygame.draw.rect(screen, "red", enemy)

                if playerHealth == 0:
                    continue

                eatFood()
                placeScore(score)
                enemyChase()
                enemyCaughtYou()

            if playerHealth == 0:
                gameStart = False
                loosingText = font.render("You have lost all lives", False, "Red")
                loosingTextRect = loosingText.get_rect()
                loosingWidth = loosingText.get_width()
                loosingHeight = loosingText.get_height()
                loosingTextRect.center = ((WIDTH // 2), (HEIGHT // 2) - loosingHeight // 2)
                screen.blit(loosingText, loosingTextRect)
                if gameOver():
                    restartGame()
                    continue

            # display and update certain portions of the screen
            pygame.display.update()

            clock.tick(60)  # limits FPS to 60

    if stage == 3:
        bigtext = FONT2.render("O", 10, "black")
        color = ((100, 200, 100))
        score = 0 
        run = True
        text1 = FONT.render("Ostrich Catch", 10, "black")
        text3 = FONT.render("Z to reset", 10, "black")
        moleCoordinates = []

        create_mole = pygame.event.custom_type()
        pygame.time.set_timer(create_mole, 1100)

        destroy_mole = pygame.event.custom_type()
        pygame.time.set_timer(destroy_mole, 3300)

        mole = pygame.transform.scale(pygame.image.load("mole.png"), (PLAYER_WIDTH + 50, PLAYER_HEIGHT + 30))
        mixer.music.load("fryingPanAudio.mp3")

        while run:
            
            text2 = FONT.render("Score: " + str(score), 10, "black")

            screen.fill(color)
            screen.blit(bigtext, (WIDTH/4 - text1.get_width()/2, HEIGHT- 80 - text1.get_height()/2))
            
            screen.blit(text1, (WIDTH/2 - text1.get_width()/2, HEIGHT- 50 - text1.get_height()/2))
            screen.blit(text2, (WIDTH/2 - text2.get_width()/2, 25 ))
            screen.blit(text3, (WIDTH - 980, HEIGHT - 600))
            screen.blit(homeIconUi, (25,(HEIGHT-75)))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:
                moleCoordinates.clear()
                score = 0

            for molcoord in moleCoordinates:
                if len(moleCoordinates) > 0:
                    screen.blit(mole,(molcoord))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == create_mole:
                    if len(moleCoordinates) < 4:
                        moleCoords = (random.randint(0, WIDTH - (PLAYER_WIDTH + 50)), random.randint(25, HEIGHT - 125 ))
                        moleCoordinates.append(moleCoords)
                if event.type == destroy_mole:
                    if len(moleCoordinates) > 0:
                        del moleCoordinates[0]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in moleCoordinates:
                        if ((i[0] <= pygame.mouse.get_pos()[0] <= (i[0] + (PLAYER_WIDTH + 50))) and (i[1] <= pygame.mouse.get_pos()[1] <= (i[1] + (PLAYER_HEIGHT + 30)))):
                            score = score + 1
                            moleCoordinates.remove(i)
                            mixer.music.play()
                if checkClick(homeIconButton) == True:
                    run = False
                    stage = 0 
            pygame.display.update()

    if stage == 4: 
        bigtext = FONT2.render("R", 10, "red")
        
        raindropspeed = 75
        raindrops = []
        droplet = pygame.transform.scale(pygame.image.load("drop.png"), (16, 18))
        seconds = 0 
        startTicks = pygame.time.get_ticks()
        run = True
        color = (25, 25, 25)
        text1  = FONT.render("Dodge the Raindrops", 10, "black")
        text2 = FONT.render("YOU LOSE", 10, "white")
        rainfall = pygame.event.custom_type()
        pygame.time.set_timer(rainfall, raindropspeed)
        clock = pygame.time.Clock()

        while run:
            screen.fill(color)
            screen.blit(text1, (WIDTH/2 - text1.get_width()/2, HEIGHT- 50 - text1.get_height()/2))
            screen.blit(homeIconUi, (25,(HEIGHT-75)))
            screen.blit(bigtext, (WIDTH/4 - text1.get_width()/2, HEIGHT- 80 - text1.get_height()/2))

            (playerX, playerY) = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (0,0,55), (playerX, playerY), 15)

            milliseconds = (pygame.time.get_ticks() - startTicks)
            
            seconds = milliseconds // 1000
            text3 = FONT.render((f'Time Alive: {seconds}'), True, (0,0,0))
            screen.blit(text3, ((WIDTH/2 - text3.get_width()/2), 40))
            clock.tick(60)
            if seconds > 15:
                raindropspeed = 35
            if seconds  > 25:
                raindropspeed = 10
            
            for i, dropcoords in enumerate(raindrops):
                dropcoords = list(dropcoords)
                dropcoords[1] += 5
                raindrops[i] = tuple(dropcoords)
                screen.blit(droplet, raindrops[i])
                if (dropcoords[0] - 15 <= pygame.mouse.get_pos()[0] <= dropcoords[0] + 16+15)  and (dropcoords[1] -15 <= pygame.mouse.get_pos()[1]<= dropcoords[1]+ 12+15):
                    screen.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT/2 - text2.get_height()/2))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    run = False
                    stage = 0        

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if checkClick(homeIconButton) == True:
                    run = False
                    stage = 0 
                if event.type == rainfall:
                    rainfallCOORD = (random.randint(0, WIDTH ), 0)
                    raindrops.append((rainfallCOORD))

            pygame.display.update()
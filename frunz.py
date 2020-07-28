import pygame
from random import randint

pygame.init()

class Dima():
    def __init__(self, screen):
        self.screen = screen
        self.image2 = pygame.image.load('images/Д.png')
        self.draw = True
        self.x = randint(100, 650)
        self.y = randint(0, 640)

    def snack(self):
        if self.draw == True:
            self.screen.blit(self.image2, (self.x,self.y))

class Frunz():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/Ф.png')
        self.image1 = pygame.image.load('images/Ф1.png')
        self.image2 = pygame.image.load('images/Ф2.png')
        self.x1 = 300
        self.y1 = 690
        self.x = 300
        self.y = 300
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        self.level = False
        self.pre = True
        self.count = 0
        self.speed = 0.5


        self.score = 0
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render("Play", 1, (200, 200, 200))

    def start(self):
        if self.pre:
            self.screen.blit(self.image, (self.x1, self.y1))
            if self.y1 < 310:
                self.screen.blit(self.text, (320, 435))
            if self.y1 > 300:
                self.y1 -= 0.4

    def moving(self):
        if self.level:
            if self.move_up and self.move_down == False:
                self.y -= self.speed
            if self.move_down and self.move_up == False:
                self.y += self.speed
            if self.move_left and self.move_right == False:
                self.x -= self.speed
            if self.move_right and self.move_left == False:
                self.x += self.speed
            if self.y < -125:
                self.y = 690
            if self.y > 690:
                self.y = -125
            if self.x < 20:
                self.x = 700
            if self.x > 700:
                self.x = 20



    def cube(self):
        if self.count//100 == 0:
            self.screen.blit(self.image, (self.x, self.y))
        if self.count // 100 == 1:
            self.screen.blit(self.image1, (self.x, self.y))
        if self.count // 100 == 2:
            self.screen.blit(self.image2, (self.x, self.y))

class Snake():
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 690))
        self.image = pygame.image.load('images/Ф.png')
        pygame.display.set_icon(self.image)
        self.ruun = True
        self.frunz = Frunz(self.screen)
        self.dima = Dima(self.screen)

        self.score = 0
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render("Play", 1, (200, 200, 200))
        self.textscore = self.font.render((f"Очки: {self.score}") , 1, (0, 0, 0))
        self.mouse = pygame.mouse.get_pos()

    def scoreprint(self):
        self.screen.blit(self.textscore, (720, 50))

    def collis(self):
        if self.dima.x + 55 > self.frunz.x + 15 > self.dima.x or self.dima.x + 50 > self.frunz.x + 50 > self.dima.x:
            if self.dima.y + 75 > self.frunz.y + 20 > self.dima.y or self.dima.y + 70 > self.frunz.y + 80 > self.dima.y:
                self.dima.draw = False
                self.score += 1
                self.dima.x = randint(100, 600)
                self.dima.y = randint(0, 600)
                self.dima.draw = True
                self.frunz.count = 200
                self.textscore = self.font.render((f"Очки: {self.score}"), 1, (0, 0, 0))
                self.frunz.speed += 0.01

    def run(self):
        while self.ruun:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ruun = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.frunz.move_up = True
                        self.frunz.move_down = False
                        self.frunz.move_left = False
                        self.frunz.move_right = False
                    elif event.key == pygame.K_DOWN:
                        self.frunz.move_down = True
                        self.frunz.move_left = False
                        self.frunz.move_right = False
                        self.frunz.move_up = False
                    elif event.key == pygame.K_RIGHT:
                        self.frunz.move_right = True
                        self.frunz.move_down = False
                        self.frunz.move_left = False
                        self.frunz.move_up = False
                    elif event.key == pygame.K_LEFT:
                        self.frunz.move_left = True
                        self.frunz.move_right = False
                        self.frunz.move_down = False
                        self.frunz.move_up = False
                    elif event.key == pygame.K_RETURN:
                        self.frunz.level = True
                        self.frunz.pre = False
                    elif event.key == pygame.K_q:
                        self.dima.draw = False
                        self.score += 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.mouse[0] in (0, 100) and self.mouse[1] in (0,100):
                            self.frunz.level = True

            self.screen.fill((0, 0, 0))
            self.bg = pygame.draw.rect(self.screen, (120, 120, 120), (0, 0, 100, 690))
            self.bg2 = pygame.draw.rect(self.screen, (120, 120, 120), (700, 0, 600, 690))
            self.frunz.start()
            if self.frunz.level:
                self.frunz.moving()
                self.dima.snack()
                self.frunz.cube()
                self.collis()
                if self.frunz.count == 250:
                    self.frunz.count = 0
                if self.frunz.count == 199:
                    self.frunz.count = 0
                self.frunz.count += 1
                self.bg = pygame.draw.rect(self.screen, (120, 120, 120), (0, 0, 100, 690))
                self.bg2 = pygame.draw.rect(self.screen, (120, 120, 120), (700, 0, 600, 690))
                self.scoreprint()
            pygame.display.flip()

snake = Snake()
snake.run()
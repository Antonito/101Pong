#!/usr/bin/env python
import pygame, sys, math, random, time
from pygame.locals import *
difficulty = 2

try:
    import pygame
    import sys
    from pygame.locals import *
except ImportError, err:
    print "Error during import\n", err
    sys.exit(1)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if (len(sys.argv) == 2):
            if (sys.argv[1] == '--fernand'):
                self.image = pygame.image.load('images/ballf.bmp')
                self.rect = pygame.image.load('images/ballf.bmp').get_rect()
            else:
                self.image = pygame.image.load('images/ball.bmp')
                self.rect = pygame.image.load('images/ball.bmp').get_rect()
        else:
            self.image = pygame.image.load('images/ball.bmp')
            self.rect = pygame.image.load('images/ball.bmp').get_rect()
        if (difficulty == 1):
            self.speed = 5
        elif (difficulty == 2):
            self.speed = 8
        elif (difficulty == 3):
            self.speed = 15
        self.position = (498, 380)

class Bat(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        if (len(sys.argv) == 2):
            if (sys.argv[1] == '--fernand'):
                self.image = pygame.image.load('images/player.bmp')
                self.rect = pygame.image.load('images/player.bmp').get_rect()
            else:
                self.image = pygame.image.load('images/player.bmp')
                self.rect = pygame.image.load('images/player.bmp').get_rect()
        else:
            self.image = pygame.image.load('images/player.bmp')
            self.rect = pygame.image.load('images/player.bmp').get_rect()
        self.speed = 20
        self.position = (x, 300)
    def moveup(self):
        if (self.position[1] - self.speed < 25):
            self.position = (self.position[0], 40)
        else:
            self.position = (self.position[0], self.position[1] - self.speed)
    def movedown(self):
        if (self.position[1] + self.speed > 620):
            self.position = (self.position[0], 620)
        else:
            self.position = (self.position[0], self.position[1] + self.speed)

def menu(screen):
    fontT = pygame.font.Font(None, 36)
    fontH = pygame.font.Font(None, 52)
    fontE = pygame.font.Font(None, 45)
    fontS = pygame.font.Font(None, 30)

    title = fontH.render("PONG WITHOUT PING", 1, (255, 255, 255))
    by = fontT.render("By", 1, (255, 255, 255))
    ant = fontT.render("Antoine BACHE &", 1, (255, 255, 255))
    lud = fontT.render("Ludovic PETRENKO", 1, (255, 255, 255))
    ent = fontE.render("Press ENTER to start", 1, (255, 255, 255))
    ex = fontT.render("  ESCAPE to quit", 1, (255, 255, 255))
    opt = fontS.render("Press o for options", 1, (255, 255, 255))
    opt2 = fontS.render("and controls", 1, (255, 255, 255))

    screen.blit(title, (512, 150))
    screen.blit(by, (68, 660))
    screen.blit(ant, (80, 690))
    screen.blit(lud, (92, 720))
    screen.blit(ent, (300, 400))
    screen.blit(ex, (400, 440))
    screen.blit(opt, (800, 600))
    screen.blit(opt2, (820, 630))

def header_bar(screen, score1, score2):
    font = pygame.font.Font(None, 36)

    p1_text = font.render("Player 1", 1, (255, 255, 255))
    p1_score_text = font.render("%d" %score1, 1, (255, 255, 255))
    p2_text = font.render("Player 2", 1, (255, 255, 255))
    p2_score_text = font.render("%d" %score2, 1, (255, 255, 255))

    screen.blit(p1_text, (10, 0))
    screen.blit(p1_score_text, (480, 0))
    screen.blit(p2_score_text, (532, 0))
    screen.blit(p2_text, (920, 0))

def options_display(screen):
    fontT = pygame.font.Font(None, 36)
    fontH = pygame.font.Font(None, 48)
    fontE = pygame.font.Font(None, 45)
    
    OPT = fontH.render("OPTIONS", 1, (255, 255, 255))
    P1 = fontH.render("Player 1 (left) : Move with up and down arrows keys", 1, (255, 255, 255))
    P2 = fontH.render("Player 2 (right) : Move with z and s keys", 1, (255, 255, 255))
    escp = fontT.render("Escape : Quit game", 1, (255,255,255))
    rld = fontT.render("R : Restart a game", 1, (255,255,255))
    start = fontT.render("Enter : Start a game / Leave \"options\"", 1, (255,255,255))
    diff = fontH.render("Difficulty = %d" %difficulty, 1, (255, 255, 255))
    diff2 = fontT.render("(Press F1, F2 or F3)", 1, (255, 255, 255))

    screen.fill((0, 0, 0))
    screen.blit(OPT, (425, 50))
    screen.blit(P1, (51, 150))
    screen.blit(P2, (51, 260))
    screen.blit(diff, (51, 350))
    screen.blit(diff2, (56, 390))
    screen.blit(start, (51, 650))
    screen.blit(rld, (51, 675))
    screen.blit(escp, (51, 700))

def win_screen(player, background, screen, left_corner_left):
    fontB = pygame.font.Font(None, 150)
    fontS = pygame.font.Font(None, 40)
    winner = fontB.render("Player %d wins !" %player, 1, (255,255,255))
    restart = fontS.render("Press R to start again", 1, (255, 255, 255))
    leave = fontS.render("& press Enter or Escape to leave", 1, (255, 255, 255))
    dominating = pygame.mixer.Sound("sound/dominating.wav")
    dominating.play()

    while True:
        pygame.time.Clock().tick(60)
        screen.fill((0, 0, 0))
        background.fill((0, 0, 0))
        screen.blit(background, left_corner_left)
        screen.blit(winner, (170, 200))
        screen.blit(restart, (300, 550))
        screen.blit(leave, (320, 580))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if ((event.key == K_RETURN) | (event.key == K_ESCAPE)):
                    pygame.quit()
                    sys.exit()
                elif event.key == K_r:
                    start_game(background, screen, left_corner_left, 0, 0, 2)
            elif event.type == QUIT:
                pygame.quit()
                sys.exit() 
    pygame.event.pump()
        
def start_game(background, screen, left_corner_left, score1, score2, i):
    BLACK = (0, 0, 0)
    RED = (200, 0, 0)
    GREY = (102, 102, 102)
    
    ball = Ball()
    player1 = Bat(15)
    player2 = Bat(980)
    direction = [1, -1]
    if (len(sys.argv) == 2):
        if ((sys.argv[1] == '--fernand') & (i == 1)):
            music = pygame.mixer.Sound("sound/playf.ogg")
            music.play()
    hitsound = pygame.mixer.Sound("sound/hit.wav")
    i = direction[random.randint(0,1)]
    j = direction[random.randint(0,1)]
    pygame.key.set_repeat(1, 1)
    ball.position = (ball.position[0] + ball.speed * i, ball.position[1] + ball.speed * j)
    while True:
        pygame.time.Clock().tick(60)
        screen.fill(BLACK)
        screen.blit(background, (121, 100))
        pygame.draw.rect(screen, RED, [0, 0, 1024, 0], 50)
        pygame.draw.rect(screen, GREY, [512, 0, 0, 768], 7)
        header_bar(screen, score1, score2)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            player2.movedown()
        if pygame.key.get_pressed()[pygame.K_UP]:
            player2.moveup()
        if pygame.key.get_pressed()[pygame.K_z]:
            player1.moveup()
        if pygame.key.get_pressed()[pygame.K_s]:
            player1.movedown()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_r:
                    start_game(background, screen, left_corner_left, 0, 0, 2)
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        if ((ball.position[1] >= 745) | (ball.position[1] <= 34)):
            j = -j
        elif (((ball.position[1] >= player1.position[1]) & (ball.position[1] <= player1.position[1] + 150) & (ball.position[0] >= player1.position[0] - 20) & (ball.position[0] <= player1.position[0] + 20)) | ((ball.position[1] >= player2.position[1]) & (ball.position[1] <= player2.position[1] + 150) & (ball.position[0] >= player2.position[0] - 25) & (ball.position[0] <= player2.position[0] + 25))):
            i = -i
            hitsound.play()
        if (ball.position[0] > 1000):
            score1 += 1
            start_game(background, screen, left_corner_left, score1, score2, 2)
        elif (ball.position[0] < 0):
            score2 += 1
            start_game(background, screen, left_corner_left, score1, score2, 2)
        if (score1 == 10):
            win_screen(1, background, screen, left_corner_left)
        elif (score2 == 10):
            win_screen(1, background, screen, left_corner_left)
        ball.position = (ball.position[0] + ball.speed * i, ball.position[1] + ball.speed * j)
        screen.blit(ball.image, ball.position)
        screen.blit(player1.image, player1.position)
        screen.blit(player2.image, player2.position)
        pygame.display.update()
    pygame.event.pump()

def options(background, screen, left_corner_left):
    BLACK = (0, 0, 0)

    screen.fill(BLACK)
    screen.blit(background, left_corner_left)
    options_display(screen)
    pygame.display.flip()
    while True:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    main()
                if event.key == K_F1:
                    global difficulty
                    difficulty = 1
                    options_display(screen)
                if event.key == K_F2:
                    global difficulty
                    difficulty = 2
                    options_display(screen)
                if event.key == K_F3:
                    global difficulty
                    difficulty = 3
                    options_display(screen)
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    pygame.event.pump()

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    background = pygame.Surface(screen.get_size())
    if (len(sys.argv) == 2):
        if (sys.argv[1] == '--fernand'):
            background = pygame.image.load("images/backgroundf.bmp")
        else:
            background = pygame.image.load("images/background.bmp")
    else:
        background = pygame.image.load("images/background.bmp")
    left_corner_left = (0, 0)
    BLACK = (0, 0, 0)
    GREY = (127, 127, 127)
    RED = (188, 14, 14)
    score1 = 0
    score2 = 0
    pygame.mixer.music.load("sound/menu.ogg")
    pygame.mixer.music.play()

    pygame.display.set_caption('Pong without ping')
    screen.blit(background, left_corner_left)
    menu(screen)
    pygame.display.flip()
    while True:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    pygame.mixer.music.stop()
                    start_game(background, screen, left_corner_left, score1, score2, 1)
                if event.key == K_o:
                    options(background, screen, left_corner_left)
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    pygame.event.pump()

if (__name__ == "__main__"):
    main()

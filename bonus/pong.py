#!/usr/bin/env python
import pygame, sys, math
from pygame.locals import *
try:
    import pygame
    import sys
    from pygame.locals import *
except ImportError, err:
    print "Error during import\n", err
    sys.exit(1)

class Ball(pygame.sprite.Sprite):
    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ball.bmp').convert()
        self.rect = pygame.image.load('ball.bmp').convert()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
    def update(self):
        pos = self.pos(self.rect, self.vector)
        self.rect = pos
    def pos(self, rect, vector):
        (angle, z) = vector
        (dx, dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx, dy)

class Bat(pygame.sprite.Sprite):
    def __init__(self, side):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('player.bmp').convert()
        self.rect = pygame.image.load('player.bmp').convert()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.side = side
        self.speed = 20
        self.state = "default"
        self.position()
    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pygame.event.pump()
    def position(self):
        self.state = "default"
        self.movepos = [0,0]
        if self.side == "left":
            self.rect.midleft = self.area.midleft
        if self.side == "right":
            self.rect.midleft = self.area.midright
    def moveup(self):
        self.state = "moveup"
        self.movepos = self.movepos[1] + self.speed
    def movedown(self):
        self.state = "movedown"
        self.position = self.position[1] - self.speed
        
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
    ex = fontT.render("& ESCAPE to quit", 1, (255, 255, 255))
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

def header_bar(screen):
    font = pygame.font.Font(None, 36)

    p1_text = font.render("Player 1", 1, (255, 255, 255))
    p1_score_text = font.render("0", 1, (255, 255, 255))
    p2_text = font.render("Player 2", 1, (255, 255, 255))
    p2_score_text = font.render("0", 1, (255, 255, 255))

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

    screen.blit(OPT, (425, 50))
    screen.blit(P1, (51, 150))
    screen.blit(P2, (51, 260))
    screen.blit(start, (51, 650))
    screen.blit(rld, (51, 675))
    screen.blit(escp, (51, 700))

def start_game(background, screen, left_corner_left):
    BLACK = (0, 0, 0)
    GREY = (127, 127, 127)
    RED = (188, 14, 14)

    background.fill(BLACK)
    screen.blit(background, left_corner_left)
    pygame.draw.rect(screen, RED, [0, 0, 1024, 0], 50) #Top 25px   
    pygame.draw.rect(screen, GREY, [512, 0, 0, 768], 7) #Middle
    header_bar(screen)
    ball = Ball((1,0))
    #player1 = Bat("left")
    #player2 = Bat("right")
    pygame.display.flip()
    while True:
        pygame.time.Clock().tick(60)
        #Ball.update(Ball((1,0)))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_DOWN:
                    player1.movedown()
                elif event.key == K_UP:
                    player1.moveup()
                elif event.key == K_z:
                    player2.moveup()
                elif event.key == K_s:
                    player2.movedown()
                elif event.key == K_r:
                    start_game(background, screen, left_corner_left)
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    pygame.event.pump()

def options(background, screen, left_corner_left):
    BLACK = (0, 0, 0)
    GREY = (127, 127, 127)
    RED = (188, 14, 14)

    background.fill(BLACK)
    screen.blit(background, left_corner_left)
    options_display(screen)
    pygame.display.flip()
    while True:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    main()
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
    background = background.convert()
    left_corner_left = (0, 0)
    BLACK = (0, 0, 0)
    GREY = (127, 127, 127)
    RED = (188, 14, 14)

    pygame.display.set_caption('Pong without ping')
    background.fill(BLACK)
    screen.blit(background, left_corner_left)
    menu(screen)
    pygame.display.flip()
    while True:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    start_game(background, screen, left_corner_left)
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
main()

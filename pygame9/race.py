import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
#цветаааа
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW= (255, 255, 0)
#параметрыыы экрана скорости и тд
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5  # скорость врага
SCORE = 0
COINS_COLLECTED = 0
N = 5  # каждые N монет скорость врага растёт

#муызкальное сопроваждениеее
pygame.mixer.music.load("tokyo.mp3")
pygame.mixer.music.play(-1) 
pygame.mixer.music.set_volume(0.5)
crash_sound = pygame.mixer.Sound("crash.mp3")

#все сввязанное с текстом и их параметры
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
coin_font = pygame.font.SysFont("Verdana", 16)   # цифра на монетке
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("animatedstreet.png")

DISPLAYSURF = pygame.display.set_mode((400,600))
pygame.display.set_caption("Game")
 
#все связанное с машинками врагами
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
 
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#монеточки которые весят по разному
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.randint(1, 5)  #монетка имеет вес 1–5
        # рисуем монетку
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (15, 15), 15)
        #ишем число веса на монетке
        text = coin_font.render(str(self.weight), True, BLACK)
        self.image.blit(text, (10, 7))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
#основное мы и наша машинка
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        #его движение
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)
            
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# тааймеры
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

COIN_SPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(COIN_SPAWN, 2000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.3       # плавный рост
        if event.type == COIN_SPAWN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))

    #очкиии
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    #монетки
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(coins_text, (300,10))
    # обновка экрана
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    collected = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected:
        COINS_COLLECTED += coin.weight    # прибавляем вес монетки
        all_sprites.remove(coin)

        #ускоряем врага после N монет
        if COINS_COLLECTED % N == 0:
            SPEED += 1

    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        final_score = font_small.render(f"Score: {SCORE}", True, WHITE)
        final_coins = font_small.render(f"Coins: {COINS_COLLECTED}", True, YELLOW)
        DISPLAYSURF.blit(final_score, (150, 350))
        DISPLAYSURF.blit(final_coins, (150, 380))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)

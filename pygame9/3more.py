import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

# COLORS
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW= (255, 255, 0)

# GAME VARIABLES
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0
LIVES = 3    # ← NEW: 3 LIVES

# MUSIC
pygame.mixer.music.load("tokyo.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

crash_sound = pygame.mixer.Sound("crash.mp3")

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("animatedstreet.png")
DISPLAYSURF = pygame.display.set_mode((400,600))
pygame.display.set_caption("Game")
 
# ---------------- CLASSES ---------------- #

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
 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            
            
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
             self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
             self.rect.move_ip(0,5)
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
# OBJECTS
C1 = Coin()
E1 = Enemy()
P1 = Player()
 
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)
 
# EVENTS
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

COIN_SPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(COIN_SPAWN, 2000)

# ---------------- GAME LOOP ---------------- #
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5

        if event.type == COIN_SPAWN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    
    # SCORE
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    
    # SHOW COINS
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(coins_text, (290,10))

    # SHOW LIVES
    lives_text = font_small.render(f"Lives: {LIVES}", True, RED)
    DISPLAYSURF.blit(lives_text, (150, 10))
 
    # MOVE OBJECTS
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    # COLLISION WITH COINS
    coins_collected = pygame.sprite.spritecollide(P1, coins, True)
    for coin in coins_collected:
        COINS_COLLECTED += 1
        all_sprites.remove(coin)
 
    # COLLISION WITH ENEMY → LOSE LIFE
    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        LIVES -= 1  # ↓↓↓ LOSE 1 LIFE

        # Reset enemy position after crash
        for enemy in enemies:
            enemy.rect.top = 0
            enemy.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

        time.sleep(0.4)

        # If out of lives → GAME OVER
        if LIVES <= 0:
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

import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init() #инициализация пайгейма
FPS = 60
FramePerSec = pygame.time.Clock()
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) #цвета
YELLOW= (255, 255, 0)

 #основные параметры
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

#крутая музыка плюс вайб
pygame.mixer.music.load("tokyo.mp3")  
pygame.mixer.music.play(-1)  # бесконечность не предел
pygame.mixer.music.set_volume(0.5)  #громкость

# звук аварии
crash_sound = pygame.mixer.Sound("crash.mp3")  
 
#параметры текста
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("animatedstreet.png")
 
#окошка
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite): #параметры машинки которая всегда мешает
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self): 
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
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
            
            
class Player(pygame.sprite.Sprite): #параметры основной нашей машинки
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self): #о том как двигается машинка
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
                   
#укарачиваем имя
C1 = Coin()
E1=Enemy()
P1=Player()
 
#созданиее груп для обьектов
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 
#ивенты для обьектов их движение
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# появлен е монет
COIN_SPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(COIN_SPAWN, 2000)  # пояаляются каждые 2 секунды
 
#основной цикл
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
    
    # показываем счет в левом верхнем углу
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    
    # показываем монеты в правом верхнем углу
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(coins_text, (300,10))
 
    #движение и перерисовка обьектоов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    # проверка стллкновения с монетками
    coins_collected = pygame.sprite.spritecollide(P1, coins, True)
    for coin in coins_collected:
        COINS_COLLECTED += 1
        # удаление при столкновении
        all_sprites.remove(coin)
 
    #столкновение с противположными машиканми
    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()  # АВАРИЯЯЯ БАБАААХ
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED) #красный фрейм
        DISPLAYSURF.blit(game_over, (30,250)) #его размер
        final_score = font_small.render(f"Score: {SCORE}", True, WHITE)
        final_coins = font_small.render(f"Coins: {COINS_COLLECTED}", True, YELLOW)
        DISPLAYSURF.blit(final_score, (150, 350))
        DISPLAYSURF.blit(final_coins, (150, 380))
           
        pygame.display.update() #обновка
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2) # закрывается через 2 секунды
        pygame.quit()
        sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)
import pygame, sys
from pygame.locals import *
import random, time

WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Drop Game")
clock = pygame.time.Clock()
FPS = 60
speed=5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
BLUE = (50, 50, 255)
GREEN = (0,255,0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((120, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, 600))
        self.speed = 15
        
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Coin(pygame.sprite.Sprite):
    def __init__(self, size=60, color=GREEN):
        super().__init__(size, size)
        points = [
            (size // 2, 0),
            (0, size),
            (size, size)
        ]
        pygame.draw.polygon(self.image, color, points)
        self.tri = Coin(70, GREEN)
        self.tri.center = (random.randint(40, WIDTH-40), 0)
 
    def move(self):
        global SCORE
        self.tri.move_ip(0,speed)
        if self.tri.top > 600:
            SCORE += 1
            self.tri.top = 0
            self.tri.center = (random.randint(40, WIDTH - 40), 0)
    

player = Player()
all_sprites = pygame.sprite.Group(player)
coins = pygame.sprite.Group()

score = 0
running = True
 
P1 = Player()
C1=Coin()
coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, C1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)
    coins.update()

    # Check if any coin reached the floor
    for coin in list(coins):
        if coin.tri.bottom >= HEIGHT:
            score += 1
            coin.kill()  
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
 
    # проверка стллкновения с монетками
    coins_collected = pygame.sprite.spritecollide(P1, coins, True)
    for coin in coins_collected:
        COINS_COLLECTED += 1
        # удаление при столкновении
        all_sprites.remove(coin)
    screen.fill(WHITE)
    all_sprites.draw(screen)

    font = pygame.font.SysFont(None, 40)
    score_text = font.render(f"Coins Collected: {score}", True, BLACK)
    screen.blit(score_text, (20, 20))

    pygame.display.update()
    for entity in all_sprites:
        entity.kill()
    time.sleep(2)
    pygame.quit()
    sys.exit()        

pygame.quit()

import pygame
import random

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball vs Rectangles")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (219, 7, 1)
BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = 25

        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (self.radius, self.radius), self.radius)

        # rect for position
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

        self.speed = 10

    def update(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # Window boundaries
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, SCREEN_WIDTH)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, SCREEN_HEIGHT)

# ------------------- ENEMY SPRITE -------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 120
        self.height = 20
        self.speed = 7

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = -random.randint(100, 600)
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 50)

    def update(self):
        self.rect.x += self.speed

        # Respawn
        if self.rect.left > SCREEN_WIDTH:
            self.rect.x = -self.width
            self.rect.y = random.randint(50, SCREEN_HEIGHT - 50)

# --- SPRITE GROUPS ---
player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Make 3 enemies
for _ in range(3):
    e = Enemy()
    enemies.add(e)
    all_sprites.add(e)

# --- MAIN LOOP ---
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()

        # Update sprites
        player.update(keys)
        enemies.update()

        # Collision check (very simple now!)
        if pygame.sprite.spritecollide(player, enemies, False):
            game_over = True

        # DRAW
        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()

    else:
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 80)
        text = font.render("GAME OVER", True, RED)
        screen.blit(text, (SCREEN_WIDTH//2 - 200, SCREEN_HEIGHT//2 - 40))
        pygame.display.flip()

    clock.tick(FPS)

pygame.quit()

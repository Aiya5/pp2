import pygame
pygame.init()

WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Drop Game")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
BLUE = (50, 50, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((120, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(midtop=(WIDTH // 2, 20))
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
    def __init__(self, x, y):
        super().__init__()
        self.radius = 10
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, GOLD, (10, 10), self.radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        self.rect.y += self.speed

player = Player()
all_sprites = pygame.sprite.Group(player)
coins = pygame.sprite.Group()

score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Create a coin when pressing SPACE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                coin = Coin(player.rect.centerx, player.rect.bottom + 5)
                coins.add(coin)
                all_sprites.add(coin)

    keys = pygame.key.get_pressed()
    player.update(keys)
    coins.update()

    # Check if any coin reached the floor
    for coin in list(coins):
        if coin.rect.bottom >= HEIGHT:
            score += 1
            coin.kill()  # remove coin from game

    # DRAW
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Show score
    font = pygame.font.SysFont(None, 40)
    score_text = font.render(f"Coins Collected: {score}", True, BLACK)
    screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

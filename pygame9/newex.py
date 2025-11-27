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

'''class RectangleShape(ShapeBase):
    def __init__(self, width=80, height=40, color=BLUE):
        super().__init__(width, height)
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        
   class CircleShape(ShapeBase):
    def __init__(self, radius=30, color=YELLOW):
        super().__init__(radius * 2, radius * 2)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        
    class TriangleShape(ShapeBase):
    def __init__(self, size=60, color=GREEN):
        super().__init__(size, size)
        points = [
            (size // 2, 0),
            (0, size),
            (size, size)
        ]
        pygame.draw.polygon(self.image, color, points)
        
        class PentagonShape(ShapeBase):
    def __init__(self, size=60, color=PURPLE):
        super().__init__(size, size)

        cx, cy = size // 2, size // 2
        r = size // 2

        points = []
        for i in range(5):
            angle = -math.pi/2 + i * (2 * math.pi / 5)
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            points.append((x, y))

        pygame.draw.polygon(self.image, color, points)
        
        class StarShape(ShapeBase):
    def __init__(self, size=70, color=YELLOW):
        super().__init__(size, size)

        cx, cy = size // 2, size // 2
        r1 = size // 2
        r2 = size // 4
        points = []

        for i in range(10):
            angle = -math.pi/2 + i * (math.pi / 5)
            r = r1 if i % 2 == 0 else r2
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            points.append((x, y))

        pygame.draw.polygon(self.image, color, points)

# Create shapes
circle = CircleShape(40, YELLOW)
circle.rect.center = (200, 300)

rect = RectangleShape(100, 40, BLUE)
rect.rect.center = (350, 350)

triangle = TriangleShape(70, GREEN)
triangle.rect.center = (500, 250)

# Add to sprite group
all_sprites.add(circle, rect, triangle)



'''

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
            coin.kill()  

    screen.fill(WHITE)
    all_sprites.draw(screen)

    font = pygame.font.SysFont(None, 40)
    score_text = font.render(f"Coins Collected: {score}", True, BLACK)
    screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

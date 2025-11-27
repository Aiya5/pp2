import pygame
import random
import time

pygame.init()

# --- SETTINGS ---
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triangle Color Change + Collision")
clock = pygame.time.Clock()
FPS = 60

# COLORS
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
ORIGINAL_COLOR = (255, 100, 0)
CHANGED_COLOR = (0, 255, 0)

# PLAYER RECTANGLE
player_w, player_h = 120, 20
player_x = WIDTH // 2 - player_w // 2
player_y = HEIGHT - 60
player_speed = 7

# TRIANGLE DATA
triangle_color = ORIGINAL_COLOR
last_color_change = time.time()

def generate_triangle():
    x = random.randint(100, WIDTH - 100)
    y = random.randint(100, HEIGHT - 300)
    size = 60
    return [(x, y), (x - size, y + size), (x + size, y + size)]

triangle_points = generate_triangle()

def rect_triangle_collision(rect, triangle):
    for (tx, ty) in triangle:
        if rect.collidepoint(tx, ty):
            return True
    return False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    player_x = max(0, min(WIDTH - player_w, player_x))
    player_rect = pygame.Rect(player_x, player_y, player_w, player_h)

    if time.time() - last_color_change >= 2:
        triangle_color = CHANGED_COLOR
        last_color_change = time.time()

    if rect_triangle_collision(player_rect, triangle_points):
        triangle_color = ORIGINAL_COLOR
    screen.fill(WHITE)

    # Draw triangle
    pygame.draw.polygon(screen, triangle_color, triangle_points)
    pygame.draw.rect(screen, BLUE, player_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

import pygame
import sys
import time
import random

pygame.init()

w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Rect + Random Triangle")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 100)

player = pygame.Rect(100, 100, 90, 45)
speed = 6

tri_color = RED
original_color = RED

changed = False
changed_time = 0

# таймер появления треугольника
spawn_delay = 3   # секунды
last_spawn = time.time()

# начальный треугольник
tx = random.randint(200, 700)
ty = random.randint(200, 500)
tri = [(tx, ty), (tx + 50, ty + 100), (tx - 50, ty + 100)]

while True:

    # --- появление треугольника по таймеру ---
    if time.time() - last_spawn >= spawn_delay:
        tx = random.randint(200, 700)
        ty = random.randint(200, 500)
        tri = [(tx, ty), (tx + 50, ty + 100), (tx - 50, ty + 100)]
        last_spawn = time.time()   # сброс таймера

    # --- обработка событий ---
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += speed

    # границы окна
    if player.x < 0:
        player.x = 0
    if player.x + player.width > w:
        player.x = w - player.width
    if player.y < 0:
        player.y = 0
    if player.y + player.height > h:
        player.y = h - player.height

    # bounding box треугольника
    tx1 = min(tri[0][0], tri[1][0], tri[2][0])
    ty1 = min(tri[0][1], tri[1][1], tri[2][1])
    tx2 = max(tri[0][0], tri[1][0], tri[2][0])
    ty2 = max(tri[0][1], tri[1][1], tri[2][1])

    tri_rect = pygame.Rect(tx1, ty1, tx2 - tx1, ty2 - ty1)

    # если прямоугольник коснулся треугольника
    if player.colliderect(tri_rect):
        if not changed:
            tri_color = GREEN
            changed = True
            changed_time = time.time()

    # вернуть цвет через 2 секунды
    if changed:
        if time.time() - changed_time >= 2:
            tri_color = original_color
            changed = False

    # отрисовка
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.polygon(screen, tri_color, tri)

    pygame.display.update()
    clock.tick(60)
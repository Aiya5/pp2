import pygame 
import random
screenwigth= 700
screenheight = 700
pygame.init()
screen = pygame.display.set_mode((screenwigth, screenheight))
FPS = 60
white = (255, 255, 255)
black = (0,0,0)
red = (219, 7, 1)
clock = pygame.time.Clock()
movespeed = 20
circlerad = 25
enemy_width = 120
enemy_height = 20
enemy_speed = 7

enemies = []
for i in range(5):
    enemies.append(pygame.Rect(
        -random.randint(100, 600),             
        random.randint(50, screenheight - 50), 
        enemy_width,
        enemy_height
    ))

running = True
INITIAL_X_POS = 300
INITIAL_Y_POS = 300
x = INITIAL_X_POS
y = INITIAL_Y_POS
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont(None, 80)
        text = font.render("GAME OVER", True, red)
        screen.blit(text, (screenwigth//2 - 200, screenheight//2 - 40))
        pygame.display.flip()
        continue
            
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_UP]:
        y = max(circlerad,y - movespeed)
        
    if pressed[pygame.K_DOWN]:
        y = min(screenheight-circlerad, y + movespeed)
        
    if pressed[pygame.K_LEFT]:
        x = max(circlerad, x - movespeed)  
    
    if pressed[pygame.K_RIGHT]:
        x = min(screenwigth-circlerad, x + movespeed)
        
    if pressed[pygame.K_EQUALS]:
        circlerad+=1
    if pressed[pygame.K_MINUS]:
        circlerad-=1
    
    if y  == screenheight - circlerad:
           y = circlerad  
    elif y == circlerad:
           y = screenheight - circlerad
            
    for enemy in enemies:
        enemy.x += enemy_speed

        if enemy.x > screenwigth:
            enemy.x = -enemy_width
            enemy.y = random.randint(50, screenheight - 50)

        dx = abs(x - (enemy.x + enemy_width / 2))
        dy = abs(y - (enemy.y + enemy_height / 2))

        if dx < enemy_width / 2 + circlerad and dy < enemy_height / 2 + circlerad:
            game_over = True
            
    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), circlerad)
    for enemy in enemies:
        pygame.draw.rect(screen, black, enemy)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
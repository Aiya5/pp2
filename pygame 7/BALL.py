import pygame 
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
running = True
INITIAL_X_POS = 100
INITIAL_Y_POS = 100
x = INITIAL_X_POS
y = INITIAL_Y_POS

while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            
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
               
    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), circlerad)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
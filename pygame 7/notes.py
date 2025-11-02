'''import pygame - this is of course needed to access the PyGame framework.
pygame.init() - This kicks things off. It initializes all the modules required for PyGame.
pygame.display.set_mode((width, height)) - This will launch a window of the desired size. The return value is a Surface object which is the object you will perform graphical operations on. This will be discussed later.
pygame.event.get() - this empties the event queue. If you do not call this, the windows messages will start to pile up and your game will become unresponsive in the opinion of the operating system.
pygame.QUIT - This is the event type that is fired when you click on the close button in the corner of the window.
pygame.display.flip() - PyGame is double-buffered. This swaps the buffers. All you need to know is that this call is required in order for any updates that you make to the game screen to become visible.

# draw a rectangle
pygame.draw.rect(surface, color, pygame.Rect(10, 10, 100, 100), 10)
# draw a circle
pygame.draw.circle(surface, color, (300, 60), 50, 10)

pygame.draw.polygon(surface, color, point_list)

pygame.draw.line(surface, color, (startX, startY), (endX, endY), width)


    # if x == SCREEN_WIDTH - CIRCLE_RAD:
    #     x = CIRCLE_RAD  
    # elif x == CIRCLE_RAD:
    #     x = SCREEN_WIDTH - CIRCLE_RAD 
    
    # if y  == SCREEN_HEIGHT - CIRCLE_RAD:
    #     y = CIRCLE_RAD  
    # elif y == CIRCLE_RAD:
    #     y = SCREEN_HEIGHT - CIRCLE_RAD
'''


import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()
        clock.tick(60)
        
        
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
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
orange = (255, 165, 0)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

current_color = random_color()


colors = [red, green, blue, yellow, purple, orange]

current_color_index = 0
 
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #current_color_index = (current_color_index + 1) % len(colors)
                current_color = random_color()
            
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_UP]:
        y = max(circlerad,y - movespeed)
        
    if pressed[pygame.K_DOWN]:
        y = min(screenheight - circlerad, y + movespeed)
        
    if pressed[pygame.K_LEFT]:
        x = max(circlerad, x - movespeed)  
    
    if pressed[pygame.K_RIGHT]:
        x = min(screenwigth - circlerad, x + movespeed)
        
    if pressed[pygame.K_EQUALS]:
        circlerad+=1
    if pressed[pygame.K_MINUS]:
        circlerad-=1
    if pressed[pygame.K_1]:
        pygame.draw.circle(screen, blue, (x, y), circlerad)
        
    # Change color when hitting walls
    if (x == circlerad or x == screenwigth - circlerad or 
        y == circlerad or y == screenheight - circlerad):
        current_color = random_color()
    #screen.fill(white)
    pygame.draw.circle(screen, current_color, (x, y), circlerad)
    pygame.display.flip()
    clock.tick(FPS)
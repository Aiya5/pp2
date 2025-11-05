import os, pygame
from datetime import datetime
pygame.init() 
screenwidth = 900
screenheight = 700
CENTER = (screenwidth / 2, screenheight / 2)
screen = pygame.display.set_mode((screenwidth, screenheight))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

def blit_rotate(surface, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    surface.blit(rotated_image, new_rect)
    
FPS = 60
clock = pygame.time.Clock()
bg = pygame.image.load(os.path.join('pygame 7', 'images', 'base_micky.jpg'))
BG_WIDTH = 850
BG_HEIGHT = 880
BG_X_POS = (screenwidth / 2 - BG_WIDTH / 2)
BG_Y_POS = (screenheight / 2 - BG_HEIGHT / 2)

minute_arrow = pygame.image.load(os.path.join('pygame 7', 'images', 'minute.png'))
minutearrowwidth = 1100
minutearrowheight = 1100
minute_arrow = pygame.transform.scale(minute_arrow, (minutearrowwidth, minutearrowheight))

minute_arrow_rect = minute_arrow.get_rect()
minute_arrow_rect.midbottom = CENTER

second_arrow = pygame.image.load(os.path.join('pygame 7', 'images', 'second.png'))
secondarrowwidth = 70
secondarrowheight = 1000
second_arrow = pygame.transform.scale(second_arrow, (secondarrowwidth, secondarrowheight))

second_arrow_rect = second_arrow.get_rect()
second_arrow_rect.midbottom = CENTER

running = True
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    now = datetime.now()
    minute_angle = now.minute * -6 
    second_angle = now.second * -6  
    screen.fill(white)
    screen.blit(bg, (BG_X_POS, BG_Y_POS))
    blit_rotate(screen, minute_arrow, CENTER, minute_angle)
    blit_rotate(screen, second_arrow, CENTER, second_angle)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
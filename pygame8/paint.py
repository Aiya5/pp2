import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    radius = 15
    mode = 'blue'
    drawing_shape = 'rectangle'  
    start_pos = None
    is_drawing = False
    shapes = []
    brush_points = []
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        #ивенты нажатие клавиш
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                #выбор фигурки
                elif event.key == pygame.K_1:  #квадратик
                    drawing_shape = 'rectangle'
                elif event.key == pygame.K_2:  #кружочек
                    drawing_shape = 'circle'
                elif event.key == pygame.K_3:  #стиралка
                    drawing_shape = 'eraser'
                elif event.key == pygame.K_4:  #кисточка
                    drawing_shape = 'brush'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    radius = min(200, radius + 1)
                elif event.button == 3: 
                    radius = max(1, radius - 1)
                
                #рисует фигурками
                if drawing_shape in ['rectangle', 'circle']:
                    start_pos = event.pos
                    is_drawing = True
                #рисует кисточкой
                elif drawing_shape == 'brush':
                    brush_points = [event.pos]
            
            if event.type == pygame.MOUSEBUTTONUP:
                #цветааа
                if mode == 'blue':
                    color = (0, 0, 255)
                elif mode == 'red':
                    color = (255, 0, 0)
                elif mode == 'green':
                    color = (0, 255, 0)
                if is_drawing and start_pos and drawing_shape in ['rectangle', 'circle']:
                    end_pos = event.pos
                    if drawing_shape == 'rectangle':
                        rect = pygame.Rect(
                            min(start_pos[0], end_pos[0]),
                            min(start_pos[1], end_pos[1]),
                            abs(end_pos[0] - start_pos[0]),
                            abs(end_pos[1] - start_pos[1])
                        )
                        shapes.append(('rectangle', rect, radius//5+1, color))
                    elif drawing_shape == 'circle':
                        center = start_pos
                        radius_circle = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
                        shapes.append(('circle', center, radius_circle, radius//5+1, color))
                elif drawing_shape == 'brush' and len(brush_points) > 1:
                    shapes.append(('brush', brush_points.copy(), radius, color))
                is_drawing = False
                start_pos = None
                brush_points = []
                
            if event.type == pygame.MOUSEMOTION:
                #рисовать в движенкиии
                if drawing_shape == 'brush' and pygame.mouse.get_pressed()[0]:
                    position = event.pos
                    brush_points.append(position)
                    #лимит чтобы избежать ошибкии
                    if len(brush_points) > 1000:
                        brush_points.pop(0)
                #стерка во время движенияя
                elif drawing_shape == 'eraser' and pygame.mouse.get_pressed()[0]:
                    position = event.pos
                    shapes.append(('eraser', position, radius))
        screen.fill((0, 0, 0))
        if mode == 'blue':
            current_color = (0, 0, 255)
        elif mode == 'red':
            current_color = (255, 0, 0)
        elif mode == 'green':
            current_color = (0, 255, 0)
        for shape in shapes:
            if shape[0] == 'rectangle':
                pygame.draw.rect(screen, shape[3], shape[1], width=shape[2])
            elif shape[0] == 'circle':
                pygame.draw.circle(screen, shape[4], shape[1], shape[2])
            elif shape[0] == 'brush':
                if len(shape[1]) > 1:
                    for i in range(len(shape[1]) - 1):
                        pygame.draw.line(screen, shape[3], shape[1][i], shape[1][i + 1], shape[2])
            elif shape[0] == 'eraser':
                pygame.draw.circle(screen, (0, 0, 0), shape[1], shape[2])
        
        if drawing_shape == 'brush' and len(brush_points) > 1:
            for i in range(len(brush_points) - 1):
                pygame.draw.line(screen, current_color, brush_points[i], brush_points[i + 1], radius)
        if is_drawing and start_pos and drawing_shape in ['rectangle', 'circle']:
            current_pos = pygame.mouse.get_pos()
            
            if drawing_shape == 'rectangle':
                rect = pygame.Rect(
                    min(start_pos[0], current_pos[0]),
                    min(start_pos[1], current_pos[1]),
                    abs(current_pos[0] - start_pos[0]),
                    abs(current_pos[1] - start_pos[1])
                )
                pygame.draw.rect(screen, current_color, rect, width=radius//5+1)
            elif drawing_shape == 'circle':
                center = start_pos
                radius_circle = int(((current_pos[0] - start_pos[0])**2 + (current_pos[1] - start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, current_color, center, radius_circle, width=radius//5+1)
        pygame.display.flip()
        clock.tick(60)
main()
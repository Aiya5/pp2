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
        
        # события нажатия клавиш
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
                #выбиарем цвеет
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                # выбираем формыы для рисования
                elif event.key == pygame.K_1:  # квадрат/прямоугольник
                    drawing_shape = 'rectangle'
                elif event.key == pygame.K_2:  # круг
                    drawing_shape = 'circle'
                elif event.key == pygame.K_3:  # стиралка
                    drawing_shape = 'eraser'
                elif event.key == pygame.K_4:  # кисть
                    drawing_shape = 'brush'
                elif event.key == pygame.K_5:  # квадрат
                    drawing_shape = 'square'
                elif event.key == pygame.K_6:  # прямой треугольник
                    drawing_shape = 'right_triangle'
                elif event.key == pygame.K_7:  # равносторонний треугольник
                    drawing_shape = 'equilateral_triangle'
                elif event.key == pygame.K_8:  # ромб
                    drawing_shape = 'rhombus'
            
            # нажатие мышки
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    radius = min(200, radius + 1)
                elif event.button == 3: 
                    radius = max(1, radius - 1)
                if drawing_shape in ['rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                    start_pos = event.pos
                    is_drawing = True
                elif drawing_shape == 'brush':
                    brush_points = [event.pos]
                    
            if event.type == pygame.MOUSEBUTTONUP:
                if mode == 'blue':
                    color = (0, 0, 255)
                elif mode == 'red':
                    color = (255, 0, 0)
                elif mode == 'green':
                    color = (0, 255, 0)
                if is_drawing and start_pos:
                    end_pos = event.pos
                    # прямоугольник
                    if drawing_shape == 'rectangle':
                        rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                           abs(end_pos[0]-start_pos[0]), abs(end_pos[1]-start_pos[1]))
                        shapes.append(('rectangle', rect, radius//5+1, color))
                    # квадрат
                    elif drawing_shape == 'square':
                        side = max(abs(end_pos[0]-start_pos[0]), abs(end_pos[1]-start_pos[1]))
                        rect = pygame.Rect(start_pos[0], start_pos[1], side, side)
                        shapes.append(('square', rect, radius//5+1, color))
                    # круг
                    elif drawing_shape == 'circle':
                        center = start_pos
                        radius_circle = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                        shapes.append(('circle', center, radius_circle, radius//5+1, color))
                    # прямой треугольник
                    elif drawing_shape == 'right_triangle':
                        points = [start_pos, (end_pos[0], start_pos[1]), end_pos]
                        shapes.append(('polygon', points, radius//5+1, color))
                    # равносторонний треугольник
                    elif drawing_shape == 'equilateral_triangle':
                        x0, y0 = start_pos
                        side = end_pos[0] - x0
                        height = int(side * (3**0.5)/2)
                        points = [start_pos, (x0 + side, y0), (x0 + side//2, y0 - height)]
                        shapes.append(('polygon', points, radius//5+1, color))
                    # ромб
                    elif drawing_shape == 'rhombus':
                        x0, y0 = start_pos
                        dx = (end_pos[0]-x0)//2
                        dy = (end_pos[1]-y0)//2
                        points = [(x0, y0-dy), (x0+dx, y0), (x0, y0+dy), (x0-dx, y0)]
                        shapes.append(('polygon', points, radius//5+1, color))
                elif drawing_shape == 'brush' and len(brush_points) > 1:
                    shapes.append(('brush', brush_points.copy(), radius, color))
                is_drawing = False
                start_pos = None
                brush_points = []
                
            if event.type == pygame.MOUSEMOTION:
                if drawing_shape == 'brush' and pygame.mouse.get_pressed()[0]:
                    position = event.pos
                    brush_points.append(position)
                    if len(brush_points) > 1000:
                        brush_points.pop(0)
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
            elif shape[0] == 'square':
                pygame.draw.rect(screen, shape[3], shape[1], width=shape[2])
            elif shape[0] == 'circle':
                pygame.draw.circle(screen, shape[4], shape[1], shape[2], width=shape[3])
            elif shape[0] == 'brush':
                if len(shape[1]) > 1:
                    for i in range(len(shape[1])-1):
                        pygame.draw.line(screen, shape[3], shape[1][i], shape[1][i+1], shape[2])
            elif shape[0] == 'eraser':
                pygame.draw.circle(screen, (0,0,0), shape[1], shape[2])
            elif shape[0] == 'polygon':
                pygame.draw.polygon(screen, shape[3], shape[1], width=shape[2])
        
        #кисточка
        if drawing_shape == 'brush' and len(brush_points) > 1:
            for i in range(len(brush_points)-1):
                pygame.draw.line(screen, current_color, brush_points[i], brush_points[i+1], radius)
        if is_drawing and start_pos:
            current_pos = pygame.mouse.get_pos()
            if drawing_shape == 'rectangle':
                rect = pygame.Rect(min(start_pos[0], current_pos[0]), min(start_pos[1], current_pos[1]),
                                   abs(current_pos[0]-start_pos[0]), abs(current_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, current_color, rect, width=radius//5+1)
            elif drawing_shape == 'square':
                side = max(abs(current_pos[0]-start_pos[0]), abs(current_pos[1]-start_pos[1]))
                rect = pygame.Rect(start_pos[0], start_pos[1], side, side)
                pygame.draw.rect(screen, current_color, rect, width=radius//5+1)
            elif drawing_shape == 'circle':
                radius_circle = int(((current_pos[0]-start_pos[0])**2 + (current_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius_circle, width=radius//5+1)
            elif drawing_shape == 'right_triangle':
                points = [start_pos, (current_pos[0], start_pos[1]), current_pos]
                pygame.draw.polygon(screen, current_color, points, width=radius//5+1)
            elif drawing_shape == 'equilateral_triangle':
                x0, y0 = start_pos
                side = current_pos[0]-x0
                height = int(side*(3**0.5)/2)
                points = [start_pos, (x0+side, y0), (x0+side//2, y0-height)]
                pygame.draw.polygon(screen, current_color, points, width=radius//5+1)
            elif drawing_shape == 'rhombus':
                x0, y0 = start_pos
                dx = (current_pos[0]-x0)//2
                dy = (current_pos[1]-y0)//2
                points = [(x0, y0-dy), (x0+dx, y0), (x0, y0+dy), (x0-dx, y0)]
                pygame.draw.polygon(screen, current_color, points, width=radius//5+1)
        
        pygame.display.flip()
        clock.tick(60)

main()

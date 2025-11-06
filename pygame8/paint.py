import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Типа Пэйнт")  # название окошка
    clock = pygame.time.Clock()
    
    # Тут все цвета какие есть
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    CYAN = (0, 255, 255)
    
    # Переменные для рисования
    radius = 15  # размер кисточки
    current_color = BLUE  # начальный цвет
    points = []
    drawing = False  # рисуем или нет
    last_pos = None  # где была мышь в прошлый раз
    current_tool = 'pen'  # чем рисуем: кисть, квадрат, круг, ластик
    
    # Палитра цветов - квадратики сверху
    colors = [BLACK, RED, GREEN, BLUE, YELLOW, PURPLE, CYAN, WHITE]
    color_buttons = []
    for i, color in enumerate(colors):
        color_buttons.append(pygame.Rect(10 + i*40, 10, 30, 30))
    
    # Кнопки инструментов
    tool_buttons = [
        {'rect': pygame.Rect(350, 10, 80, 30), 'tool': 'pen', 'text': 'Кисть'},
        {'rect': pygame.Rect(440, 10, 80, 30), 'tool': 'rectangle', 'text': 'Квадрат'},
        {'rect': pygame.Rect(530, 10, 80, 30), 'tool': 'circle', 'text': 'Круг'},
        {'rect': pygame.Rect(620, 10, 80, 30), 'tool': 'eraser', 'text': 'Ластик'}
    ]
    
    # Холсты для рисования
    canvas = pygame.Surface((800, 600))  # основной холст
    canvas.fill(WHITE)  # белый фон
    temp_surface = pygame.Surface((800, 600), pygame.SRCALPHA)  # временный для фигур
    
    # Для рисования фигур
    start_pos = None  # откуда начали рисовать
    current_shape = None  # что сейчас рисуем
    
    def draw_interface():
        #Рисуем панельку сверху с инструментам
        # Рисуем цветные квадратики
        for i, button in enumerate(color_buttons):
            pygame.draw.rect(screen, colors[i], button)
            pygame.draw.rect(screen, BLACK, button, 1)  # черная рамка
        
        # Рисуем кнопки инструментов
        for button in tool_buttons:
            # Подсвечиваем выбранный инструмент
            if current_tool == button['tool']:
                color = (200, 200, 200)  # светлый если выбран
            else:
                color = (100, 100, 100)  # темный если не выбран
            
            pygame.draw.rect(screen, color, button['rect'])
            pygame.draw.rect(screen, BLACK, button['rect'], 1)
            
            # Текст на кнопках
            font = pygame.font.Font(None, 24)
            text = font.render(button['text'], True, BLACK)
            text_rect = text.get_rect(center=button['rect'].center)
            screen.blit(text, text_rect)
        
        # Показываем текущий цвет
        pygame.draw.rect(screen, current_color, (710, 10, 30, 30))
        pygame.draw.rect(screen, BLACK, (710, 10, 30, 30), 1)
    
    def draw_pen(pos):
        #Рисуем обычной кистью"""
        if last_pos:
            pygame.draw.line(canvas, current_color, last_pos, pos, radius)
        return pos
    
    def draw_rectangle(start, end):
        #Рисуем прямоугольник или квадрат
        temp_surface.fill((0, 0, 0, 0))  # очищаем временную поверхность
        # Создаем прямоугольник от начальной до конечной точки
        rect = pygame.Rect(
            min(start[0], end[0]),
            min(start[1], end[1]),
            abs(end[0] - start[0]),
            abs(end[1] - start[1])
        )
        pygame.draw.rect(temp_surface, current_color, rect, max(1, radius//2))
        return rect
    
    def draw_circle(start, end):
        #Рисуем круг
        temp_surface.fill((0, 0, 0, 0))  # очищаем временную поверхность
        # Находим центр между двумя точками
        center_x = (start[0] + end[0]) // 2
        center_y = (start[1] + end[1]) // 2
        # Считаем радиус по расстоянию между точками
        radius_shape = int(((end[0] - start[0])**2 + (end[1] - start[1])**2)**0.5) // 2
        pygame.draw.circle(temp_surface, current_color, (center_x, center_y), radius_shape, max(1, radius//2))
        return (center_x, center_y, radius_shape)
    
    def draw_eraser(pos):
        #Стираем ластиком
        if last_pos:
            pygame.draw.line(canvas, WHITE, last_pos, pos, radius * 2)
        return pos
    
    # Главный цикл игры
    while True:
        # Проверяем нажатые клавиши
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        # Обрабатываем события
        for event in pygame.event.get():
            # Выход из игры
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Быстрые клавиши для цветов
                if event.key == pygame.K_r:
                    current_color = RED
                elif event.key == pygame.K_g:
                    current_color = GREEN
                elif event.key == pygame.K_b:
                    current_color = BLUE
                elif event.key == pygame.K_y:
                    current_color = YELLOW
                elif event.key == pygame.K_p:
                    current_color = PURPLE
                elif event.key == pygame.K_c:
                    current_color = CYAN
                elif event.key == pygame.K_k:
                    current_color = BLACK
                elif event.key == pygame.K_w:
                    current_color = WHITE
            
            # Клики мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()  # где кликнули
                
                # Проверяем клик по цветам
                for i, button in enumerate(color_buttons):
                    if button.collidepoint(pos):
                        current_color = colors[i]
                        break
                
                # Проверяем клик по инструментам
                for button in tool_buttons:
                    if button['rect'].collidepoint(pos):
                        current_tool = button['tool']
                        break
                
                # Начинаем рисовать если кликнули ниже панели
                if pos[1] > 50:
                    if event.button == 1:  # Левая кнопка - рисуем
                        drawing = True
                        last_pos = pos
                        start_pos = pos
                    elif event.button == 3:  # Правая кнопка - уменьшаем кисть
                        radius = max(1, radius - 1)
                    elif event.button == 4:  # Колесико вверх - увеличиваем кисть
                        radius = min(50, radius + 1)
                    elif event.button == 5:  # Колесико вниз - уменьшаем кисть
                        radius = max(1, radius - 1)
            
            # Отпустили кнопку мыши
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False
                    
                    # Фиксируем фигуры на основном холсте
                    if current_tool in ["rectangle", "circle"] and current_shape:
                        canvas.blit(temp_surface, (0, 0))
                        temp_surface.fill((0, 0, 0, 0))  # очищаем временную поверхность
                    
                    # Сбрасываем переменные
                    last_pos = None
                    start_pos = None
                    current_shape = None
            
            # Движение мыши
            if event.type == pygame.MOUSEMOTION:
                if drawing:  # если рисуем
                    pos = pygame.mouse.get_pos()
                    
                    if current_tool == "pen":
                        last_pos = draw_pen(pos)
                    
                    elif current_tool == "eraser":
                        last_pos = draw_eraser(pos)
                    
                    elif current_tool == "rectangle" and start_pos:
                        current_shape = draw_rectangle(start_pos, pos)
                    
                    elif current_tool == "circle" and start_pos:
                        current_shape = draw_circle(start_pos, pos)
        
        # Рисуем все на экран
        screen.blit(canvas, (0, 0))  # основной холст
        screen.blit(temp_surface, (0, 0))  # временные фигуры
        draw_interface()  # панель инструментов
        
        pygame.display.flip()  # обновляем экран
        clock.tick(60)  # 60 кадров в секунду

# Старая функция для совместимости (можно игнорить)
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
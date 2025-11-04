import pygame

pygame.init()

# размеры окна
width = 800
height = 600

# цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (255, 0, 255)

# создаем окно
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Мой рисовалка")

# переменные для рисования
risuem = False
last_pos = None
current_color = black
razmer_kisti = 5
instrument = "kist"  # kist, kvadrat, krug, lastik

# цвета для выбора
tsveta = [
    {"rect": pygame.Rect(10, 10, 30, 30), "color": black},
    {"rect": pygame.Rect(50, 10, 30, 30), "color": red},
    {"rect": pygame.Rect(90, 10, 30, 30), "color": green},
    {"rect": pygame.Rect(130, 10, 30, 30), "color": blue},
    {"rect": pygame.Rect(170, 10, 30, 30), "color": yellow},
    {"rect": pygame.Rect(210, 10, 30, 30), "color": purple},
    {"rect": pygame.Rect(250, 10, 30, 30), "color": white}
]

# кнопки инструментов
knopki_instrumentov = [
    {"rect": pygame.Rect(300, 10, 80, 30), "tool": "kist", "text": "Кисть"},
    {"rect": pygame.Rect(390, 10, 80, 30), "tool": "kvadrat", "text": "Квадрат"},
    {"rect": pygame.Rect(480, 10, 80, 30), "tool": "krug", "text": "Круг"},
    {"rect": pygame.Rect(570, 10, 80, 30), "tool": "lastik", "text": "Ластик"},
    {"rect": pygame.Rect(660, 10, 80, 30), "tool": "clear", "text": "Очистить"}
]

# холст для рисования
holst = pygame.Surface((width, height))
holst.fill(white)

# временная поверхность для фигур
temp_poverhnost = pygame.Surface((width, height), pygame.SRCALPHA)

# переменные для рисования фигур
start_pos = None
current_figura = None

def risovat_interface():
    """Рисуем панель инструментов"""
    # рисуем палитру цветов
    for tsvet in tsveta:
        pygame.draw.rect(screen, tsvet["color"], tsvet["rect"])
        pygame.draw.rect(screen, black, tsvet["rect"], 1)
    
    # рисуем кнопки инструментов
    for knopka in knopki_instrumentov:
        tsvet_knopki = (200, 200, 200) if instrument == knopka["tool"] else (100, 100, 100)
        pygame.draw.rect(screen, tsvet_knopki, knopka["rect"])
        pygame.draw.rect(screen, black, knopka["rect"], 1)
        
        font = pygame.font.Font(None, 24)
        text = font.render(knopka["text"], True, black)
        text_rect = text.get_rect(center=knopka["rect"].center)
        screen.blit(text, text_rect)
    
    # показываем текущий цвет
    pygame.draw.rect(screen, current_color, (750, 10, 30, 30))
    pygame.draw.rect(screen, black, (750, 10, 30, 30), 1)

def risovat_kistyu(pos):
    """Рисуем кистью"""
    if last_pos:
        pygame.draw.line(holst, current_color, last_pos, pos, razmer_kisti)
    return pos

def risovat_kvadrat(start, end):
    """Рисуем квадрат/прямоугольник"""
    temp_poverhnost.fill((0, 0, 0, 0))  # очищаем временную поверхность
    rect = pygame.Rect(
        min(start[0], end[0]),
        min(start[1], end[1]),
        abs(end[0] - start[0]),
        abs(end[1] - start[1])
    )
    pygame.draw.rect(temp_poverhnost, current_color, rect, razmer_kisti)
    return rect

def risovat_krug(start, end):
    """Рисуем круг"""
    temp_poverhnost.fill((0, 0, 0, 0))  # очищаем временную поверхность
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2
    radius = int(((end[0] - start[0])**2 + (end[1] - start[1])**2)**0.5) // 2
    pygame.draw.circle(temp_poverhnost, current_color, (center_x, center_y), radius, razmer_kisti)
    return (center_x, center_y, radius)

def risovat_lastikom(pos):
    """Стираем ластиком"""
    if last_pos:
        pygame.draw.line(holst, white, last_pos, pos, razmer_kisti * 2)
    return pos

def ochistit_holst():
    """Очищаем весь холст"""
    holst.fill(white)
    temp_poverhnost.fill((0, 0, 0, 0))

# главный цикл
rabotaet = True
while rabotaet:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rabotaet = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # левая кнопка мыши
                pos = pygame.mouse.get_pos()
                
                # проверяем цвета
                for tsvet in tsveta:
                    if tsvet["rect"].collidepoint(pos):
                        current_color = tsvet["color"]
                        break
                
                # проверяем инструменты
                for knopka in knopki_instrumentov:
                    if knopka["rect"].collidepoint(pos):
                        if knopka["tool"] == "clear":
                            ochistit_holst()
                        else:
                            instrument = knopka["tool"]
                        break
                
                # начинаем рисовать
                if pos[1] > 50:  # ниже панели инструментов
                    risuem = True
                    last_pos = pos
                    start_pos = pos
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and risuem:
                risuem = False
                
                # завершаем рисование фигур
                if instrument in ["kvadrat", "krug"] and current_figura:
                    # копируем с временной поверхности на холст
                    holst.blit(temp_poverhnost, (0, 0))
                    temp_poverhnost.fill((0, 0, 0, 0))  # очищаем временную поверхность
                
                last_pos = None
                start_pos = None
                current_figura = None
        
        elif event.type == pygame.MOUSEMOTION:
            if risuem:
                pos = pygame.mouse.get_pos()
                
                if instrument == "kist":
                    last_pos = risovat_kistyu(pos)
                
                elif instrument == "lastik":
                    last_pos = risovat_lastikom(pos)
                
                elif instrument == "kvadrat" and start_pos:
                    current_figura = risovat_kvadrat(start_pos, pos)
                
                elif instrument == "krug" and start_pos:
                    current_figura = risovat_krug(start_pos, pos)
    
    # рисуем все
    screen.blit(holst, (0, 0))  # рисуем холст
    screen.blit(temp_poverhnost, (0, 0))  # рисуем временные фигуры
    risovat_interface()  # рисуем интерфейс
    
    pygame.display.flip()

pygame.quit()
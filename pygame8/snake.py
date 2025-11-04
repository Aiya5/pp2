import pygame #пайгейм
import time #вреям
import random #для рандомного появление яблочек
x=720 #широта
y=480 #высота
snake_speed = 15 #СПИД

black = pygame.Color(0, 0, 0)  #ччерный
white = pygame.Color(255, 255, 255) #белый
red = pygame.Color(255, 0, 0) #красный
green = pygame.Color(0, 255, 0) #зеленый
blue = pygame.Color(0, 0, 255) #королевский синий
pink=pygame.Color(255,209,220) #розизий

pygame.init() #инициализация пайгейма
pygame.display.set_caption('Snake')  #название в уголке вкладки
game_window = pygame.display.set_mode((x, y)) #размеры параметры окошко
fps = pygame.time.Clock() #время обновления фпс

snake_position = [100, 50] #позиция северуса
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ] #размеры змейки
fruit_position = [random.randrange(1, (x // 10)) * 10,
                  random.randrange(1, (y // 10)) * 10] # а вот и рандомное позиция яблочки

fruit_spawn = True #появление существование яблочко тру
direction = 'RIGHT'
change_to = direction
score = 0 #поинты
level = 1 #начинается с перовго уровня
last_level_up = 0

# Show score and level
def show_info(color, font, size):
    info_font = pygame.font.SysFont(font, size)#размер и вид текста
    info_surface = info_font.render(f"Score: {score}  Level: {level}", True, color)#текст и поинты которые меняются
    info_rect = info_surface.get_rect()
    game_window.blit(info_surface, info_rect)#показать/вывести на экранчик
    # функции для показа очков и сколько заработано
    
def game_over() : #конец
    my_font = pygame.font.SysFont('times new roman', 50) #параметры текста
    game_over_surface = my_font.render( #создание обекта для поверхности а также текст и поинытыы
        'Your Score is : ' + str(score), True, green)
    game_over_rect = game_over_surface.get_rect() # прямоугольноквадратный обьект для текстаааа ну типа
    game_over_rect.midtop = (x / 2, y / 4) #появление текста в середине
    game_window.blit(game_over_surface, game_over_rect) #вывод на экран
    pygame.display.flip()#обновление экрана
    time.sleep(2)# окошко закроется через 2 секнуды
    pygame.quit()
    quit() #закрыть
    
while True : #основной цикл
    for event in pygame.event.get() : #а тут ключевые событие и клавиши их функции 
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                change_to = 'UP' #навверх
            if event.key == pygame.K_DOWN :
                change_to = 'DOWN' #вниз
            if event.key == pygame.K_LEFT :
                change_to = 'LEFT' #влево
            if event.key == pygame.K_RIGHT :
                change_to = 'RIGHT' #вправо
                
    #А это чтобы змейкаа не разделилась если одновременно начжать а то будет змейгорынычб
    if change_to == 'UP' and direction != 'DOWN' :
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP' :
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT' :
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT' :
        direction = 'RIGHT'
        
        #параметры на сколько пикселей и куда поворачивает и двиагется змейка
    if direction == 'UP' :
        snake_position[1] -= 10
    if direction == 'DOWN' :
        snake_position[1] += 10
    if direction == 'LEFT' :
        snake_position[0] -= 10
    if direction == 'RIGHT' :
        snake_position[0] += 10
        #удлинение телы змейки
        
    snake_body.insert(0, list(snake_position))
    #змейка съела яблочко или нет проверяерт
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1] :
        score += 10 #плюс вайб плюс поинты
        fruit_spawn = False #фрукт исчезает
    else :
        snake_body.pop() #удаляет хвост чтобы сохранить его длину елси змейка не съела яблочко
 
    if not fruit_spawn : #новая поизция для фрукта
        fruit_position = [random.randrange(1, (x // 10)) * 10,
                          random.randrange(1, (y // 10)) * 10]
    fruit_spawn = True #появление новгго фрукта
    
    if score // 30 > last_level_up: #условие больше 30 поинтов
        last_level_up = score // 30 
        level += 1 #плюс уровень
        snake_speed += 3 #увеличивает скорость змейки
        
    game_window.fill(black) #черный бэграунд
    for pos in snake_body :  #проходится по всей длине змейки
        pygame.draw.rect(game_window, pink,pygame.Rect(pos[0], pos[1], 10, 10))  #тело змейки его цвет и позиция
    pygame.draw.rect(game_window, red, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))  #яблочко его позиция и цвет
        
    if snake_position[0] < 0 or snake_position[0] > x - 10 : #змейка ударилась о левую или вправую стенку
        game_over()
    if snake_position[1] < 0 or snake_position[1] > y - 10 : #а теперь ударилась об вверхнюю или нижнюю границу
        game_over()
        
    for block in snake_body[1 :] : #проверка всего тела кроме головы
        if snake_position[0] == block[0] and snake_position[1] == block[1] :
            game_over() # если она ударился об свое же тело игра тоже заканчивается

    show_info(white, 'times new roman', 20) #прказывает поинты
    pygame.display.update() #обновление экрана 
    fps.tick(snake_speed) 
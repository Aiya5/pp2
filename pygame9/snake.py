import pygame #пайгейм
import time #вреям
import random #для рандомного появление яблочек

# параметры окна и скорости
x=720 #широта
y=480 #высота
snake_speed = 15 #СПИД

# цвета
black = pygame.Color(0, 0, 0)  #ччерный
white = pygame.Color(255, 255, 255) #белый
red = pygame.Color(255, 0, 0) #красный
green = pygame.Color(0, 255, 0) #зеленый
blue=pygame.Color(0, 0, 255) #королевский синий
pink=pygame.Color(255,209,220) #розизий

pygame.init() #инициализация пайгейма
pygame.display.set_caption('Snake')  #название в уголке вкладки
game_window = pygame.display.set_mode((x, y)) #размеры параметры окошко
fps = pygame.time.Clock() #время обновления фпс

# добавляем музыку для змейки
pygame.mixer.music.load("snakessong.mp3")  # положи файл snake_music.mp3 в папку
pygame.mixer.music.play(-1)  # играет бесконечно
pygame.mixer.music.set_volume(0.3)  # громкость

# змейка
snake_position = [100, 50] #позиция северуса
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]] #размеры змейки

# фрукт
fruit_position = [random.randrange(1, (x // 10)) * 10,
                  random.randrange(1, (y // 10)) * 10] # а вот и рандомное позиция яблочки
fruit_spawn = True #появление существование яблочко тру

# разные веса фруктов + таймер исчезновения 
fruit_weight = random.choice([5, 10, 15, 20])  # вес фруктов случайный
fruit_timer = time.time()  # время появления фрукта
fruit_lifetime = random.randint(3, 7)  # фрукт живет от 3 до 7 секунд
# -------------------------------------------------------------

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
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, green)
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
                
    #А это чтобы змейкаа не разделилась если одновременно начать
    if change_to == 'UP' and direction != 'DOWN' :
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP' :
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT' :
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT' :
        direction = 'RIGHT'
        
    #параметры на сколько пикселей и куда поворачивает и двигается змейка
    if direction == 'UP' :
        snake_position[1] -= 10
    if direction == 'DOWN' :
        snake_position[1] += 10
    if direction == 'LEFT' :
        snake_position[0] -= 10
    if direction == 'RIGHT' :
        snake_position[0] += 10
        
    #удлинение тела змейки
    snake_body.insert(0, list(snake_position))
    
    # фрукт исчезает сам спустя время ---
    if time.time() - fruit_timer > fruit_lifetime:
        fruit_spawn = False
    # -----------------------------------------------
    
    # змейка съела яблочко или нет проверяет
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += fruit_weight  #поинты = вес фрукта
        fruit_spawn = False  # фрукт исчезает
    else:
        snake_body.pop() #удаляет хвост если змейка не съела яблочко

    # новая позиция фрукта
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (x // 10)) * 10,
                          random.randrange(1, (y // 10)) * 10]
        fruit_weight = random.choice([5, 10, 15, 20])  # случайный вес
        fruit_timer = time.time()  # новое время появления
        fruit_lifetime = random.randint(3, 7)  # фрукт живет 3–7 секунд
    fruit_spawn = True

    # проверка повышения уровня
    if score // 30 > last_level_up: #условие больше 30 поинтов
        last_level_up = score // 30 
        level += 1 #плюс уровень
        snake_speed += 3 #увеличивает скорость змейки
        
    # черный бэграунд
    game_window.fill(black) 
    for pos in snake_body :  #проходится по всей длине змейки
        pygame.draw.rect(game_window, pink,pygame.Rect(pos[0], pos[1], 10, 10))  #тело змейки его цвет и позиция
    
    # яблочко
    pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    
    #показываем вес фруктов рядом с яблочком
    weight_text = pygame.font.SysFont('times new roman', 10).render(str(fruit_weight), True, white)
    game_window.blit(weight_text, (fruit_position[0], fruit_position[1] - 10))
        
    # столкновение со стеной
    if snake_position[0] < 0 or snake_position[0] > x - 10 :
        game_over()
    if snake_position[1] < 0 or snake_position[1] > y - 10 :
        game_over()
        
    # столкновение с телом
    for block in snake_body[1:] :
        if snake_position[0] == block[0] and snake_position[1] == block[1] :
            game_over() 

    # показать очки и уровень
    show_info(white, 'times new roman', 20)
    pygame.display.update() #обновление экрана 
    fps.tick(snake_speed)

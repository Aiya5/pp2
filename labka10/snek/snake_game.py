import pygame
import time
import random
import psycopg2
from config import load_config

config = load_config()

def create_user(username):
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT id FROM "user" WHERE username=%s;', (username,))
                row = cur.fetchone()

                if row:
                    user_id = row[0]
                    print(f"Welcome back, {username}, baby!")

                    # псоледний резульати
                    cur.execute("""SELECT score FROM user_score 
                                   WHERE user_id=%s ORDER BY played_at DESC LIMIT 1;""",
                                (user_id,))
                    last = cur.fetchone()
                    if last:
                        print("Your last score:", last[0])
                    return user_id

                # новый игратель 
                cur.execute('INSERT INTO "user"(username) VALUES(%s) RETURNING id;', (username,))
                user_id = cur.fetchone()[0]
                conn.commit()
                print("New user:", username)
                return user_id
    except Exception as e:
        print("DB ERROR:", e)

def save_score(user_id, score):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                # играл человек или нет проверяем
                cur.execute("""
                    SELECT id, score 
                    FROM user_score
                    WHERE user_id = %s
                    ORDER BY score DESC
                    LIMIT 1;
                """, (user_id,))
                row = cur.fetchone()

                if row is None:
                    #самый первый скор по первой игре
                    cur.execute("""
                        INSERT INTO user_score (user_id, score)
                        VALUES (%s, %s);
                    """, (user_id, score))
                    conn.commit()
                    print(f"First score saved: {score}")
                    return

                current_id, current_high = row

                # не сохраняем новый кот потому что он меньше
                if score <= current_high:
                    print(f"Score {score} NOT saved (current high = {current_high})")
                    return

                # уддаляем старый если новый скор больше чем старыенькии
                cur.execute("""
                    DELETE FROM user_score 
                    WHERE id = %s;
                """, (current_id,))

                cur.execute("""
                    INSERT INTO user_score (user_id, score)
                    VALUES (%s, %s);
                """, (user_id, score))

                conn.commit()
                print(f"New HIGHEST score : {score}")

    except Exception as e:
        print("save ERROR:", e)


#Запршивает имя человечка чтобы запсиать его в таблицу
username = input("Enter username: ")
user_id = create_user(username)
#мой игровой код
# параметры окна
x = 720
y = 480
snake_speed = 15

# цвета
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
pink = pygame.Color(255, 209, 220)

pygame.init()
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((x, y))
fps = pygame.time.Clock()

# музыка
pygame.mixer.music.load("snakessong.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

# змейка
snake_position = [100, 50]
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

# фрукт
fruit_position = [random.randrange(1, (x // 10)) * 10,
                  random.randrange(1, (y // 10)) * 10]
fruit_spawn = True

fruit_weight = random.choice([5, 10, 15, 20])
fruit_timer = time.time()
fruit_lifetime = random.randint(3, 7)

direction = 'RIGHT'
change_to = direction
score = 0
level = 1
last_level_up = 0

paused = False  #пауза

def show_info(color, font, size):
    info_font = pygame.font.SysFont(font, size)
    info_surface = info_font.render(f"Score: {score}  Level: {level}", True, color)
    info_rect = info_surface.get_rect()
    game_window.blit(info_surface, info_rect)


def game_over():
    save_score(user_id, score)

    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, green)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (x / 2, y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

obstacles = []

def generate_obstacles(level):
    #новые блохи 
    blocks = []
    count = 3 + level * 3      #о нет их больше
    for _ in range(count):
        bx = random.randrange(1, (x // 10)) * 10
        by = random.randrange(1, (y // 10)) * 10
        blocks.append([bx, by])
    return blocks

#основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            #пауза
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    print("Game paused. Saving score...")
                    save_score(user_id, score)

            if not paused:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

    if paused:
    # рисует вместо заморозки
       game_window.fill(black)
       pause_font = pygame.font.SysFont('times new roman', 50)
       pause_surface = pause_font.render("PAUSED", True, white)
       pause_rect = pause_surface.get_rect(center=(x // 2, y // 2))
       game_window.blit(pause_surface, pause_rect)
       pygame.display.update()
       fps.tick(5)  #обновляет через 5сек
       continue

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    #движение змейки
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))

    # время фруктов
    if time.time() - fruit_timer > fruit_lifetime:
        fruit_spawn = False

    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += fruit_weight
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (x // 10)) * 10,
                          random.randrange(1, (y // 10)) * 10]
        fruit_weight = random.choice([5, 10, 15, 20])
        fruit_timer = time.time()
        fruit_lifetime = random.randint(3, 7)
    fruit_spawn = True

    #уровень
    if score // 30 > last_level_up:
        last_level_up = score // 30
        level += 1
        snake_speed += 3

        if level >= 2:
            obstacles = generate_obstacles(level)
            
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, pink, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    # рисуем препятствия
    for obs in obstacles:
        pygame.draw.rect(game_window, blue, pygame.Rect(obs[0], obs[1], 10, 10))


    weight_text = pygame.font.SysFont('times new roman', 10).render(str(fruit_weight), True, white)
    game_window.blit(weight_text, (fruit_position[0], fruit_position[1] - 10))

    #столкновение со стеной
    if snake_position[0] < 0 or snake_position[0] > x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > y - 10:
        game_over()

    #суицид змейки
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    # столкновение с препятствиями
    for obs in obstacles:
        if snake_position[0] == obs[0] and snake_position[1] == obs[1]:
            game_over()

    show_info(white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(snake_speed)

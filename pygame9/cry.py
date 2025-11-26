# all_tasks_demo.py
# Single-file collection of 25 mini Pygame demos (tasks generated previously).
# Set TASK = 1..25 to run a particular demo.
import pygame, random, math, time, sys
pygame.init()

WIDTH, HEIGHT = 700, 700
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (219,7,1)
GREEN = (0,200,0)
BLUE  = (50,50,255)
GOLD  = (255,215,0)

TASK = 1  # CHANGE this 1..25 to run a specific task demo

def handle_quit_events():
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit(); sys.exit()

# ---------------------
# LEVEL 1 - EASY TASKS
# ---------------------

# 1. Falling Obstacles - rectangles fall from top, collision -> game over
def run_task1():
    player = pygame.Rect(WIDTH//2-30, HEIGHT-60, 60, 30)
    obstacles=[]
    spawn_timer=0
    speed = 3
    game_over=False
    while True:
        handle_quit_events()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x -= 6
        if keys[pygame.K_RIGHT]: player.x += 6
        player.x = max(0, min(WIDTH-player.w, player.x))

        spawn_timer += 1
        if spawn_timer>40:
            spawn_timer=0
            obstacles.append(pygame.Rect(random.randint(0,WIDTH-40), -30, random.randint(30,80), 20))
        for o in obstacles:
            o.y += speed
        obstacles = [o for o in obstacles if o.y < HEIGHT+50]
        for o in obstacles:
            if player.colliderect(o): game_over=True

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player)
        for o in obstacles: pygame.draw.rect(screen, RED, o)
        if game_over:
            font=pygame.font.SysFont(None,80); screen.blit(font.render("GAME OVER",True,RED),(150,HEIGHT//2-40))
        pygame.display.flip(); clock.tick(FPS)

# 2. Speed Up Over Time - increase speed every 10 sec
def run_task2():
    player = pygame.Rect(WIDTH//2-25, HEIGHT-60, 50, 30)
    speed = 4
    start = time.time()
    while True:
        handle_quit_events()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x -= speed
        if keys[pygame.K_RIGHT]: player.x += speed
        player.x = max(0, min(WIDTH-player.w, player.x))
        # speed up every 10 sec
        elapsed = time.time()-start
        speed = 4 + int(elapsed // 10)
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player)
        font=pygame.font.SysFont(None,30); screen.blit(font.render(f"Speed: {speed}",True,BLACK),(10,10))
        pygame.display.flip(); clock.tick(FPS)

# 3. Multi-color Coins - different coin types with different scores
def run_task3():
    player = pygame.Rect(WIDTH//2-50, HEIGHT-60, 100, 20)
    coins=[]  # (x,y,type) type: 'gold'=1,'silver'=2,'red'=-1
    coin_speed=3
    score=0
    while True:
        handle_quit_events()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x -= 6
        if keys[pygame.K_RIGHT]: player.x += 6
        player.x = max(0, min(WIDTH-player.w, player.x))
        if random.random() < 0.02:
            t = random.choices(['gold','silver','red'], [0.6,0.3,0.1])[0]
            coins.append([random.randint(10,WIDTH-10), -10, t])
        for c in coins:
            c[1] += coin_speed
        for c in coins[:]:
            if pygame.Rect(c[0]-8,c[1]-8,16,16).colliderect(player):
                if c[2]=='gold': score+=1
                elif c[2]=='silver': score+=2
                else: score-=1
                coins.remove(c)
            elif c[1]>HEIGHT: coins.remove(c)
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player)
        for c in coins:
            col = GOLD if c[2]=='gold' else (200,200,200) if c[2]=='silver' else RED
            pygame.draw.circle(screen, col, (c[0], int(c[1])), 8)
        font=pygame.font.SysFont(None,36); screen.blit(font.render(f"Score: {score}",True,BLACK),(10,10))
        pygame.display.flip(); clock.tick(FPS)

# 4. Bouncing Ball - ball bounces and changes direction at walls
def run_task4():
    x,y = WIDTH//2, HEIGHT//2
    vx,vy = 4,3
    r=20
    while True:
        handle_quit_events()
        x+=vx; y+=vy
        if x-r<=0 or x+r>=WIDTH: vx *= -1
        if y-r<=0 or y+r>=HEIGHT: vy *= -1
        screen.fill(WHITE)
        pygame.draw.circle(screen, BLUE, (int(x),int(y)), r)
        pygame.display.flip(); clock.tick(FPS)

# 5. Player Lives - 3 lives, collision loses life
def run_task5():
    player = pygame.Rect(WIDTH//2-30, HEIGHT-60, 60, 30)
    obstacles=[]
    spawn_timer=0
    lives=3
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=6
        if keys[pygame.K_RIGHT]: player.x+=6
        player.x = max(0, min(WIDTH-player.w, player.x))
        spawn_timer+=1
        if spawn_timer>50: spawn_timer=0; obstacles.append(pygame.Rect(random.randint(0,WIDTH-40), -30, random.randint(30,80), 20))
        for o in obstacles: o.y+=4
        for o in obstacles[:]:
            if player.colliderect(o):
                lives-=1
                obstacles.remove(o)
            elif o.y>HEIGHT: obstacles.remove(o)
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player)
        for o in obstacles: pygame.draw.rect(screen, RED, o)
        font=pygame.font.SysFont(None,36); screen.blit(font.render(f"Lives: {lives}",True,BLACK),(10,10))
        if lives<=0: screen.blit(pygame.font.SysFont(None,80).render("GAME OVER",True,RED),(150,HEIGHT//2-40))
        pygame.display.flip(); clock.tick(FPS)

# ---------------------
# LEVEL 2 - MEDIUM TASKS
# ---------------------

# 6. Random Shape Generator every 5 seconds (triangle,circle,rect,pentagon)
def run_task6():
    shapes=[]
    last_spawn=time.time()
    def spawn():
        t=random.choice(['tri','circ','rect','pent'])
        x=random.randint(80,WIDTH-80); y=random.randint(120,HEIGHT-120)
        size=random.randint(20,60)
        col=(random.randint(50,255),random.randint(50,255),random.randint(50,255))
        shapes.append({'t':t,'x':x,'y':y,'s':size,'c':col})
    while True:
        handle_quit_events()
        if time.time()-last_spawn>5:
            spawn(); last_spawn=time.time()
        screen.fill(WHITE)
        for s in shapes:
            if s['t']=='tri':
                pts=[(s['x'],s['y']), (s['x']-s['s'], s['y']+s['s']), (s['x']+s['s'], s['y']+s['s'])]
                pygame.draw.polygon(screen, s['c'], pts)
            elif s['t']=='circ':
                pygame.draw.circle(screen, s['c'], (s['x'],s['y']), s['s'])
            elif s['t']=='rect':
                pygame.draw.rect(screen, s['c'], (s['x']-s['s']//2,s['y']-s['s']//2,s['s'],s['s']))
            else:
                # pentagon
                pts=[]
                for i in range(5):
                    a = i*2*math.pi/5 - math.pi/2
                    pts.append((s['x']+math.cos(a)*s['s'], s['y']+math.sin(a)*s['s']))
                pygame.draw.polygon(screen, s['c'], pts)
        pygame.display.flip(); clock.tick(FPS)

# 7. Moving Platforms - platforms move left/right, player can ride
def run_task7():
    player = pygame.Rect(350, HEIGHT-120, 40, 40)
    vel_y=0; gravity=0.6
    platforms=[{'r':pygame.Rect(100,500,160,16),'vx':2}, {'r':pygame.Rect(350,400,180,16),'vx':-3}]
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x -=5
        if keys[pygame.K_RIGHT]: player.x +=5
        # gravity
        vel_y += gravity; player.y += vel_y
        # simple ground
        if player.bottom > HEIGHT: player.bottom = HEIGHT; vel_y = 0
        # platforms move
        on_platform=False
        for p in platforms:
            p['r'].x += p['vx']
            if p['r'].left < 0 or p['r'].right > WIDTH: p['vx'] *= -1
            if player.colliderect(p['r']) and vel_y>=0 and player.bottom - p['r'].top < 20:
                player.bottom = p['r'].top
                vel_y = 0
                on_platform=True
                # ride with platform
                player.x += p['vx']
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player)
        for p in platforms: pygame.draw.rect(screen, BLACK, p['r'])
        pygame.display.flip(); clock.tick(FPS)

# 8. Rotating Triangle - triangle rotates around center and collision preserved (bounding box)
def run_task8():
    cx,cy = WIDTH//2, HEIGHT//2
    size=60
    angle=0
    player = pygame.Rect(50, HEIGHT-80, 80, 30)
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=6
        if keys[pygame.K_RIGHT]: player.x+=6
        angle += 2
        # triangle points
        pts=[]
        for a in [ -90, 30, 150 ]:
            rad = math.radians(a+angle)
            pts.append((cx + math.cos(rad)*size, cy + math.sin(rad)*size))
        tri_rect = pygame.Rect(min(p[0] for p in pts), min(p[1] for p in pts),
                               max(p[0] for p in pts)-min(p[0] for p in pts),
                               max(p[1] for p in pts)-min(p[1] for p in pts))
        collided = player.colliderect(tri_rect)
        screen.fill(WHITE)
        pygame.draw.polygon(screen, GREEN if collided else RED, pts)
        pygame.draw.rect(screen, BLUE, player)
        pygame.display.flip(); clock.tick(FPS)

# 9. Timed Challenge - 30s timer, collect coins as many as possible
def run_task9():
    player = pygame.Rect(WIDTH//2-30, HEIGHT-80, 60, 30)
    coins=[]
    score=0; start=time.time(); duration=30
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=6
        if keys[pygame.K_RIGHT]: player.x+=6
        if random.random()<0.02: coins.append([random.randint(20,WIDTH-20), -10])
        for c in coins: c[1]+=3
        for c in coins[:]:
            if pygame.Rect(c[0]-8,c[1]-8,16,16).colliderect(player):
                score+=1; coins.remove(c)
            elif c[1]>HEIGHT: coins.remove(c)
        tleft = max(0, duration - (time.time()-start))
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player)
        for c in coins: pygame.draw.circle(screen, GOLD, (int(c[0]),int(c[1])),8)
        f=pygame.font.SysFont(None,36); screen.blit(f.render(f"Score:{score}",True,BLACK),(10,10))
        screen.blit(f.render(f"Time:{int(tleft)}",True,BLACK),(10,40))
        if tleft<=0:
            screen.blit(pygame.font.SysFont(None,80).render("TIME UP",True,RED),(200,HEIGHT//2-40))
        pygame.display.flip(); clock.tick(FPS)

# 10. Collect the Correct Shape - prompt target shape every 10s
def run_task10():
    shapes=[]
    last_spawn=time.time(); target=None; last_target=time.time()
    player = pygame.Rect(WIDTH//2-30, HEIGHT-60, 60, 30)
    score=0
    def spawn():
        t=random.choice(['tri','circ','rect'])
        shapes.append({'t':t,'x':random.randint(80,WIDTH-80),'y':random.randint(120,HEIGHT-200)})
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=6
        if keys[pygame.K_RIGHT]: player.x+=6
        if time.time()-last_spawn>1.2: spawn(); last_spawn=time.time()
        if time.time()-last_target>10:
            target=random.choice(['tri','circ','rect']); last_target=time.time()
        for s in shapes[:]:
            r = pygame.Rect(s['x']-20,s['y']-20,40,40)
            if r.colliderect(player):
                if s['t']==target: score+=1
                else: score-=1
                shapes.remove(s)
        screen.fill(WHITE)
        for s in shapes:
            if s['t']=='tri': pygame.draw.polygon(screen,RED,[(s['x'],s['y']),(s['x']-20,s['y']+30),(s['x']+20,s['y']+30)])
            elif s['t']=='circ': pygame.draw.circle(screen,BLUE,(s['x'],s['y']),18)
            else: pygame.draw.rect(screen,BLACK,(s['x']-20,s['y']-20,40,40))
        pygame.draw.rect(screen, GREEN, player)
        f=pygame.font.SysFont(None,36)
        screen.blit(f.render(f"Target: {target}",True,BLACK),(10,10))
        screen.blit(f.render(f"Score:{score}",True,BLACK),(10,40))
        pygame.display.flip(); clock.tick(FPS)

# ---------------------
# LEVEL 3 - ADVANCED TASKS
# ---------------------

# 11. Enemy Following Player (X-axis)
def run_task11():
    player = pygame.Rect(WIDTH//2-25, HEIGHT-60, 50, 30)
    enemy = pygame.Rect(50, 100, 80, 30)
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=6
        if keys[pygame.K_RIGHT]: player.x+=6
        # follow x
        if enemy.centerx < player.centerx: enemy.x += 2
        if enemy.centerx > player.centerx: enemy.x -= 2
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player)
        pygame.draw.rect(screen, RED, enemy)
        pygame.display.flip(); clock.tick(FPS)

# 12. Pathfinding Enemy - predefined path L->D->R->U
def run_task12():
    player = pygame.Rect(WIDTH//2-25, HEIGHT-60, 50, 30)
    path = [(0,2),(2,0),(0,-2),(-2,0)]  # down,right,up,left (cycled)
    enemy = pygame.Rect(100,100,50,30); pi=0; steps=0
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=6
        if keys[pygame.K_RIGHT]: player.x+=6
        dx,dy = path[pi]; enemy.x += dx; enemy.y += dy; steps += 1
        if steps>150: steps=0; pi=(pi+1)%len(path)
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player); pygame.draw.rect(screen, RED, enemy)
        pygame.display.flip(); clock.tick(FPS)

# 13. Laser Obstacles - horizontal laser appears for 2 seconds
def run_task13():
    player = pygame.Rect(WIDTH//2-20, HEIGHT-80, 40, 30)
    laser_on=False; last_switch=time.time()
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=6
        if keys[pygame.K_RIGHT]: player.x+=6
        if time.time()-last_switch>4:
            laser_on=True; laser_y=random.randint(100,HEIGHT-200); last_switch=time.time()
        if laser_on and time.time()-last_switch>2: laser_on=False; last_switch=time.time()
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player)
        if laser_on:
            pygame.draw.rect(screen, RED, (0,laser_y,WIDTH,6))
            if player.top <= laser_y+6 and player.bottom >= laser_y:
                screen.blit(pygame.font.SysFont(None,60).render("HIT!",True,RED),(280,50))
        pygame.display.flip(); clock.tick(FPS)

# 14. Teleporting Triangle every 3 seconds
def run_task14():
    player = pygame.Rect(WIDTH//2-30, HEIGHT-60, 60, 30)
    def gen_tri():
        x=random.randint(100,WIDTH-100); y=random.randint(100,HEIGHT-200); s=40
        return [(x,y),(x-s,y+s),(x+s,y+s)]
    tri = gen_tri(); last = time.time()
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=6
        if keys[pygame.K_RIGHT]: player.x+=6
        if time.time()-last>3:
            tri = gen_tri(); last=time.time()
        tri_rect = pygame.Rect(min(p[0] for p in tri), min(p[1] for p in tri),
                               max(p[0] for p in tri)-min(p[0] for p in tri),
                               max(p[1] for p in tri)-min(p[1] for p in tri))
        screen.fill(WHITE)
        pygame.draw.polygon(screen, GREEN, tri)
        pygame.draw.rect(screen, BLUE, player)
        if player.colliderect(tri_rect): pygame.draw.circle(screen, RED, (50,50), 15)
        pygame.display.flip(); clock.tick(FPS)

# 15. Combo Scoring - 3 coins within 4s => +5 bonus
def run_task15():
    player = pygame.Rect(WIDTH//2-30, HEIGHT-80, 60, 30)
    coins=[]  # (x,y,timestamp)
    collected_times=[]
    score=0
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=6
        if keys[pygame.K_RIGHT]: player.x+=6
        if random.random()<0.02: coins.append([random.randint(20,WIDTH-20), -10, time.time()])
        for c in coins: c[1]+=3
        for c in coins[:]:
            if pygame.Rect(c[0]-8,c[1]-8,16,16).colliderect(player):
                collected_times.append(time.time()); score += 1; coins.remove(c)
        # check combos
        # count how many collected in last 4 seconds
        now=time.time()
        recent=[t for t in collected_times if now-t<=4]
        if len(recent) >= 3:
            score += 5
            collected_times = []  # reset after awarding
        collected_times = [t for t in collected_times if now-t<=4]
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player)
        for c in coins: pygame.draw.circle(screen, GOLD, (int(c[0]),int(c[1])),8)
        f=pygame.font.SysFont(None,36); screen.blit(f.render(f"Score:{score}",True,BLACK),(10,10))
        pygame.display.flip(); clock.tick(FPS)

# ---------------------
# LEVEL 4 - HARD TASKS
# ---------------------

# 16. Shape Memory Game - touch shapes in the shown order
def run_task16():
    seq=[]
    shapes=[]  # list of (type,rect)
    types = ['tri','circ','rect']
    def gen_shapes():
        shapes.clear()
        for i in range(5):
            t=random.choice(types)
            r=pygame.Rect(100+i*100,200,60,60)
            shapes.append((t,r))
    gen_shapes()
    show_seq=True; idx=0; started=False; message=""
    while True:
        handle_quit_events()
        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit(); sys.exit()
            if e.type==pygame.MOUSEBUTTONDOWN and not show_seq:
                for i,(t,r) in enumerate(shapes):
                    if r.collidepoint(e.pos):
                        if seq[idx]==t:
                            idx+=1
                            if idx==len(seq): message="YOU WIN"; show_seq=True; idx=0
                        else:
                            message="WRONG"; show_seq=True; idx=0
        if show_seq:
            seq = [random.choice(types) for _ in range(3)]
            show_seq=False; time.sleep(0.8)
        screen.fill(WHITE)
        for i,(t,r) in enumerate(shapes):
            c = (200,200,255) if seq and seq[min(i,len(seq)-1)]==t else (220,220,220)
            pygame.draw.rect(screen, c, r)
            if t=='tri': pygame.draw.polygon(screen,RED,[(r.centerx,r.top),(r.left,r.bottom),(r.right,r.bottom)])
            elif t=='circ': pygame.draw.circle(screen,BLUE,r.center, r.w//2-4)
            else: pygame.draw.rect(screen,BLACK,r.inflate(-10,-10),2)
        if message: screen.blit(pygame.font.SysFont(None,60).render(message,True,RED),(250,50))
        pygame.display.flip(); clock.tick(FPS)

# 17. Moving Maze - moving walls; player avoid touching
def run_task17():
    player = pygame.Rect(60,60,30,30)
    walls = [pygame.Rect(150,0,20,300), pygame.Rect(350,400,20,300)]
    directions = [2,-3]
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=5
        if keys[pygame.K_RIGHT]: player.x+=5
        if keys[pygame.K_UP]: player.y-=5
        if keys[pygame.K_DOWN]: player.y+=5
        for i,w in enumerate(walls):
            w.y += directions[i]
            if w.top<0 or w.bottom>HEIGHT: directions[i]*=-1
        hit=False
        for w in walls:
            if player.colliderect(w): hit=True
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player)
        for w in walls: pygame.draw.rect(screen, BLACK, w)
        if hit: screen.blit(pygame.font.SysFont(None,60).render("TOUCHED",True,RED),(250,50))
        pygame.display.flip(); clock.tick(FPS)

# 18. Mini Boss - boss with 100 HP, player shoots with SPACE, boss fires projectiles
def run_task18():
    player = pygame.Rect(WIDTH//2-20, HEIGHT-60, 40, 30)
    boss = pygame.Rect(WIDTH//2-60,50,120,60); boss_hp=100
    bullets=[]; boss_shots=[]
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=6
        if keys[pygame.K_RIGHT]: player.x+=6
        if keys[pygame.K_SPACE]:
            bullets.append(pygame.Rect(player.centerx-4, player.top-8, 8, 12))
        for b in bullets: b.y -= 8
        if random.random()<0.02: boss_shots.append(pygame.Rect(boss.centerx-6,boss.bottom,12,12))
        for s in boss_shots: s.y += 6
        for b in bullets[:]:
            if b.colliderect(boss): boss_hp -= 5; bullets.remove(b)
            elif b.bottom < 0: bullets.remove(b)
        for s in boss_shots[:]:
            if s.colliderect(player): # you can handle player damage here
                boss_shots.remove(s)
            elif s.top > HEIGHT: boss_shots.remove(s)
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player)
        pygame.draw.rect(screen, RED, boss)
        for b in bullets: pygame.draw.rect(screen,BLACK,b)
        for s in boss_shots: pygame.draw.rect(screen,BLACK,s)
        f=pygame.font.SysFont(None,30); screen.blit(f.render(f"Boss HP: {boss_hp}",True,BLACK),(10,10))
        if boss_hp<=0: screen.blit(pygame.font.SysFont(None,80).render("BOSS DOWN",True,GREEN),(180,HEIGHT//2-40))
        pygame.display.flip(); clock.tick(FPS)

# 19. Dynamic Lighting - dark screen with small light radius around player
def run_task19():
    player = pygame.Rect(WIDTH//2-20, HEIGHT//2-20, 40, 40)
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=6
        if keys[pygame.K_RIGHT]: player.x+=6
        if keys[pygame.K_UP]: player.y-=6
        if keys[pygame.K_DOWN]: player.y+=6
        screen.fill(BLACK)
        # draw a light circle as white on black background using a surface
        light = pygame.Surface((WIDTH, HEIGHT))
        light.fill(BLACK)
        pygame.draw.circle(light, (255,255,255), player.center, 120)
        light.set_colorkey((0,0,0))
        screen.blit(light, (0,0), special_flags=pygame.BLEND_RGBA_ADD)
        pygame.draw.rect(screen, BLUE, player)
        pygame.display.flip(); clock.tick(FPS)

# 20. Physics Drop - coins have gravity and bounce slightly on ground
def run_task20():
    coins = []  # x,y,vx,vy
    while True:
        handle_quit_events()
        if random.random()<0.03: coins.append([random.randint(50,WIDTH-50),50, random.uniform(-2,2), 0])
        for c in coins:
            c[3] += 0.35  # gravity
            c[0] += c[2]; c[1] += c[3]
            if c[1] > HEIGHT-12:
                c[1] = HEIGHT-12
                c[3] *= -0.5
                c[2] *= 0.98
                if abs(c[3]) < 0.5: c[3]=0
        screen.fill(WHITE)
        for c in coins: pygame.draw.circle(screen, GOLD, (int(c[0]),int(c[1])), 10)
        pygame.display.flip(); clock.tick(FPS)

# ---------------------
# LEVEL 5 - VERY ADVANCED TASKS
# ---------------------

# 21. Simple Game Engine - load levels from dict
def run_task21():
    class GameObj:
        def __init__(self,x,y,w,h,col): self.r=pygame.Rect(x,y,w,h); self.col=col
        def draw(self): pygame.draw.rect(screen,self.col,self.r)
    levels = {
        1: [GameObj(100,500,200,20,BLACK), GameObj(350,400,150,20,BLACK)],
        2: [GameObj(0,300,700,20,BLACK)]
    }
    current=1
    player=pygame.Rect(50,50,30,30)
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=4
        if keys[pygame.K_RIGHT]: player.x+=4
        screen.fill(WHITE)
        for obj in levels[current]: obj.draw()
        pygame.draw.rect(screen,BLUE,player)
        pygame.display.flip(); clock.tick(FPS)

# 22. Multiplayer (Same Keyboard)
def run_task22():
    p1 = pygame.Rect(100, HEIGHT-60, 40, 40)
    p2 = pygame.Rect(WIDTH-140, HEIGHT-60, 40, 40)
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]: p1.x -=5
        if keys[pygame.K_d]: p1.x +=5
        if keys[pygame.K_LEFT]: p2.x -=5
        if keys[pygame.K_RIGHT]: p2.x +=5
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, p1); pygame.draw.rect(screen, GREEN, p2)
        pygame.display.flip(); clock.tick(FPS)

# 23. Shadow Effects - shadow under falling object scales
def run_task23():
    x = WIDTH//2; y=50; vy=0
    while True:
        handle_quit_events()
        vy += 0.5; y += vy
        if y>HEIGHT-50: y=HEIGHT-50; vy *= -0.4
        # shadow size based on height
        shadow_w = max(20, int(100*(1 - (y/HEIGHT))))
        screen.fill(WHITE)
        pygame.draw.ellipse(screen, (50,50,50,100), (x-shadow_w//2, HEIGHT-40, shadow_w, 20))
        pygame.draw.circle(screen, RED, (int(x),int(y)), 20)
        pygame.display.flip(); clock.tick(FPS)

# 24. Image-based Sprites - using placeholder rectangles (no external files)
def run_task24():
    # since we should not rely on external images, simulate with colored rectangles
    player = pygame.Rect(WIDTH//2-30, HEIGHT-60, 60, 40)
    enemy = pygame.Rect(100,100,60,40)
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=6
        if keys[pygame.K_RIGHT]: player.x+=6
        screen.fill(WHITE)
        # pretend these are images
        pygame.draw.rect(screen, (200,100,100), enemy)
        pygame.draw.rect(screen, (100,100,200), player)
        pygame.display.flip(); clock.tick(FPS)

# 25. Save/Load High Score
def run_task25():
    player = pygame.Rect(WIDTH//2-30, HEIGHT-60, 60, 30)
    coins=[]; score=0; high=0
    # try load
    try:
        with open("highscore.txt","r") as f: high=int(f.read().strip() or 0)
    except: high=0
    while True:
        handle_quit_events()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x-=6
        if keys[pygame.K_RIGHT]: player.x+=6
        if random.random()<0.02: coins.append([random.randint(20,WIDTH-20), -10])
        for c in coins: c[1]+=3
        for c in coins[:]:
            if pygame.Rect(c[0]-8,c[1]-8,16,16).colliderect(player):
                score+=1; coins.remove(c)
            elif c[1]>HEIGHT: coins.remove(c)
        if score>high: high=score
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player)
        for c in coins: pygame.draw.circle(screen, GOLD, (int(c[0]),int(c[1])),8)
        f=pygame.font.SysFont(None,36); screen.blit(f.render(f"Score:{score}",True,BLACK),(10,10)); screen.blit(f.render(f"High:{high}",True,BLACK),(10,40))
        pygame.display.flip(); clock.tick(FPS)
        # save high periodically
        with open("highscore.txt","w") as f: f.write(str(high))

# ---------------------
# TASK RUNNER
# ---------------------
task_funcs = {
 5: run_task5, 2: run_task2, 3: run_task3, 4: run_task4, 1: run_task1,
 6: run_task6, 7: run_task7, 8: run_task8, 9: run_task9, 10: run_task10,
 11: run_task11, 12: run_task12, 13: run_task13, 14: run_task14, 15: run_task15,
 16: run_task16, 17: run_task17, 18: run_task18, 19: run_task19, 20: run_task20,
 21: run_task21, 22: run_task22, 23: run_task23, 24: run_task24, 25: run_task25
}

if __name__ == "__main__":
    if TASK in task_funcs:
        task_funcs[TASK]()
    else:
        print("Set TASK to 1..25 at top of file.")

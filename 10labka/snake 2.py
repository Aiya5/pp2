import pygame
import sys
import random
import psycopg2
from psycopg2 import Error
import json
import time

class Database:
    def __init__(self):
        self.connection = None
        self.connect()
        self.init_database()
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='postgres',
                database='snake_game',
                port='5432',
                client_encoding='UTF8'
            )
        except Error as e:
            print(f"Error connecting to PostgreSQL: {e}")
    
    def init_database(self):
        """Initialize database tables including high scores"""
        try:
            cursor = self.connection.cursor()
            
            # Users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Saved games table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_scores (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    level INTEGER DEFAULT 1,
                    score INTEGER DEFAULT 0,
                    snake_body TEXT,
                    food_position VARCHAR(50),
                    direction VARCHAR(10),
                    game_speed INTEGER DEFAULT 100,
                    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            ''')
            
            # High scores table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS high_scores (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    username VARCHAR(50) NOT NULL,
                    score INTEGER NOT NULL,
                    level INTEGER NOT NULL,
                    achieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            ''')
            
            self.connection.commit()
            cursor.close()
            print("✅ Database tables initialized")
        except Error as e:
            print(f"❌ Error initializing database: {e}")
    
    def get_user(self, username):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user_data = cursor.fetchone()
            cursor.close()
            
            if user_data:
                columns = [desc[0] for desc in cursor.description]
                user = dict(zip(columns, user_data))
                return user
            return None
        except Error as e:
            print(f"Error getting user: {e}")
            return None
    
    def create_user(self, username):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
            user_id = cursor.fetchone()[0]
            self.connection.commit()
            cursor.close()
            return user_id
        except Error as e:
            print(f"Error creating user: {e}")
            return None
    
    def get_saved_game(self, user_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM user_scores 
                WHERE user_id = %s 
                ORDER BY saved_at DESC 
                LIMIT 1
            """, (user_id,))
            game_data = cursor.fetchone()
            cursor.close()
            
            if game_data:
                columns = [desc[0] for desc in cursor.description]
                game = dict(zip(columns, game_data))
                return game
            return None
        except Error as e:
            print(f"Error getting saved game: {e}")
            return None
    
    def save_game(self, user_id, level, score, snake_body, food_position, direction, game_speed):
        try:
            cursor = self.connection.cursor()
            # Delete previous saved game for this user
            cursor.execute("DELETE FROM user_scores WHERE user_id = %s", (user_id,))
            
            # Insert new saved game
            cursor.execute("""
                INSERT INTO user_scores 
                (user_id, level, score, snake_body, food_position, direction, game_speed) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (user_id, level, score, json.dumps(snake_body), 
                  json.dumps(food_position), direction, game_speed))
            
            saved_id = cursor.fetchone()[0]
            self.connection.commit()
            cursor.close()
            return saved_id
        except Error as e:
            print(f"Error saving game: {e}")
            return None
    
    def save_high_score(self, user_id, username, score, level):
        """Save high score to database"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO high_scores 
                (user_id, username, score, level) 
                VALUES (%s, %s, %s, %s)
            """, (user_id, username, score, level))
            
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error saving high score: {e}")
            return False
    
    def get_high_scores(self, limit=10):
        """Get top high scores"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT username, score, level, achieved_at 
                FROM high_scores 
                ORDER BY score DESC, achieved_at DESC 
                LIMIT %s
            """, (limit,))
            
            scores = cursor.fetchall()
            cursor.close()
            
            high_scores = []
            for score in scores:
                high_scores.append({
                    'username': score[0],
                    'score': score[1],
                    'level': score[2],
                    'achieved_at': score[3]
                })
            return high_scores
        except Error as e:
            print(f"Error getting high scores: {e}")
            return []
    
    def delete_saved_game(self, user_id):
        """Delete saved game for user"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM user_scores WHERE user_id = %s", (user_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error deleting saved game: {e}")
            return False

class SnakeGame:
    def __init__(self):
        pygame.init()
        
        # Game constants
        self.WIDTH, self.HEIGHT = 600, 600
        self.GRID_SIZE = 20
        self.GRID_WIDTH = self.WIDTH // self.GRID_SIZE
        self.GRID_HEIGHT = self.HEIGHT // self.GRID_SIZE
        
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GRAY = (128, 128, 128)
        self.YELLOW = (255, 255, 0)
        self.PURPLE = (128, 0, 128)
        
        # Game setup
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake Game - PostgreSQL")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.title_font = pygame.font.Font(None, 48)
        
        # Game states
        self.MAIN_MENU = 0
        self.PLAYING = 1
        self.GAME_OVER = 2
        self.HIGH_SCORES = 3
        self.current_state = self.MAIN_MENU
        
        # Database
        self.db = Database()
        self.current_user = None
        self.current_level = 1
        
        # Level configurations
        self.levels = {
            1: {"speed": 100, "walls": [], "name": "Beginner", "color": self.GREEN},
            2: {"speed": 80, "walls": self.create_border_walls(), "name": "Intermediate", "color": self.YELLOW},
            3: {"speed": 60, "walls": self.create_maze_walls(), "name": "Advanced", "color": (255, 165, 0)},
            4: {"speed": 40, "walls": self.create_complex_walls(), "name": "Expert", "color": self.RED}
        }
        
        self.reset_game()
    
    def create_border_walls(self):
        """Create border walls for level 2"""
        walls = []
        for i in range(self.GRID_WIDTH):
            walls.append((i, 0))
            walls.append((i, self.GRID_HEIGHT - 1))
        for i in range(1, self.GRID_HEIGHT - 1):
            walls.append((0, i))
            walls.append((self.GRID_WIDTH - 1, i))
        return walls
    
    def create_maze_walls(self):
        walls = []
        center_x = self.GRID_WIDTH // 2
        center_y = self.GRID_HEIGHT // 2
        frame_size = 12
        entrance_size = 4  
        half_frame = frame_size // 2
        half_entrance = entrance_size // 2
        left = center_x - half_frame
        right = center_x + half_frame
        top = center_y - half_frame
        bottom = center_y + half_frame
        
        for x in range(left, right + 1):
            if x < center_x - half_entrance or x > center_x + half_entrance:
                walls.append((x, top))
        for x in range(left, right + 1):
            if x < center_x - half_entrance or x > center_x + half_entrance:
                walls.append((x, bottom))
        for y in range(top, bottom + 1):
            if y < center_y - half_entrance or y > center_y + half_entrance:
                walls.append((left, y))
        for y in range(top, bottom + 1):
            if y < center_y - half_entrance or y > center_y + half_entrance:
                walls.append((right, y))
        return walls
    
    def create_complex_walls(self):
        """Create complex walls for level 4"""
        walls = self.create_maze_walls()
        for i in range(5, 25):
            if i % 3 == 0:
                walls.append((i, 8))
                walls.append((i, 22))
        for i in range(8, 18):
            walls.append((15, i))
            walls.append((i, 12))
        return walls
    
    def reset_game(self):
        """Reset game state"""
        self.snake = [(self.GRID_WIDTH // 2, self.GRID_HEIGHT // 2)]
        self.direction = "RIGHT"
        self.score = 0
        self.game_over = False
        self.paused = False
        
        level_config = self.levels[self.current_level]
        self.game_speed = level_config["speed"]
        self.walls = level_config["walls"]
        self.wall_color = level_config["color"]
        self.food = self.generate_food()
    
    def generate_food(self):
        """Generate food at random position, avoiding snake and walls"""
        while True:
            food = (random.randint(0, self.GRID_WIDTH - 1), 
                   random.randint(0, self.GRID_HEIGHT - 1))
            if food not in self.snake and food not in self.walls:
                return food
    
    def handle_events(self):
        """Handle keyboard events for all game states"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.current_user and not self.game_over and self.current_state == self.PLAYING:
                    self.db.delete_saved_game(self.current_user['id'])
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                # Main menu controls
                if self.current_state == self.MAIN_MENU:
                    if event.key == pygame.K_1:
                        self.current_state = self.PLAYING
                        self.show_level_info(self.current_level)
                        self.reset_game()
                    elif event.key == pygame.K_2:
                        self.current_state = self.HIGH_SCORES
                    elif event.key == pygame.K_3:
                        pygame.quit()
                        sys.exit()
                
                # High scores screen controls
                elif self.current_state == self.HIGH_SCORES:
                    if event.key in [pygame.K_ESCAPE, pygame.K_m]:
                        self.current_state = self.MAIN_MENU
                
                # Playing game controls
                elif self.current_state == self.PLAYING:
                    if not self.game_over:
                        if event.key == pygame.K_p:  # Pause and save game
                            self.pause_and_save()
                        elif event.key == pygame.K_ESCAPE:  # Just pause without saving
                            self.paused = not self.paused
                        
                        # Direction controls (only if not paused)
                        if not self.paused:
                            if event.key == pygame.K_UP and self.direction != "DOWN":
                                self.direction = "UP"
                            elif event.key == pygame.K_DOWN and self.direction != "UP":
                                self.direction = "DOWN"
                            elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                                self.direction = "LEFT"
                            elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                                self.direction = "RIGHT"
                    
                    # Restart game or go to menu
                    if event.key == pygame.K_r and self.game_over:
                        self.reset_game()
                    elif event.key == pygame.K_m and self.game_over:
                        self.current_state = self.MAIN_MENU
                
                # Game over screen controls
                elif self.current_state == self.GAME_OVER:
                    if event.key == pygame.K_r:
                        self.current_state = self.PLAYING
                        self.reset_game()
                    elif event.key == pygame.K_m:
                        self.current_state = self.MAIN_MENU
                    elif event.key == pygame.K_h:
                        self.current_state = self.HIGH_SCORES
    
    def pause_and_save(self):
        """Pause game and save current state to database"""
        if self.current_user:
            self.paused = True
            saved_id = self.db.save_game(
                self.current_user['id'],
                self.current_level,
                self.score,
                self.snake,
                self.food,
                self.direction,
                self.game_speed
            )
            
            if saved_id:
                self.show_message("Game Saved Successfully!", self.GREEN)
            else:
                self.show_message("Failed to Save Game!", self.RED)
    
    def show_message(self, message, color):
        """Show a message on screen"""
        self.screen.fill(self.BLACK)
        message_text = self.font.render(message, True, color)
        instruction_text = self.small_font.render("Press any key to continue...", True, self.WHITE)
        
        self.screen.blit(message_text, (self.WIDTH // 2 - message_text.get_width() // 2, self.HEIGHT // 2 - 20))
        self.screen.blit(instruction_text, (self.WIDTH // 2 - instruction_text.get_width() // 2, self.HEIGHT // 2 + 20))
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False
                    self.paused = False
    
    def move_snake(self):
        """Move the snake"""
        if self.paused or self.game_over or self.current_state != self.PLAYING:
            return
        
        head_x, head_y = self.snake[0]
        
        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)
        
        # Check collision with walls or self
        if (new_head in self.snake or 
            new_head in self.walls or
            new_head[0] < 0 or new_head[0] >= self.GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= self.GRID_HEIGHT):
            self.game_over = True
            self.current_state = self.GAME_OVER
            
            # Save high score and delete saved game
            if self.current_user:
                self.db.save_high_score(
                    self.current_user['id'],
                    self.current_user['username'],
                    self.score,
                    self.current_level
                )
                self.db.delete_saved_game(self.current_user['id'])
            return
        
        self.snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == self.food:
            self.score += 10
            
            # Level up every 50 points
            new_level = self.score // 50 + 1
            if new_level > self.current_level and new_level <= len(self.levels):
                self.current_level = new_level
                level_config = self.levels[self.current_level]
                self.game_speed = level_config["speed"]
                self.walls = level_config["walls"]
                self.wall_color = level_config["color"]
                self.show_level_info(self.current_level)
            
            self.food = self.generate_food()
        else:
            self.snake.pop()
    
    def draw_main_menu(self):
        """Draw main menu screen"""
        self.screen.fill(self.BLACK)
        
        # Title
        title_text = self.title_font.render("SNAKE GAME", True, self.GREEN)
        subtitle_text = self.font.render("PostgreSQL Edition", True, self.YELLOW)
        
        # Menu options
        start_text = self.font.render("1. Start New Game", True, self.WHITE)
        scores_text = self.font.render("2. High Scores", True, self.WHITE)
        quit_text = self.font.render("3. Quit", True, self.WHITE)
        user_text = self.small_font.render(f"Logged in as: {self.current_user['username']}", True, self.GRAY)
        
        # Position elements
        self.screen.blit(title_text, (self.WIDTH // 2 - title_text.get_width() // 2, 100))
        self.screen.blit(subtitle_text, (self.WIDTH // 2 - subtitle_text.get_width() // 2, 160))
        self.screen.blit(start_text, (self.WIDTH // 2 - start_text.get_width() // 2, 250))
        self.screen.blit(scores_text, (self.WIDTH // 2 - scores_text.get_width() // 2, 300))
        self.screen.blit(quit_text, (self.WIDTH // 2 - quit_text.get_width() // 2, 350))
        self.screen.blit(user_text, (self.WIDTH // 2 - user_text.get_width() // 2, 450))
        
        pygame.display.flip()
    
    def draw_high_scores(self):
        """Draw high scores screen"""
        self.screen.fill(self.BLACK)
        
        # Title
        title_text = self.title_font.render("HIGH SCORES", True, self.YELLOW)
        self.screen.blit(title_text, (self.WIDTH // 2 - title_text.get_width() // 2, 50))
        
        # Get high scores
        high_scores = self.db.get_high_scores(10)
        
        # Column headers
        rank_text = self.font.render("Rank", True, self.WHITE)
        name_text = self.font.render("Player", True, self.WHITE)
        score_text = self.font.render("Score", True, self.WHITE)
        level_text = self.font.render("Level", True, self.WHITE)
        
        self.screen.blit(rank_text, (100, 120))
        self.screen.blit(name_text, (200, 120))
        self.screen.blit(score_text, (350, 120))
        self.screen.blit(level_text, (450, 120))
        
        # Display scores
        y_pos = 170
        for i, score in enumerate(high_scores):
            rank = self.font.render(f"{i+1}.", True, self.WHITE)
            name = self.font.render(score['username'], True, self.GREEN)
            score_val = self.font.render(str(score['score']), True, self.YELLOW)
            level = self.font.render(str(score['level']), True, self.WHITE)
            
            self.screen.blit(rank, (100, y_pos))
            self.screen.blit(name, (200, y_pos))
            self.screen.blit(score_val, (350, y_pos))
            self.screen.blit(level, (450, y_pos))
            
            y_pos += 40
        
        # Instructions
        if not high_scores:
            no_scores = self.font.render("No high scores yet!", True, self.GRAY)
            self.screen.blit(no_scores, (self.WIDTH // 2 - no_scores.get_width() // 2, 200))
        
        instructions = self.small_font.render("Press ESC or M to return to Main Menu", True, self.GRAY)
        self.screen.blit(instructions, (self.WIDTH // 2 - instructions.get_width() // 2, 500))
        
        pygame.display.flip()
    
    def draw_game_screen(self):
        """Draw the main game screen"""
        self.screen.fill(self.BLACK)
        
        # Draw walls
        for wall in self.walls:
            rect = pygame.Rect(wall[0] * self.GRID_SIZE, wall[1] * self.GRID_SIZE, 
                             self.GRID_SIZE, self.GRID_SIZE)
            pygame.draw.rect(self.screen, self.wall_color, rect)
        
        # Draw snake (head different color)
        for i, segment in enumerate(self.snake):
            rect = pygame.Rect(segment[0] * self.GRID_SIZE, segment[1] * self.GRID_SIZE, 
                             self.GRID_SIZE, self.GRID_SIZE)
            if i == 0:  # Head
                pygame.draw.rect(self.screen, (0, 200, 0), rect)  # Darker green
            else:  # Body
                pygame.draw.rect(self.screen, self.GREEN, rect)
        
        # Draw food
        food_rect = pygame.Rect(self.food[0] * self.GRID_SIZE, self.food[1] * self.GRID_SIZE, 
                              self.GRID_SIZE, self.GRID_SIZE)
        pygame.draw.rect(self.screen, self.RED, food_rect)
        
        # Draw score and level info
        score_text = self.font.render(f"Score: {self.score}", True, self.WHITE)
        level_text = self.font.render(f"Level: {self.current_level}", True, self.WHITE)
        user_text = self.font.render(f"User: {self.current_user['username']}", True, self.WHITE)
        speed_text = self.small_font.render(f"Speed: {self.game_speed}", True, self.WHITE)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 50))
        self.screen.blit(user_text, (10, 90))
        self.screen.blit(speed_text, (10, 130))
        
        # Draw controls info
        controls_text = self.small_font.render("P: Save | ESC: Pause | M: Menu", True, self.GRAY)
        self.screen.blit(controls_text, (self.WIDTH - controls_text.get_width() - 10, 10))
        
        # Draw pause message
        if self.paused:
            pause_text = self.font.render("Game Paused", True, self.YELLOW)
            continue_text = self.font.render("Press ESC to continue", True, self.WHITE)
            
            self.screen.blit(pause_text, (self.WIDTH // 2 - pause_text.get_width() // 2, self.HEIGHT // 2 - 20))
            self.screen.blit(continue_text, (self.WIDTH // 2 - continue_text.get_width() // 2, self.HEIGHT // 2 + 20))
        
        pygame.display.flip()
    
    def draw_game_over(self):
        """Draw game over screen"""
        self.screen.fill(self.BLACK)
        
        game_over_text = self.title_font.render("GAME OVER", True, self.RED)
        final_score_text = self.font.render(f"Final Score: {self.score}", True, self.YELLOW)
        level_text = self.font.render(f"Level Reached: {self.current_level}", True, self.WHITE)
        
        restart_text = self.font.render("Press R to Play Again", True, self.GREEN)
        menu_text = self.font.render("Press M for Main Menu", True, self.WHITE)
        scores_text = self.font.render("Press H for High Scores", True, self.BLUE)
        
        self.screen.blit(game_over_text, (self.WIDTH // 2 - game_over_text.get_width() // 2, 100))
        self.screen.blit(final_score_text, (self.WIDTH // 2 - final_score_text.get_width() // 2, 180))
        self.screen.blit(level_text, (self.WIDTH // 2 - level_text.get_width() // 2, 220))
        self.screen.blit(restart_text, (self.WIDTH // 2 - restart_text.get_width() // 2, 300))
        self.screen.blit(menu_text, (self.WIDTH // 2 - menu_text.get_width() // 2, 350))
        self.screen.blit(scores_text, (self.WIDTH // 2 - scores_text.get_width() // 2, 400))
        
        pygame.display.flip()
    
    def draw(self):
        """Draw appropriate screen based on game state"""
        if self.current_state == self.MAIN_MENU:
            self.draw_main_menu()
        elif self.current_state == self.HIGH_SCORES:
            self.draw_high_scores()
        elif self.current_state == self.PLAYING:
            self.draw_game_screen()
        elif self.current_state == self.GAME_OVER:
            self.draw_game_over()
    
    def get_username(self):
        """Get username from user input"""
        username = ""
        input_active = True
        
        while input_active:
            self.screen.fill(self.BLACK)
            
            title_text = self.font.render("Snake Game - PostgreSQL", True, self.YELLOW)
            prompt_text = self.font.render("Enter your username:", True, self.WHITE)
            input_text = self.font.render(username, True, self.GREEN)
            instruction_text = self.small_font.render("Press ENTER to continue, ESC to exit", True, self.GRAY)
            
            self.screen.blit(title_text, (self.WIDTH // 2 - title_text.get_width() // 2, 100))
            self.screen.blit(prompt_text, (self.WIDTH // 2 - 100, self.HEIGHT // 2 - 50))
            self.screen.blit(input_text, (self.WIDTH // 2 - 50, self.HEIGHT // 2))
            self.screen.blit(instruction_text, (self.WIDTH // 2 - 150, self.HEIGHT // 2 + 50))
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and username:
                        input_active = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        if event.unicode.isalnum() and len(username) < 20:
                            username += event.unicode
        
        return username
    
    def load_saved_game(self, user_id):
        """Load saved game for user"""
        saved_game = self.db.get_saved_game(user_id)
        if saved_game:
            self.current_level = saved_game['level']
            self.score = saved_game['score']
            self.snake = json.loads(saved_game['snake_body'])
            self.food = json.loads(saved_game['food_position'])
            self.direction = saved_game['direction']
            self.game_speed = saved_game['game_speed']
            
            level_config = self.levels[self.current_level]
            self.walls = level_config["walls"]
            self.wall_color = level_config["color"]
            
            return True
        return False
    
    def show_level_info(self, level):
        """Show level information"""
        level_config = self.levels[level]
        self.screen.fill(self.BLACK)
        
        level_text = self.font.render(f"Level {level}: {level_config['name']}", True, level_config["color"])
        speed_text = self.font.render(f"Speed: {level_config['speed']}", True, self.WHITE)
        walls_text = self.font.render(f"Walls: {len(level_config['walls'])}", True, self.WHITE)
        start_text = self.font.render("Press SPACE to start", True, self.GREEN)
        warning_text = self.small_font.render("Watch out for walls!", True, self.YELLOW)
        
        self.screen.blit(level_text, (self.WIDTH // 2 - level_text.get_width() // 2, self.HEIGHT // 2 - 80))
        self.screen.blit(speed_text, (self.WIDTH // 2 - speed_text.get_width() // 2, self.HEIGHT // 2 - 30))
        self.screen.blit(walls_text, (self.WIDTH // 2 - walls_text.get_width() // 2, self.HEIGHT // 2 + 10))
        self.screen.blit(warning_text, (self.WIDTH // 2 - warning_text.get_width() // 2, self.HEIGHT // 2 + 50))
        self.screen.blit(start_text, (self.WIDTH // 2 - start_text.get_width() // 2, self.HEIGHT // 2 + 100))
        
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False
    
    def run(self):
        """Main game loop"""
        # Get username
        username = self.get_username()
        
        # Check if user exists
        user = self.db.get_user(username)
        if user:
            self.current_user = user
            print(f"Welcome back, {username}!")
            
            # Check for saved game
            saved_game = self.db.get_saved_game(user['id'])
            if saved_game:
                self.show_message("Saved game found! Press L to load or any other key to start new game", self.YELLOW)
                
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_l:
                                if self.load_saved_game(user['id']):
                                    self.show_message("Game loaded successfully!", self.GREEN)
                                    self.current_state = self.PLAYING
                                else:
                                    self.show_message("Error loading game!", self.RED)
                                    self.current_level = 1
                            else:
                                self.current_level = 1
                            waiting = False
            else:
                self.current_level = 1
        else:
            # Create new user
            user_id = self.db.create_user(username)
            if user_id:
                user = self.db.get_user(username)
                self.current_user = user
                self.current_level = 1
                print(f"New user {username} created! Starting at level 1")
            else:
                self.show_message("Error creating user! Exiting...", self.RED)
                time.sleep(2)
                return
        
        # Main game loop
        while True:
            self.handle_events()
            
            if self.current_state == self.PLAYING and not self.paused and not self.game_over:
                self.move_snake()
            
            self.draw()
            self.clock.tick(1000 // self.game_speed if self.current_state == self.PLAYING else 60)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
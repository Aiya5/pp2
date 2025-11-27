import psycopg2
import json

def get_connection():
    # CHANGE THE PASSWORD to your actual PostgreSQL password
    # Common passwords: 'postgres', '12345', '123456', 'password'
    return psycopg2.connect(
        host='localhost',
        database='phonebook',
        user='postgres',
        password='postgres',  # ⚠️ CHANGE THIS TO YOUR PASSWORD
        port='5432'
    )

def create_snake_tables():
    try:
        conn = get_connection()
        cur = conn.cursor()
        
        # Users table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS snake_users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # User scores table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS user_scores (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES snake_users(id),
                level INTEGER DEFAULT 1,
                score INTEGER DEFAULT 0,
                speed INTEGER DEFAULT 15,
                saved_state TEXT,
                saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        cur.close()
        conn.close()
        print("Snake game tables created successfully!")
        return True
    except Exception as e:
        print(f"Error creating tables: {e}")
        return False

def get_user_level(username):
    """Get user's current level and game state"""
    try:
        conn = get_connection()
        cur = conn.cursor()
        
        cur.execute("""
            SELECT us.level, us.score, us.speed 
            FROM user_scores us 
            JOIN snake_users u ON u.id = us.user_id 
            WHERE u.username = %s 
            ORDER BY us.saved_at DESC 
            LIMIT 1
        """, (username,))
        
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        print(f"Error getting user level: {e}")
        return None

def save_game_state(username, level, score, speed, game_state):
    """Save game state to database"""
    try:
        conn = get_connection()
        cur = conn.cursor()
        
        # Get or create user
        cur.execute("""
            INSERT INTO snake_users (username) 
            VALUES (%s) 
            ON CONFLICT (username) DO NOTHING
        """, (username,))
        
        cur.execute("SELECT id FROM snake_users WHERE username = %s", (username,))
        user_result = cur.fetchone()
        
        if user_result:
            user_id = user_result[0]
        else:
            print("Error: Could not get user ID")
            return
        
        # Save game state
        cur.execute("""
            INSERT INTO user_scores (user_id, level, score, speed, saved_state)
            VALUES (%s, %s, %s, %s, %s)
        """, (user_id, level, score, speed, game_state))
        
        conn.commit()
        cur.close()
        conn.close()
        print("Game saved successfully!")
        return True
    except Exception as e:
        print(f"Error saving game: {e}")
        return False
import psycopg2

def connect_db():
    conn = psycopg2.connect(
        host='localhost',
        database='phonebook',
        user='postgres',
        password='postgres',  # CHANGE TO YOUR PASSWORD
        port='5432'
    )
    return conn

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50),
            phone VARCHAR(20) UNIQUE NOT NULL,
            email VARCHAR(100)
        )
    """)
    
    conn.commit()
    cur.close()
    conn.close()
    print("Table created successfully!")
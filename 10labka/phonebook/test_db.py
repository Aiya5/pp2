import psycopg2

try:
    # Try to connect with your password
    conn = psycopg2.connect(
        host='localhost',
        database='postgres',  # Try connecting to default database first
        user='postgres',
        password='postgres',    # CHANGE THIS
        port='5432'
    )
    print("✅ Connected to PostgreSQL successfully!")
    
    # Create our database if it doesn't exist
    conn.autocommit = True
    cur = conn.cursor()
    
    try:
        cur.execute("CREATE DATABASE phonebook")
        print("✅ Database 'phonebook' created successfully!")
    except:
        print("ℹ️ Database 'phonebook' already exists")
    
    cur.close()
    conn.close()
    
except Exception as e:
    print(f"❌ Connection failed: {e}")
    print("\nTroubleshooting tips:")
    print("1. Is PostgreSQL running?")
    print("2. Is your password correct?")
    print("3. Try the default password 'postgres'")
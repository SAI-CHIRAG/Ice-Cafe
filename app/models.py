import sqlite3

def create_tables():
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    
    c.execute('''
    CREATE TABLE IF NOT EXISTS flavors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        season TEXT NOT NULL
    )
    ''')
    
    c.execute('''
    CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY,
        item TEXT NOT NULL
    )
    ''')
    
    c.execute('''
    CREATE TABLE IF NOT EXISTS suggestions (
        id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL,
        suggestion TEXT NOT NULL
    )
    ''')
    
    c.execute('''
    CREATE TABLE IF NOT EXISTS allergens (
        id INTEGER PRIMARY KEY,
        allergen TEXT NOT NULL UNIQUE
    )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()

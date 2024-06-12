import sqlite3

def connect_db():
    return sqlite3.connect('ice_cream_parlor.db')

def add_flavor(name, season):
    conn = connect_db()
    c = conn.cursor()
    c.execute('INSERT INTO flavors (name, season) VALUES (?, ?)', (name, season))
    conn.commit()
    conn.close()

def get_flavors():
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM flavors')
    flavors = c.fetchall()
    conn.close()
    return flavors

def add_allergen(allergen):
    conn = connect_db()
    c = conn.cursor()
    c.execute('INSERT INTO allergens (allergen) VALUES (?)', (allergen,))
    conn.commit()
    conn.close()

def get_all_allergens():
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM allergens')
    allergens = c.fetchall()
    conn.close()
    return allergens

def add_item_cart(item):
    conn = connect_db()
    c = conn.cursor()
    c.execute('INSERT INTO cart (item) VALUES (?)',(item,))
    conn.commit()
    conn.close()

def display_all_items():
    conn = connect_db()
    c =conn.cursor()
    c.execute('SELECT * FROM cart')
    items = c.fetchall()
    conn.close()
    return items

def remove_item(item):
    conn = connect_db()
    c = conn.cursor()
    c.execute('DELETE FROM cart WHERE item = ?', (item,))
    conn.commit()
    conn.close()

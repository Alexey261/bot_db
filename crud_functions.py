import sqlite3

# connection = sqlite3.connect('telegram.db')
# cursor = connection.cursor()


def initiate_db():
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    photo TEXT NOT NULL
    )
    ''')

    cursor.execute('SELECT COUNT(*) FROM Products')
    if not cursor.fetchone()[0]:
        for i in range(1, 5):
            cursor.execute('INSERT INTO Products (title, description, price, photo) VALUES(?,?,?,?)',
                           (f'Продукт {i}', f'Описание {i}', f'{100 * i}', f'{i}.png'))

    connection.commit()
    connection.close()

def get_all_products():
    initiate_db()

    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()

    cursor.execute("SELECT title, description, price, photo FROM Products")
    records = cursor.fetchall()

    connection.commit()
    connection.close()

    return records




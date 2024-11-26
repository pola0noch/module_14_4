import sqlite3

def initiate_db():
    connect = sqlite3.connect('products.db')
    cursor = connect.cursor()
    try:
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS Products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    price INTEGER NOT NULL
                )
            """)
        connect.commit()
        print("Таблица Products успешно создана или уже существует.")
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблицы: {e}")
    finally:
        connect.close()

initiate_db()

'''def insert_products():
    connect = sqlite3.connect('products.db')
    cursor = connect.cursor()
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                           (f"Продукт {i}", f"Описание {i}", i*100))
    
    connect.commit()
    connect.close()'''
def get_all_products():
    connect = sqlite3.connect('products.db')
    cursor = connect.cursor()
    try:
        cursor.execute("SELECT * FROM Products")
        products = cursor.fetchall()
        return products
    except sqlite3.Error as e:
        print(f"Ошибка при получении данных: {e}")
        return None
    finally:
        connect.close()


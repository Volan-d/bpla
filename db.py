import sqlite3

# подключаемся в БД, если такой нет, то она создается
con = sqlite3.connect('database.sqlite3')

# создание БД в оперативной памяти (ОЗУ) - только для тестов!
# con = sqlite3.connect(":memory:")

# создаем объект курсора
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS ultrasonics(
id INTEGER PRIMARY KEY AUTOINCREMENT,
sensor_name TEXT,
value REAL
);
""")
# выполняем запрос
con.commit()

# Вставка данных в таблицу ultrasonics
# cur.execute("""INSERT INTO ultrasonics(sensor_name, value)
#     VALUES ('forward_sensor', 100);
# """)

# добавление одной записи (placeholder)
data_ultrasonic = (None, 'back_sensor', 250)
cur.execute("INSERT INTO ultrasonics VALUES (?, ?, ?)", data_ultrasonic)
# выполняем запрос
con.commit()

# добавление множества записей (placeholder)
data_ultrasonic_many = [(None, 'back_sensor', 150), (None, 'back_sensor', 750), (None, 'forward_sensor', 30)]
cur.executemany("INSERT INTO ultrasonics VALUES (?, ?, ?)", data_ultrasonic_many)
con.commit()

# выборка данных
cur.execute("SELECT sensor_name, value FROM ultrasonics WHERE sensor_name == 'back_sensor'")
result = cur.fetchall()
print(result)

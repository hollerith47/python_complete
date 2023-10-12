import sqlite3

connection = sqlite3.connect("lab11_data.db")
cursor = connection.cursor()
cursor.execute(" PRAGMA FOREIGN_KEYS = ON ")
cursor.execute("""CREATE TABLE IF NOT EXISTS Преподаватель(
id INTEGER ,
ФИО TEXT,
ID_Дисциплины INTEGER PRIMARY KEY
)""")
connection.commit()
cursor.execute("""CREATE TABLE IF NOT EXISTS Дисциплина(
id INTEGER PRIMARY KEY,
Название TEXT,
КоличествоЛекций INTEGER,
КоличествоПрактик INTEGER,
Курсовая TEXT,
"Самостоят.раб." INTEGER,
FOREIGN KEY (id) REFERENCES Преподаватель(ID_Дисциплины) ON UPDATE CASCADE ON DELETE CASCADE
)""")
connection.commit()

teachers = [(6, 'Натан Демидович Афанасьев', 301), (1, 'Брагин Ипатий Архипович', 302), (7, 'Туров Прокофий '
																							'Ерофеевич', 303),
			(10, 'Савин Эрнст Харламович', 304), (9, 'Соловьев Мечислав Харлампович', 305),
			(5, 'Станислав Евсеевич Белов', 306), (6, 'Жанна Робертовна Никонова', 307),
			(5, 'Мухин Никон Давыдович', 308), (8, 'Копылов Мир Анисимович', 309), (3, 'Воронцова Анна Ильинична', 310)
			]
# cursor.executemany('INSERT INTO Преподаватель(id, ФИО, ID_Дисциплины) VALUES (?,?,?)', teachers)
connection.commit()

Courses = [(308, 'Основы программирования', 90, 66, 'Да', 8), (301, 'Права человека', 57, 63, 'Нет', 4),
		   (307, 'Дискретная математика', 49, 16, 'Да', 11), (306, 'Философия', 45, 94, 'Да', 14),
		   (303, 'Теория вероятности, математическая статистика', 49, 29, 'Нет', 5),
		   (304, 'Основы программирования', 79, 76, 'Нет', 12), (310, 'Дискретная математика', 30, 53, 'Нет', 1),
		   (309, 'Теория вероятности, математическая статистика', 77, 62, 'Да', 6), (302, 'Философия', 32, 40, 'Нет',
																					 6),
		   (305, 'Права человека', 69, 75, 'Да', 11)
		   ]
# cursor.executemany('INSERT INTO Дисциплина(id, Название, КоличествоЛекций, КоличествоПрактик, Курсовая, "Самостоят.раб.") VALUES (?,'
# 				   '?,?, ?, ?, ?)',
# 				   Courses)
connection.commit()
# cursor.execute()


connection.close()
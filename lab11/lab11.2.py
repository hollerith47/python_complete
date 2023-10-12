import sqlite3

connection = sqlite3.connect("lab11_data.db")
cursor = connection.cursor()
cursor.execute("PRAGMA FOREIGN_KEYS = ON")
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
# connection.commit()
MENU =""""Что вы хотите?
1: Удалить
2: Добавить
3: Изменить
4: Выйти
👉 Ваш выбор : """

MENU_del ="""Что конкретно надо изменить
	1: id
	2: ФИО
	3: ID_Дисциплины
	👉 Ваш выбор : """

user_vibor = ''
# MENU_CHOICES = ['1', '2', '3', "4"]
turn_off ="4"
while user_vibor != turn_off:
	user_vibor = input(MENU)
	# удаление
	if user_vibor == "1":
		udalite_prep = int(input("Введите id Преподавателя, которое необходимо удалить: "))
		cursor.executemany('DELETE FROM Преподаватель WHERE id=udalite_prep')
		connection.commit()
	# добавление
	elif user_vibor == "2":
		dabavit_prep = [( int(input("id Преподавателя :")), input("ФИО Преподавателя: "), int(input("ID_Дисциплины: "
																									"")))]
		cursor.executemany('INSERT INTO Преподаватель(id, ФИО, ID_Дисциплины) VALUES (?,?,?)', dabavit_prep)
		dabavit_course = [int(input("id_Дисциплины: ")), input('Название Дисциплины: '), int(input('КоличествоЛекций: ')), int(input('КоличествоПрактик: ')), input('Курсовая: '),
						  int(input('Самостоят.раб.: '))]
		cursor.executemany('INSERT INTO Дисциплина(id, Название, КоличествоЛекций, КоличествоПрактик, Курсовая, '
						   '"Самостоят.раб.") VALUES (?, ?,?, ?, ?, ?)', dabavit_course)
		connection.commit()
	# изменение
	elif user_vibor == "3" :
		user_vibor_1 = input(MENU_del)
		if user_vibor_1 =="1":
			stari_id = int(input("Введите старый id Преподавателя: "))
			id_new = int(input("Введите новый id Преподавателя: "))
			choisss= {"novo": id_new,"stari": stari_id}
			cursor.executemany('''UPDATE Преподаватель SET id =:novo WHERE id=:stari_id AND ФИО=:ФИО''', choisss)
			connection.commit()
		elif user_vibor_1 =="2":
			stari_fio = input("Введите старое ФИО Преподавателя: ")
			new_fio = input("Введите новое ФИО Преподавателя: ")
			choisss_1 ={'novo': new_fio , "stari": stari_fio}
			cursor.execute('UPDATE Преподаватель SET ФИО =:novo WHERE id=:id AND ФИО=:stari', choisss_1)
			connection.commit()
		elif user_vibor_1 =="3":
			stari_disp_id = (input("Введите старый ID_Дисциплины: "))
			new_disp_id = (input("Введите новый ID_Дисциплины: "))
			choisss_2 = {"novo":new_disp_id, "stari":stari_disp_id}
			cursor.executemany('''UPDATE Преподаватель SET ID_Дисциплины =:novo WHERE ФИО=:ФИО AND
			ID_Дисциплины=:stari ''', choisss_2)
			connection.commit()
			
cursor.execute("SELECT * FROM Преподаватель")
prepadavatel = cursor.fetchall()
print(prepadavatel)
		
cursor.execute("SELECT * FROM Дисциплина")
disciplina = cursor.fetchall()
print(disciplina)

connection.close()
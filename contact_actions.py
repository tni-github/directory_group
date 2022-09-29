import csv

def add_contact():
    '''
    Добавление контакта 
    '''
    with open("classmates.csv", encoding='utf-8') as data:
        # Создаем объект DictReader, указываем символ-разделитель ","
        file_reader = csv.DictReader(data, delimiter = ",")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'Файл содержит столбцы: {", ".join(row)}')
            # Вывод строк
            print(f' {row["Имя"]} - {row["Успеваемость"]}', end='')
            print(f' и он родился в {row["Год рождения"]} году.')
            count += 1
        print(f'Всего в файле {count + 1} строк.')



<<<<<<< HEAD
# Чтение из файла (Открыть контакт) ? как открыть выборочно?
def reading_contact():
    '''
    чтение из файла
    '''
    with open('contacts.csv', newline = '', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            print(row['id'], row['Фамилия'], row['Имя'], row['Отчество'], row['Тип_телефона'], row['Номер_телефона'], row['Комментарий'])
=======
# # Чтение из файла (Открыть контакт) ? как открыть выборочно?
# def reading_contact():
#     with open('contacts.csv', newline = '', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile, delimiter=',')
#         for row in reader:
#             print(row['id'], row['Фамилия'], row['Имя'], row['Отчество'], row['Тип_телефона'], row['Номер_телефона'], row['Комментарий'])
=======

>>>>>>> e17b9ca35e10253cc8e6d2c3c06a93fb57f9a514

        
# Запись в файл (Добавить контакт) ? Добавить id контакта и пустые вводы
def add_contact():
    '''
    запись в файл
    '''
    with open('contacts.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['id', 'Фамилия', 'Имя', 'Отчество', 'Тип_телефона', 'Номер_телефона', 'Комментарий'])



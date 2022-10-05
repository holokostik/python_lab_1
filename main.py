import csv
from collections import Counter

counter = -1  # счётчик записей
long_name_counter = 0  # счётчик записей с названиями больше 30 символов
search_counter = 0  # счётчик записей для функции поиска
search_results = []  # массив, в который добавляются найденные записи
refs = []  # массив, в который добавляются библиографические ссылки
tags = []  # массив, в который добавляются теги для допзадания
row_tags = []  # массив с тегами текущей строки(до проверки на повторы и занесения в общий массив)
names = []  # массив с названиями книг для допзадания

print("\t\tПоиск книги по автору")
author_name = input("Введите имя автора: ")

with open("books.csv", "r", encoding='windows-1251') as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:

        row_text = []  # массив с содержанием текущий строки, разбитой по разделителям
        for i in row:
            row_text.append(i)

        date = row_text[6]  # дата записи, нужна для создания библиографической ссылки и тегов в допзадании

        if len(row_text[1]) > 30:  # считаем длинные названия
            long_name_counter += 1

        if author_name == row_text[3] and date[6:10] in ['2015', '2018']:  # 8 вариант допзадания
            search_results.append(row_text[1])
            search_counter += 1

        if 0 <= counter < 20:  # создаём ссылки
            refs.append(f"{counter + 1}: {row_text[3]}. {row_text[1]} - {date[6:10]}\n")

        row_tags = (row_text[12])[1:].split('# ')  # смотрим теги и записываем
        for i in row_tags:
            if i not in tags:
                tags.append(i)
        names.append(row_text[1])

        counter += 1  # считаем общее кол-во записей

with open("refs.txt", "w") as refs_file:  # записываем ссылки в отдельный файл
    refs_file.write("\n".join(refs))

with open("tags.txt", "w") as tags_file:  # записываем теги в отдельный файл
    tags_file.writelines(f"# {tag}\n" for tag in tags)

with open("top_20.txt", "w") as top_file:  # записываем самые популярные книги в отдельный файл
    top = Counter(names).most_common(20)
    for i in range(20):
        top_file.write(f"{i+1}: {top[i][0]}\n")

if search_counter == 0:
    print("Не было найдено ни одной книги 2015/2018 годов с данным автором")
else:
    print(f"Было найдено {search_counter} Записей:")
    print("\n".join(search_results))

print(f"Количество записей: {counter}\n"
      f"Количество записей с названием больше 30 символов: {long_name_counter}")

import csv

with open("books.csv", "r", encoding='windows-1251') as file:
    reader = csv.reader(file, delimiter=";")
    counter = -1  # счётчик записей
    long_name_counter = 0  # счётчик записей с названиями больше 30 символов
    search_counter = 0  # счётчик записей для функции поиска
    search_results = []  # массив, в который добавляются найденные записи
    refs = []  # массив, в который добавляются библиографические ссылки
    tags = []  # массив, в который добавляются теги для допзадания
    row_tags = []  # массив с тегами текущей строки(до проверки на повторы и занесения в общий массив)
    print("\t\tПоиск книги по автору")
    author_name = input("Введите имя автора: ")
    for row in reader:
        row_text = []  # массив с содержанием текущий строки, разбитой по разделителям
        for i in row:
            row_text.append(i)
        date = row_text[6]  # дата записи, нужна для создания библиографической ссылки и тегов в допзадании
        if len(row_text[1]) > 30:
            long_name_counter += 1
        if author_name == row_text[3]:
            search_results.append(row_text[1])
            search_counter += 1
        if 0 <= counter < 20:
            refs.append(f"{counter + 1}: {row_text[3]}. {row_text[1]} - {date[6:10]}\n")
        if date[6:10] in ['2015', '2018']:  # 8 вариант допзадания
            row_tags = (row_text[12])[1:].split('# ')
            for i in row_tags:
                if i not in tags:
                    tags.append(i)
        counter += 1
    with open("refs.txt", "w") as refs_file:
        refs_file.write("\n".join(refs))
with open("tags.txt", "w") as tags_file:
    tags_file.writelines(f"# {tag}\n" for tag in tags)
if search_counter == 0:
    print("Не было найдено ни одной книги с данным автором")
else:
    print(f"Было найдено {search_counter} Записей:")
    print("\n".join(search_results))
print(f"Количество записей: {counter}\n"
      f"Количество записей с названием больше 30 символов: {long_name_counter}")

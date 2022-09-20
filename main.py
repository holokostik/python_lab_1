import csv
with open("books.csv") as f:
    reader = csv.reader(f, delimiter=";")
    count = 0
    long_name = 0
    search_count = 0
    search_results = []
    print("\t\tПоиск книги по автору")
    author_name = input("Введите имя автора: ")
    for row in reader:
        a = []
        for i in row:
            a.append(i)
        if len(a[1]) > 30:
            long_name += 1
        if author_name in a[3]:
            search_results.append(a[1])
            search_count += 1
        count += 1
if search_count == 0:
    print("Не было найдено ни одной книги с данным автором")
else:
    print(f"Было найдено {search_count} Записей:")
    print(f"\n".join(search_results))
print(f"Количество записей: {count}\n"
      f"Количество записей с названием больше 30 символов: {long_name}")

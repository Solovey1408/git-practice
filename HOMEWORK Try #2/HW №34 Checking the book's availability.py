def check_book_in_library(title, my_library):
    return title in my_library


def book_list_view(my_library):
    if not my_library:
        print("В библиотеке нет книг.")

    else:
        print(f"Список книг в библиотеке:")
        for key in my_library:
            print(f"{key}")


def add_book_to_library(title, author, year, my_library):
    my_library[title] = {
        "Author": author,
        "Year": year,
        "Availability": None
    }


def add_book(title, author, year, my_library):

    if check_book_in_library(title, my_library):
        update_question = input("Такая книга уже есть.Обновить информацию о данной книге?").lower()

        if update_question == "да":
            add_book_to_library(title, author, year, my_library)
            print(f"Информация книги '{title}' обновлена.")

        else:
            print(f"Информация книги '{title}' не обновлена.")

    else:
        add_book_to_library(title, author, year, my_library)
        print(f"Книга '{title}' добавлена.")


# Удаление методом del
def remove_book(title, my_library):

    if not check_book_in_library(title, my_library):
        print(f"Книга '{title}' отсутствует в библиотеке.")
    else:
        del my_library[title]
        print(f"Книга '{title}' удалена.")


def issue_book(title, my_library):
    if not check_book_in_library(title, my_library):
        print(f"Книга '{title}' отсутствует в библиотеке.")

    elif my_library[title]["Availability"] is False: #или если статус книги "выдана"
        print(f"Книга '{title}' уже выдана.")

    else: #в противном случае статус книги остается "выдана"
        my_library[title]["Availability"] = False
        print(f"Книга {title} выдана")


def return_book(title, my_library):
    if not check_book_in_library(title, my_library):
        print(f"Книга '{title}' отсутствует в библиотеке.")

    if my_library[title]["Availability"] is True:
        print(f"Книга '{title}' уже находится в библиотеке.")

    else:
        my_library[title]["Availability"] = True
        print(f"Книга '{title}' возвращена в библиотеку.")


def find_book(title, my_library):
    if not check_book_in_library(title, my_library):
        print(f"Книги '{title}' нет в библиотеке.")

    else:
        book = my_library[title]
        status_book = {
        True: "Книга доступна",
        False: "Книга выдана",
        None: "Книга в библиотеке, но ее статус не определен"
        }

        availability = status_book[book["Availability"]]

        book_info = (
        f"Информация о книге '{title}':\n"
        f"Автор: {book['Author']}\n"
        f"Год издания: {book['Year']}\n"
        f"Статус: {availability}")

        print(book_info)


my_library = {
    "Call of Cthulhu": {
        "Author": "Howard Lovecraft",
        "Year": 1928,
        "Availability": False
    },
    "Idiot": {
        "Author": "Fedor Dostoevsky",
        "Year": 1869,
        "Availability": True
    },
    "The Beach": {
        "Author": "Alex Garland",
        "Year": 1996,
        "Availability": False
    },
    "The Blade Artist": {
        "Author": "Irvine Welsh",
        "Year": 2016,
        "Availability": True
    }
}

menu = ('''Главное меню библиотеки
1.Просмотреть список книг
2.Добавить книгу
3.Удалить книгу
4.Выдать книгу
5.Вернуть книгу
6.Найти книгу
7.Выйти из библиотеки''')

print(menu)

correct_options = '1234567'

choice_options = input("Выберите номер опции из меню: ")

while choice_options not in correct_options:
    print("Неверный номер. Пожалуйста, выберите правильный номер.")
    choice_options = input("Выберите номер опции из меню: ")

if choice_options == '1':
    book_list_view(my_library)

elif choice_options == '2':
    title = str(input("Введите название книги: ")).lower()
    author = str(input("Введите автора книги: ")).lower()
    year = int(input("Введите год выпуска книги: "))
    add_book(title, author, year, my_library)

elif choice_options == '3':
    title = str(input("Введите название книги: ")).lower()
    remove_book(title, my_library)

elif choice_options == '4':
    title = str(input("Введите название книги: ")).lower()
    issue_book(title, my_library)

elif choice_options == '5':
    title = str(input("Введите название книги: ")).lower()
    return_book(title, my_library)

elif choice_options == '6':
    title = str(input("Введите название книги: ")).lower()
    find_book(title, my_library)

elif choice_options == '7':
    print("Закрываем библиотеку.")



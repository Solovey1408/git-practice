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


# Реализуйте функцию `find_book(title)`, которая выводит информацию о книге по ее названию.
# Если книга не найдена, должно выводиться соответствующее сообщение.
def find_book(title, my_library):
    if not check_book_in_library(title, my_library):
        print(f"Книги '{title}' нет в библиотеке.")

    else:
        book = my_library[title]
        availability = True if book ["Availability"] else False
        print(f"Книга '{title}' есть в библиотеке")

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

book_list_view(my_library)

add_book("Alice’s Adventures in Wonderland", "Lewis Carroll", 1865, my_library)

find_book("Alice’s Adventures in Wonderland", my_library)

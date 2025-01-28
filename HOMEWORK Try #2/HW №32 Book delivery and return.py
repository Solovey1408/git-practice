# Создайте словарь library, где ключами будут названия книг, а значениями — словари с информацией
# о книге (автор, год издания, наличие).
# После этого реализуйте первую функцию 'book_list_view(library)',
# которая выводит в консоль названия всех книг в библиотеке. Если в библиотеке нет книг,
# функция выводит сообщение об этом.


def book_list_view(my_library):

    for key in my_library:
        print(f"{key}")

    if not my_library:
        print("В библиотеке нет книг.")


# Продолжаем работать над созданием библиотеки:
# Реализуйте функцию `add_book(title, author, year)`, которая добавляет книгу в словарь `library`.
# Поле `наличие` при добавлении новой книги должно быть `None`
# (означает, что книга в библиотеке, но не определен ее статус).
# Если книга с таким названием уже существует, программа должна предложить обновить информацию о ней.
# Функция должна вывести сообщение об успешном добавлении/обновлении информации о книге с ее названием


def add_book_to_library(title, author, year):
    my_library[title] = {
        "Author": author,
        "Year": year,
        "Availability": None  # При добавлении новой книги статус наличия None
    }


def add_book(title, author, year):

    if title in my_library:
        update_question = input("Такая книга уже есть.Обновить информацию о данной книге?").lower()

        if update_question == "да":
            add_book_to_library(title, author, year)
            print(f"Информация книги '{title}' обновлена.")

        else:
            print(f"Информация книги '{title}' не обновлена.")

    else:
        add_book_to_library(title, author, year)
        print(f"Книга '{title}' добавлена.")


# Реализуйте функцию `remove_book(title)`, которая удаляет книгу из словаря.
# Если книга не найдена, программа должна вывести сообщение об этом.

# Удаление методом del
def remove_book(title):

    if title not in my_library:
        print(f"Книга '{title}' отсутствует в библиотеке.")

    else:
        del my_library[title]
        print(f"Книга '{title}' удалена.")


# #Удаление методом pop
# def remove_book(title):
#     if title not in my_library:
#         print(f"Книга '{title}' отсутствует в библиотеке.")
#     else:
#         delete_library = my_library.pop(title)
#         print(f"Книга '{title}' удалена.")


# Реализуйте функцию issue_book(title), которая отмечает книгу как выданную (`наличие` становится `False`).
# Реализуйте функцию return_book(title), которая отмечает книгу как вернувшуюся в библиотеку (`наличие` становится `True`).


def issue_book(title):

    if my_library[title]["Availability"] is False: #или если статус книги "выдана"
        print(f"Книга '{title}' уже выдана.")

    else: #в противном случае статус книги остается "выдана"
        my_library[title]["Availability"] = False
        print(f"Книга {title} выдана")


def return_book(title):

    if title not in my_library:
        print(f"Книга '{title}' отсутствует в библиотеке.")

    elif my_library[title]["Availability"] is True:
        print(f"Книга '{title}' уже находится в библиотеке.")

    else:
        my_library[title]["Availability"] = True
        print(f"Книга '{title}' возвращена в библиотеку.")


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


book_view = book_list_view(my_library)

add_book("The Beach", "Alex Garland", 1995)
add_book("Alice’s Adventures in Wonderland", "Lewis Carroll", 1865)

remove_book("The Beach")
remove_book("The Beach")

issue_book("Idiot")
return_book("The Beach")

print(my_library)
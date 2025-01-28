def is_book_in_library(title):
    if title not in my_library:
        print(f"Книга '{title}' отсутствует в библиотеке.")


def book_list_view(my_library):

    if not my_library:
        print("В библиотеке нет книг.")
    else:
        for key in my_library:
            print(f"{key}")


def add_book_to_library(title, author, year):
    my_library[title] = {
        "Author": author,
        "Year": year,
        "Availability": None
    }


def add_book(title, author, year):

    if title in my_library:
        update_question = input("Такая книга уже есть.Обновить информацию о данной книге?").lower()

        if update_question == "да":
            add_book_to_library(title, author, year)
            print(f"Информация книги '{title}' обновлена.")

        else:
            is_book_in_library(title)

    else:
        add_book_to_library(title, author, year)
        print(f"Книга '{title}' добавлена.")


# Удаление методом del
def remove_book(title):

    if is_book_in_library(title):
        print(f"Книга '{title}' отсутствует в библиотеке.")
    else:
        del my_library[title]
        print(f"Книга '{title}' удалена.")


def issue_book(title):

    if my_library[title]["Availability"] is False: #или если статус книги "выдана"
        print(f"Книга '{title}' уже выдана.")

    else: #в противном случае статус книги остается "выдана"
        my_library[title]["Availability"] = False
        print(f"Книга {title} выдана")


def return_book(title):
    is_book_in_library(title)

    if my_library[title]["Availability"] is True:
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
return_book("Alice’s Adventures in Wonderland")

print(my_library)
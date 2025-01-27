# Реализуйте функцию `remove_book(title)`, которая удаляет книгу из словаря.
# Если книга не найдена, программа должна вывести сообщение об этом.
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


my_library = {
    "Call of Cthulhu": {
        "Author": "Howard Lovecraft",
        "Year": 1928,
        "Availability": None
    },
    "Idiot": {
        "Author": "Fedor Dostoevsky",
        "Year": 1869,
        "Availability": "In stock"
    },
    "The Beach": {
        "Author": "Alex Garland",
        "Year": 1996,
        "Availability": None
    },
    "The Blade Artist": {
        "Author": "Irvine Welsh",
        "Year": 2016,
        "Availability": "In stock"
    }
}


add_book("The Beach", "Alex Garland", 1995)
add_book("Alice’s Adventures in Wonderland", "Lewis Carroll", 1865)

remove_book("The Beach")
remove_book("The Beach")
print(my_library)
# Реализуйте функцию issue_book(title), которая отмечает книгу как выданную (`наличие` становится `False`).
# Реализуйте функцию return_book(title), которая отмечает книгу как вернувшуюся в библиотеку (`наличие` становится `True`).

# def add_book_to_library(title, author, year):
#     my_library[title] = {
#         "Author": author,
#         "Year": year,
#         "Availability": None  # При добавлении новой книги статус наличия None
#     }
#
#
# def add_book(title, author, year):
#     if title in my_library:
#         update_question = input("Такая книга уже есть.Обновить информацию о данной книге?").lower()
#         if update_question == "да":
#             add_book_to_library(title, author, year)
#             print(f"Информация книги '{title}' обновлена.")
#         else:
#             print(f"Информация книги '{title}' не обновлена.")
#     else:
#         add_book_to_library(title, author, year)
#         print(f"Книга '{title}' добавлена.")
#
#
# # Удаление методом del
# def remove_book(title):
#     if title not in my_library:
#         print(f"Книга '{title}' отсутствует в библиотеке.")
#     else:
#         del my_library[title]
#         print(f"Книга '{title}' удалена.")


# #Удаление методом pop
# def remove_book(title):
#     if title not in my_library:
#         print(f"Книга '{title}' отсутствует в библиотеке.")
#     else:
#         delete_library = my_library.pop(title)
#         print(f"Книга '{title}' удалена.")

def issue_book(title):
    if title not in my_library: #если книги нет в библиотеке
        print(f"Книга '{title}' отсутствует в библиотеке.") #сообщение что книги нет

    elif my_library[title]["Availability"] is False: #или если статус книги "выдана"
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


# add_book("The Beach", "Alex Garland", 1995)
# add_book("Alice’s Adventures in Wonderland", "Lewis Carroll", 1865)
#
# remove_book("The Beach")
# remove_book("The Beach")

issue_book("Idiot")
return_book("The Beach")

print(my_library)
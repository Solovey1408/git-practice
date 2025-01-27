# Реализуйте функцию `remove_book(title)`, которая удаляет книгу из словаря.
# Если книга не найдена, программа должна вывести сообщение об этом.
def remove_book_to_library(title):
    my_library[title] = {
        "Author": author,
        "Year": year,
        "Availability": None  # При добавлении новой книги статус наличия None
    }


#Удаление методом del
# def remove_book(title):
#     if title not in my_library:
#         print(f"Книга '{title}' отсутствует в библиотеке.")
#     else:
#         del my_library[title]
#         print(f"Книга '{title}' удалена.")


#Удаление методом pop
def remove_book(title):
    if title not in my_library:
        print(f"Книга '{title}' отсутствует в библиотеке.")
    else:
        delete_library = my_library.pop(title)
        print(f"Книга '{title}' удалена.")


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


remove_book("The Beach")
remove_book("The Beach")
print(my_library)
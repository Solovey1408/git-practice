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


add_book("The Beach", "Alex Garland", 1995)
add_book("Alice’s Adventures in Wonderland", "Lewis Carroll", 1865)

print(my_library)


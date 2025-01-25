# Создайте словарь library, где ключами будут названия книг, а значениями — словари с информацией о книге
# (автор, год издания, наличие).
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

# После этого реализуйте первую функцию book_list_view(library),которая выводит в консоль названия всех книг в библиотеке.
# Если в библиотеке нет книг, функция выводит сообщение об этом.
def book_list_view(my_library):
    if not my_library:
        print("В библиотеке нет книг.")
    for key in my_library:
        print(f"{key}")


book_view = book_list_view(my_library)
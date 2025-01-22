# Напишите программу, которая анализирует текст, введенный пользователем, и выполняет следующие действия:
input_text = str(input("Введите текст: "))

def text_processing(input_text):
    user_string = input_text.lower()
    signs = '!,.?@#$%^&*(){}[]:;'
    without_sign = ''.join(i for i in user_string if i not in signs)
    return without_sign

# 1. Подсчитывает количество слов в тексте.
def count_words_in_string(input_text):
    redit_txt = text_processing(input_text)
    words = redit_txt.split()
    count_words = len(words)
    return count_words

# 2. Самое длинное слово в тексте.
def longest_word(input_text):
    long_word = ""
    words = text_processing(input_text).split()
    for word in words:
        if len(word) > len(long_word):
            long_word = word
    return long_word

# 3. Поиск гласных.
def counting_vowels(input_text):
    vowels = 'аеёиоуыэюя'
    consonants = 'цкнгшщзхъфвпрлджчсмтьб'
    without_sign = text_processing(input_text)
    delete_consonants = ''.join(i for i in without_sign if i not in consonants)
    delete_consonants_without_space = delete_consonants.replace(" ","")
    number_of_vowels = len(delete_consonants_without_space)
    return number_of_vowels

def counting_words(input_text):
    words_and_count = {}
    words = text_processing(input_text).split()

    for i in words:

        if i in words_and_count:
            words_and_count[i] += 1

        else:
            words_and_count[i] = 1

    return words_and_count

how_many_words = count_words_in_string(input_text)
print(f"Сколько слов в тексте:", how_many_words)

what_long_word = longest_word(input_text)
print(f"Самое длинное слово: {what_long_word}")

how_many_vowels = counting_vowels(input_text)
print(f"Количество гласных: {how_many_vowels}")

how_words_and_count = counting_words(input_text)
print(f"Cлова и количество: {how_words_and_count} ")

#Что ? Кого ! Когда .
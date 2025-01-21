# Напишите программу, которая анализирует текст, введенный пользователем, и выполняет следующие действия:
def text_processing():
    user_in_text = user_in_text.lower()
    signs = '!,.?@#$%^&*(){}[]:;'
    without_sign = ''.join(i for i in user_in_text if i not in signs)
    return without_sign

def count_words_in_string(): # 1. Подсчитывает количество слов в тексте.
    words = without_sign.split()
    count_words = len(words)
    return count_words and words

def longest_word():
    long_word = ""
    for i in words:
        if len(i) > len(long_word):
            long_word = i
    return long_word

def counting_vowels():
    vowels = 'аеёиоуыэюя'
    consonants = 'цкнгшщзхъфвпрлджчсмтьб'
    delete_consonants = ''.join(i for i in without_sign if i not in consonants)
    delete_consonants_without_space = delete_consonants.replace(" ","")
    number_of_vowels = len(delete_consonants_without_space)
    return number_of_vowels


def counting_words():
    words_and_count = []

    for word in words:
        count = 0

        if word in words:
            count += 1

        if word not in words_and_count:
            words_and_count.append(word)
        return words_and_count and word and count


user_in_text = str(input('Введите текст: '))

without_sign = text_processing(user_in_text)
print(f'Строка без знаков: {without_sign}')
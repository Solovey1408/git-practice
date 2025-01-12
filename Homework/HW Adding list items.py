  # Напишите программу, которая создает два списка чисел и на их основе создаёт новый список.
  # В новом списке каждый элемент является суммой соответствующих элементов входных списков.
  # Программа должна делать это на основе циклов и работать со списками любой длины.

user_list_1 = [1, 2, 3]  #Создание первого списка
user_list_2 = [6, 7, 8, 9, 10]  #Создание второго списка
sum_list =[]  # Список с суммой первого и второго списка

for i in range(max(len(user_list_1),len(user_list_2))):  #Перебор каждого элемента в списке с максимальным числом элементов
    if i >= min(len(user_list_1), len(user_list_2)):  #Если элемент в списке больше или равен, минимальному количеству
          # элементов в первом и втором списке
         if len(user_list_1) == i + 1 and len(user_list_1) < len(user_list_2):
           sum_list.append(0 + user_list_1[i])
         else:
             sum_list.append(user_list_2[i] + 0)
    else:
        sum_list.append(user_list_1[i] + user_list_2[i])

print(sum_list)

  # for i in range(max(len(user_list_1),len(user_list_2))):
  #    try:
  #        sum_list.append(user_list_1[i] + user_list_2[i])
  #    except IndexError:
  #        if i >= min(len(user_list_1), len(user_list_2)):
  #            if len(user_list_1) == i + 1 and len(user_list_1) < len(user_list_2):
  #                sum_list.append(0 + user_list_1[i])
  #            else:
  #                sum_list.append(user_list_2[i] + 0)
  # print(sum_list)
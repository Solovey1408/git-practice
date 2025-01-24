list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9]
list_c = []
# Решение отличное, но нет
# min_list = list_a if min(len(list_b), len(list_a)) == len(list_a) else list_b
# max_list = list_a if max(len(list_b), len(list_a)) == len(list_a) else list_b
#
# for i in range(len(min_list)):
#
#     max_list[i] += min_list[i]
#
# print(max_list)

#Решение, через while
max_len = max(len(list_a), len(list_b)) #Переменная, которая выводит список с большим количеством элементов
#print(max_len) #Проверка в консоли

min_len = min(len(list_a), len(list_b)) #Переменная, которая выводит список с меньшим количеством элементов
#print(min_len) #Проверка в консоли

i = 0 # переменная для перехода по индексам элементов в списке

while len(list_c) < max_len: #цикл, который будет работать, до тех пор пока кол-во эл-тов списка с суммой эл-тов
#будет меньше или равен списка с большим кол-вом элементов
    if i < min_len: #условие, если индекс меньше минимального списка, элементы суммируются
        sum_element = list_a[i] + list_b[i]
    else: #в противном случае
        if len(list_a) > len(list_b): #условие, при котором, сравниваются два списка
            sum_element = list_a[i] #Если list_a больше, суммой становится элемент из списка list_a
        else: #len(list_a) < len(list_b)
            sum_element = list_b[i] #Если list_b больше, суммой становится элемент из списка list_b

    list_c.append(sum_element) #сумма добавляется в list_c

    i += 1 #увеличение индекса после каждой операции

print(list_c)


list_a = [1, 2, 3]
list_b = [6, 7, 8, 9]

min_list = list_a if min(len(list_b), len(list_a)) == len(list_a) else list_b
max_list = list_a if max(len(list_b), len(list_a)) == len(list_a) else list_b

for i in range(len(min_list)):

    max_list[i] += min_list[i]

print(max_list)
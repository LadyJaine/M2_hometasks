my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_1 = []
for i in my_list:
    if i >= 0:
        my_list_1.append(i)
    else:
        break
my_list_1.remove(0)
print(my_list_1)

first = input('Введите первое число ', )
second = input('Введите второе число ', )
third = input('Введите третье число ', )
if first == second and second==third:
    print('Все числа равны ',3)
elif first == second or second == third or first == third:
    print('Два числа равны ',2)
elif not first == second or second == third or first == third:
    print('Все числа неравны ',0)
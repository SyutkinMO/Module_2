first = int(input ('Первое число'))
second = int(input ('Второе число'))
third = int(input ('Третье число'))

if first == second and second == third:
    print (3, 'Все числа равны')
elif first == second or second == third:
        print (2, 'Есть два одинаковых')
elif first == third:
        print(2, 'Есть два одинаковых')
else: print(0, 'все числа разные')

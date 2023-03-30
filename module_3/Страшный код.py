a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
k = a.count(5)
print('Кол-во цифр 5 при первом объединении:', k)
while 5 in a:
    for i_sym in a:
        if i_sym == 5:
            a.remove(i_sym)
a.extend(c)
k_2 = a.count(3)
print('Кол-во цифр 3 при втором объединении:', k_2)
print('Итоговый список: ', a)

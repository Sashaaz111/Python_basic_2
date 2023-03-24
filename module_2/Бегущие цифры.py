n = int(input('Кол-во чисел: '))
k = int(input('Сдвиг: '))
old_list = []
for i in range(n):
    a = int(input('Введите число: '))
    old_list.append(a)

k %= n
new_list = old_list[-k:] + old_list[:-k]
print('Старый список:', old_list)
print('Новый список:', new_list)

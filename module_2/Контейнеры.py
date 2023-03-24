weight = []
count = int(input('Кол-во контейнеров: '))
for _ in range(count):
    a = int(input('Введите вес контейнера: '))
    weight.append(a)
x = int(input('Введите вес нового контейнера: '))
index = 1
for i in weight:
    if x <= i:
        index += 1
    else:
        break

print('Номер, который получит новый контейнер:', index)
skates = []
leg = []
n = int(input('Количество коньков: '))
for _ in range(1, n + 1):
    size = int(input('Размер пары: '))
    skates.append(size)
k = int(input('Количество людей: '))
for _ in range(1, k + 1):
    size = int(input('Размер ноги человека: '))
    leg.append(size)
leg.sort()
count = 0
i = 0
j = 0
print(skates)
print(leg)
while i < n and j < k:
    if skates[i] >= leg[j]:
        count += 1
        i += 1
        j += 1
    else:
        i += 1
print('Наибольшее количество людей, которые могут взять ролики:', count)
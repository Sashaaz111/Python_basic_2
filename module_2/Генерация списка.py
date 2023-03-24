N = int(input('Введите число: '))
nums = []
num = 1
while num <= N:
    if num % 2 == 1:
        nums.append(num)
    num += 1

print('Список из нечётных чисел от одного до N:', nums)
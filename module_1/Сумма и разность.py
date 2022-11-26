def sum_nums(N):
    summ = 0
    while N != 0:
        summ += N % 10
        N //= 10
    print('Сумма чисел:', summ)
    return summ

def count_nums(N):
    count = 0
    while N != 0:
        count += 1
        N //= 10
    print('Количество цифр в числе:', count)
    return count

N = int(input('Введите число: '))
num1 = sum_nums(N)
num2 = count_nums(N)

def raz(num1, num2):
    return num1 - num2

ans = raz(num1, num2)
print('Разность суммы и количества цифр:', ans)

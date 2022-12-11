def min_del(n):
    i = 2
    while (i <= n):
        if (n % i == 0):
            ans = i
            break
        i += 1
    print('Наименьший делитель, отличный от еденицы:', ans)


n = int(input('Введите число: '))
min_del(n)
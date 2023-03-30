violator_songs = [
['World in My Eyes', 4.86],
['Sweetest Perfection', 4.43],
['Personal Jesus', 4.56],
['Halo', 4.9],
['Waiting for the Night', 6.07],
['Enjoy the Silence', 4.2],
['Policy of Truth', 4.76],
['Blue Dress', 4.29],
['Clean', 5.83]
]
N = int(input('Сколько песен выбрать? '))
summ = 0
for _ in range(1, N + 1):
    name = input('Название песни: ')
    for song in violator_songs:
        if name == song[0]:
            summ += song[1]
print('Общее время звучания песен —', summ, 'минуты')

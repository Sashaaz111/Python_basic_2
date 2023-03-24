films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
count_films = int(input('Сколько фильмов хотите добавить? '))
favorite_films = []
for i in range(count_films):
    film = input('Введите название фильма: ')
    if film not in films:
        print('Ошибка: фильма', film, 'у нас нет :(')
    else:
        favorite_films.append(film)
print('Ваш список любимых фильмов:', "".join(favorite_films))
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while 1 > 0:
    print('Сейчас на вечеринке',len(guests), 'человек:', guests)
    answer = input('Гость пришёл или ушёл? ')
    if answer == 'пришёл' and len(guests) < 6:
        name = input('Имя гостя: ')
        print('Привет,', name)
        guests.append(name)
    elif answer == 'пришёл' and len(guests) == 6:
        name = input('Имя гостя: ')
        print('Прости,', name, 'но мест нет.')
    elif answer == 'ушёл':
        name = input('Имя гостя: ')
        print('Пока,', name)
        guests.remove(name)
    elif answer == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break




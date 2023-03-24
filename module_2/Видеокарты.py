count = int(input('Кол-во видеокарт: '))
old_cards = []
for i in range(count):
    a = int(input('Видеокарта: '))
    old_cards.append(a)
print('Старый спискок видеокарт:', old_cards)
old_cards.remove(max(old_cards))
old_cards.remove(max(old_cards))
print('Новый спискок видеокарт:', old_cards)

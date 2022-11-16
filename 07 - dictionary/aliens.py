# alien_0 = {'colors': 'green', 'points': 5}
# alien_1 = {'colors': 'yellow', 'points': 10}
# alien_2 = {'colors': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)
    
# Создание пустого списка для хранения пришельцев
# aliens = []

# Создание 30 зеленых пришельцев

# for alien_number in range(30):
#     new_alien = {'colors':'green', 'points': 5, 'speed': "slow"}
#     aliens.append(new_alien)

# Вывод первых 5 пришельцев
# for alien in aliens[:5]:
#     print(alien)
    
# Вывод количество созданных пришельцев
# print("Total number of aliens: " + str(len(aliens)))


# Делаем чтобы пришельца меняли характеристики

aliens = []
for alien_numbers in range(30):
    new_aline ={'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_aline)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)


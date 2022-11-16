# list = ['first',1, 2, 3, 'second', 34, 56]
# d ={}
# value = None
# for i in list:
#     if type(i) == str:
#         d[i] = []
#         value = i
#     else:
#         d[value].append(i)

# print(d)
        
# alien_0 = {'color' : 'green', 'points' : 5}
# print(alien_0['color'])
# print(alien_0['points'])
# new_points = alien_0['points']
# print(new_points)

# добавляем новые пары

# print(alien_0) 
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# Создание нового словаря

# alien_0 ={} 
# alien_0['colors'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# Изменение значения в словаре

# alien_0 = {'colors':'green'}
# print("The alien is " + alien_0['colors'].upper())
# alien_0['colors'] = 'yellow'
# print(" The alien is now " + alien_0['colors'].upper())

# alien_0 = {'x_position': 0, "y_position": 25, "speed": "medium"}
# print("Original x_position = " + str(alien_0["x_position"]))
# alien_0["speed"] = 'fast'
# if alien_0["speed"] == "slow":
#     x_increment = 1
# elif alien_0["speed"] == "medium":
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0["x_position"] = alien_0["x_position"] + x_increment
# print("New x_position = " + str(alien_0["x_position"]))

# Удаление пар ключ:значение

# alien_0 = {"colors": "green", "points":5}
# print(alien_0)
# del alien_0["colors"]
# print(alien_0)

# Словарь с однотипными объектами

# favorite_languages = {
#     "jen":'python',
#     'sarah':'c',
#     'edwurd':'rube',
#     'phil':'python',
#     }
# print("Sarah's favorite language is " 
#       + str(favorite_languages['sarah'].title()))

# Перебор всех пар 

# user_0 = {
#     'username' : 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
#     }
# for key, value in user_0.items():
#     print("\nkey: " + key)
#     print("value: " + value)
    
# Перебор ключей только

# favorite_languages = {
#     "jen":'python',
#     'sarah':'c',
#     'edwurd':'rube',
#     'phil':'python',
#     }
# friends = ['phil', 'sarah']

# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print("Hi " + name.title() 
#               + ", I see you favorite language is " 
#               + favorite_languages[name].title())
    
#  Упорядоченный перебор ключей словаря

# favorite_languages = {
#     "jen":'python',
#     'sarah':'c',
#     'edwurd':'rube',
#     'phil':'python',
#     }
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ' thank you')
    
    # Перебор всех значении в словаре
    
favorite_languages = {
    "jen":'python',
    'sarah':'c',
    'edwurd':'rube',
    'phil':'python',
    }    

# for v in favorite_languages.values():
#     print(v.title())

# set()
# for v in set(favorite_languages.values()):
#     print(v.title())

# Задание: Перебрать имена которые не прошли опрос...

persons = ['lady', 'job', 'edwurd', 'kiril', 'phil']

for name in persons:
    if name in favorite_languages.keys():
        print(name.title() + ' Thank you')
    else:
        print(name.title() + ' you must')
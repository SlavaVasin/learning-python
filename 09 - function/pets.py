# def describe_pet(animal_type, pet_name):
#     '''Выводит информацию о животном'''
#     print("\nI have a " + animal_type)
#     print("My " + animal_type + "s name is " + pet_name.title())

# describe_pet('hamster', 'harry')
# describe_pet(animal_type='dog', pet_name='wille')

#-----------------------------------------------------------------
# def describe_pet(pet_name, animal_type='dog'):
#     print('One  - ' + animal_type.title())
#     print('name: ' + pet_name.title())

# describe_pet(pet_name='john', animal_type='cat')
# describe_pet('trixi')
#-------------------------Тест----------------------------------------

# def make_shirt(size='L', text='I love Python'):
#     print('Размер: ' + size + ' с надписью: ' + text.upper())

# make_shirt()
# make_shirt(size='XL')
# make_shirt(size='XXL')
#-----------------------Возращаем значение------------------------------------------
# def get_formatted_name(first_name, last_name):
#     '''Возвращает аккуратное отформатированное полное имя'''
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimmi', 'hendrix')
# print(musician)
#-----------------------Необязательные аргументы------------------------------------------
# def get_formatted_name(first_name,last_name,middle_name=''):
#     if middle_name:
#         full_name = first_name +" "+ middle_name +' '+ last_name
#     else:
#         full_name = first_name + " " + last_name
#     return full_name.title()

# musician = get_formatted_name('jimmi', 'hendrix')
# print(musician)
# musician = get_formatted_name('jonh','hooker', 'lee')
# print(musician)
#-----------------------Возвращает словарь------------------------------------------
# def build_person(first_name,last_name,age=''):
#     '''Возвращает словарь с информацией человека'''
#     person = {'first': first_name, 'last':last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimmi','hendrix','32')
# print(musician)
#----------------------- While ------------------------------------------
# def get_formatted_name(first_name,last_name):
#     full_name = first_name + " " + last_name
#     return full_name.title()

# while True:
#     print('\nPlease tell me your name:')
#     print("enter 'q' at any time to quite")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     formatted = get_formatted_name(f_name,l_name)
#     print('\nHello ' + formatted)
#----------------------- Test ------------------------------------------
# def city_country(city, country):
#     result = city +', '+ country
#     return result.title()

# a = city_country('Moscow', 'russian')
# print(a)


# def make_album(name_person, name_album, count_trek=''):
#     album = {
#         'person': name_person,
#         'album': name_album,
#     }
#     if count_trek:
#         album['trek'] = count_trek
#     return album


# while True:
#     print('\nHello, please write make album')
#     print(" please 'q' at any time quite")

#     name = input('Name person: ')
#     if name == 'q':
#         break
#     album = input('name album: ')
#     if album == 'q':
#         break
#     trek = input('count trek: ')
#     if trek == 'q':
#         break
#     musician = make_album(name, album, trek)
#     print(musician)

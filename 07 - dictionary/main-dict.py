#"имя":"Вячеслав"
#"Возраст" : "34"
# "ключ" : "значение"

# my_dict1 = {}
# my_dict2 = dict()

# print(type(my_dict1))
# print(type(my_dict2))

my_dict = {
    "user": "Tomas Andarson",
    "nickname": "neo",
    "team": ['Morfius', "Trinity"],
    "1": "Matrix",
    'has': 'you',
    (1, 2, 3): "Hello"
}
#print(my_dict)
# print(my_dict['user'])
# print(my_dict['1'])
# print(my_dict[(1, 2, 3)])

months = {"1": 'January', "2": "February"}
#print(months["2"])

person ={"имя": "Виктор", "возраст": "32", "рост": "180"}
#print(person["рост"])

#print(person)
person["любмое блюдо"] = "картошка"  # Добавить новый ключ
person["вес"] = 76
#print(person)

person["вес"] = 109 # Изменить значение в ключе
#print(person)

del person["любмое блюдо"] # Удалить ключ
#print(person)


person["car"] = 'bmw'

# for k, v in person.items():   # Перебрать словарь
#     print(f"{k} >>> {v}")
# print("=" * 20)

# for key in person:
#     print(key)
# print("=" * 20)

# for key in person.keys():
#     print(key)

#if "рост" in person.keys():
# if "язык" in person:
#     print("Данный ключ уже используется")
# else:
#     print("Можете добавить ключ в словарь")
    
# for value in person.values():   # Перебрать словарь(value)
#     print(value)
# print(person)

# person['любимое блюдо'] = "картошка"
# print(person)

# person = {'имя': 'Виктор',
#           'возраст': '32', 
#           'рост': '180', 
#           'вес': 109,
#           'car': 'bmw',
#           'любимое блюдо': ['картошка', "пельмешки", "карьонара"]
#           }

# for value in person["любимое блюдо"]:
#     print(value)
    
# person = {
#     "Александр" : {
#           'возраст': '32',    # Словарь в словаре
#           'рост': '180', 
#           'вес': 109,
#           'машина': 'bmw',
#           'любимое блюдо': ['картошка', "пельмешки", "карьонара"]
#     },
#     "Ольга" : {
#           'возраст': '31',    
#           'рост': '170', 
#           'вес': 76,
#           'машина': 'Audi',
#           'любимое блюдо': ['кукуруза', "креветки"]
#     }
# }

# for username, userinfo in person.items():
#     print(f"Имя пользователя: {username}")
#     age = userinfo['возраст']
#     car = userinfo['машина']
    
#     print(f"Возраст пользователя {username} : {age} лет")
#     print(f"Авто пользователя: {username} : {car} \n")
    
# print(person)

# .get() возвращает значение по указанному ключу
# print(person.get('имя'))
# print(person.get('адрес', "Тюмень")) # Можно указать через "," значение

# setdefault()
# print(person.setdefault(5, "magic")) # Создает новую пару
# print(person)

# copy()
# copy_person = person.copy()
# print(copy_person)

#update({"":""}) создает новую пару в словарь
# person.update({"профессия": "слесарь"})
# print(person)

# pop() Удаляет ключ, возвращает значение
# print(person.pop("рост"))

#popitem() Удаляет и возвращает случайный ключ и значение
# print(person.popitem())
# print(person.popitem())
# print(person.popitem())
# print(person.popitem())

print(person.keys()) # Возвращвет ключи
print(person.values()) # Возвращает значение
print(person.items()) # Возвращает пары в виде кортежа


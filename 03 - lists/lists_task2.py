# «3-4. Список гостей: если бы вы могли пригласить кого угодно (из живых или умерших) на обед,
# то кого бы вы пригласили? 
# Создайте список, включающий минимум трех людей, 
# которых вам хотелось бы пригласить на обед. 
# Затем используйте этот список для вывода пригласительного сообщения каждому участнику.»

names = ["Maks", "Denis", "Sasha", 'Robert', 'Tom']
messeage = ', welcome to the party\n'
print()
print(names[0] + messeage)
print(names[1] + messeage)
print(names[2]+ messeage)
print(names[-2]+ messeage)
print(names[-1] + messeage)

# «3-5. Изменение списка гостей: вы только что узнали, что один из гостей прийти не сможет, 
# поэтому вам придется разослать новые приглашения. 
# Отсутствующего гостя нужно заменить кем-то другим.»

guest_no = names.pop()
print('\nНе сможет прийти в гости ' + guest_no.title())

names.append('Karl')
print('\nвместо '+ guest_no + " придет " + names[-1])

print(names)

# «3-6. Больше гостей: вы решили купить обеденный стол большего размера. 
# Дополнительные места позволяют пригласить на обед еще трех гостей.»

names.insert(0, 'kirill')
print('так же пригласил ' + names[0])
names.insert(2, 'Platon')
print('так же пригласил ' + names[2])
names.insert(-1, 'Pasha')
print('так же пригласил ' + names[-2])
print(names)
print()

# «3-7. Сокращение списка гостей: только что выяснилось, 
# что новый обеденный стол привезти вовремя не успеют, 
# и места хватит только для двух гостей.»

print(names[0] + messeage)
print(names[1] + messeage)
print(names[2]+ messeage)
print(names[3]+ messeage)
print(names[4]+ messeage)
print(names[-3]+ messeage)
print(names[-2]+ messeage)
print(names[-1] + messeage)

message_2 = "Приглашаются всего два гостя\n"
print(message_2)
del_name = names.pop()
print('Сожалею, что вечеринка отменяется ' + del_name.title())
del_name = names.pop()
print('Сожалею, что вечеринка отменяется ' + del_name.title())
del_name = names.pop()
print('Сожалею, что вечеринка отменяется ' + del_name.title())
del_name = names.pop()
print('Сожалею, что вечеринка отменяется ' + del_name.title())
del_name = names.pop()
print('Сожалею, что вечеринка отменяется ' + del_name.title())
del_name = names.pop()
print('Сожалею, что вечеринка отменяется ' + del_name.title())
print(names)
print(names[0] + " Приглашение ранее для Вас остается")
print(names[1] + " Приглашение ранее для Вас остается")
del names[0]
del names[0]
print(names)

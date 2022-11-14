# «4-13. 
# Шведский стол: меню «шведского стола» в ресторане состоит всего из пяти пунктов. 
# Придумайте пять простых блюд и сохраните их в кортеже.
# • вывод всех блюд, предлагаемых рестораном.
buffets = ('Potatoes', 'Tomatoes', 'Stuffed peppers', 'Fried egg', 'Tuna')
for buffet in buffets:
    print(buffet)

# • Ресторан изменяет меню, заменяя два элемента другими блюдами. 

buffets = ('Potatoes', 'Tomatoes', 'banana', 'meat', 'Tuna')
for buffet in buffets:
    print(buffet.title())
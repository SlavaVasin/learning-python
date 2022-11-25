#списко моделей которых нужно распечатать
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahendron']
# completed_models = []

# #цикл посл.печатает каждую модель из списка
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     #печать модели на 3Д пирнтере
#     print("printing model: " + current_design)
#     completed_models.append(current_design)

# #Вывод готовых всех моделей
# print('\nThe following models have been printed:')
# for i in completed_models:
#     print(i)

#---------------------- с помощью функции ---------------------------
# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         currenet_designs = unprinted_designs.pop()
#         print("printed models: " + currenet_designs)
#         completed_models.append(currenet_designs)

# def show_completed_models(completed_models):
#     print("\nThe following models have been printed:")
#     for i in completed_models:
#         print(i)

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahendron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

#Чтобы не трогать оригинал списка, можно сделать копию
# print_models(unprinted_designs[:],completed_models)

#--------------------------Test----------------------------------
magicians = ['alfred', 'tom', 'john', 'andy']
new_magicians = []


def show_magicians(names):
    for name in names:
        print("Hello " + name.title())


def make_great(old_magicians, new_magicians):
    while old_magicians:
        names = old_magicians.pop()
        new_magicians.append(names + ' Great')


make_great(magicians[:], new_magicians)
show_magicians(new_magicians)
print(magicians)
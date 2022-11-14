# «4-10. Срезы: добавьте в конец одной из программ, 
# написанных в этой главе, фрагмент, который делает следующее.
# • Выводит сообщение «The first three items in the list are:», 
# а затем использует срез для вывода первых трех элементов из списка.
magicians = ['alice', 'david', 'carolina', 'tom', 'david', 'john']
print("The first three items in the list are:")
print(magicians[:3])
# • Выводит сообщение «Three items from the middle of the list are:», 
# а затем использует срез для вывода первых трех элементов из середины списка.
print('\nThree items from the middle of the list are:')
print(magicians[3:])
# • Выводит сообщение «The last three items in the list are:», 
# а затем использует срез для вывода последних трех элементов из списка.
print("\nThe last three items in the list are:")
print(magicians[-3:])
# 4-11. Моя пицца, твоя пицца: начните с программы из упражнения 4-1. 
# Создайте копию списка с видами пиццы, присвойте ему имя friend_pizzas. 
# Затем сделайте следующее.
my_pizzas = ['pepperoni', 'four cheeses', 'bavarian']
friend_pizza = my_pizzas[:]
# • Добавьте новую пиццу в исходный список.
# • Добавьте другую пиццу в список friend_pizzas.
# • Докажите, что в программе существуют два разных списка. 
my_pizzas.append('three cheese')
friend_pizza.append('village')
print(my_pizzas)
print(friend_pizza)
# Выведите сообщение «My favorite pizzas are:», а затем первый список в цикле for. 
# Выведите сообщение «My friend’s favorite pizzas are:», а затем второй список в цикле for. 
# Убедитесь в том, что каждая новая пицца находится в соответствующем списке.
for pizza in my_pizzas:
    print(f"My favorite pizzas are: {pizza}")

for pizza in friend_pizza:
    print(f"My friend’s favorite pizzas are: {pizza}")
# 4-12. Больше циклов: во всех версиях foods.py 
# из этого раздела мы избегали использования цикла for при выводе для экономии места. 
# Выберите версию foods.py и напишите два цикла for для вывода каждого списка.»

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
for food in my_foods:
    print(f"My favorite foods are: {food}")

friend_foods.append('ice cream')
for food in friend_foods:
    print(f"My friends favorite foods are: {food}")
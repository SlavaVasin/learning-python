# 4-3. Считаем до 20: используйте цикл for для вывода чисел от 1 до 20 включительно.
numbers =[value for value in range(1,21)]
print(numbers)

# 4-4. Миллион: создайте список чисел от 1 до 1 000 000, 

numbers_million = [value for value in range(1,1000000)]
# print(numbers_million)

# 4-5. Суммирование миллиона чисел: создайте список чисел от 1 до 1 000 000, 
# затем воспользуйтесь функциями min() и max() 
# Вызовите функцию sum()
numbers_million=[value for value in range(1,1000000)]
print(min(numbers_million))
print(max(numbers_million))
print(sum(numbers_million))

# 4-6. Нечетные числа: Выведите все числа в цикле for.
numbers = [value for value in range(1,21,2)]
print(numbers)

# 4-7. Тройки: создайте список чисел, кратных 3, в диапазоне от 3 до 30. 
numbers_three = [value for value in range(3,31,3)]
print(numbers_three)

# «4-8. Создайте список первых 10 кубов (то есть кубов всех целых чисел от 1 до 10) 
cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)
print(cubes)

# 4-9. Генератор кубов: используйте конструкцию генератора списка для создания списка первых 10 кубов.
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
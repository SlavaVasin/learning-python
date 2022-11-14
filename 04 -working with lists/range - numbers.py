for value in range(1,5):
    print(value)
    
# Числовой список
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

# Список квадратов в диапазоне от 1 до 10
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# Более компактный код
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

# Ещё более компактнее код
squares = [value ** 2 for value in range(1,11)]
print(squares)


# функция min(), max(), sum()
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(digits)
print("Минимальное число: " + str(min(digits)))
print(f"Максимальное число: {max(digits)}")
print(f"Сумма всех чисел состовляет: {sum(digits)}\n")


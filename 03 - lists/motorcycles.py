motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Изменение списка
#motorcycles[0] = 'ducati'
print(motorcycles)

# Добавление списка
motorcycles.append('ducati')
print(motorcycles)

# Добавляем в новый список
motorcycles =[]
motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('ducati')
motorcycles.append('yamaha')
print(motorcycles)

# Add method .insert() где указываем позицию
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Удаление элемента из списка
print()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# Удаление методом pop() позволяет работать с элементом после
print()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motocycles = motorcycles.pop()
print(motorcycles)
print(popped_motocycles)


motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(0)
print("The last motocycles I owned was a " + last_owned.title() + ".")

# Удаление по значению элемента методом .remove()
print()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
print()

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.\n")

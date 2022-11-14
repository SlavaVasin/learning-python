name = 'ada lovelas'
print(name.title())   #  «первый символ каждого слова в строке к верхнему регистру»

name = "Ada Lovelas"
print(name.upper())   # все регистр букв БОЛЬШИЕ
print(name.lower())   # все буквы маленькие

# Конкатенация
first_name = "ada"
last_name = "lovelas"
full_name = first_name + " " + last_name
#print(full_name)
#print('Hello,' + full_name.title() + "!")
message = 'Hello,' + full_name.title() + "!"
print(message)

# \n - new row, \t - tab
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = ' python '
favorite_language = favorite_language.rstrip() # метод удаляет пробел справа
print(favorite_language)

favorite_language = favorite_language.lstrip() # метод удалаяет пробел слева
print(favorite_language)

favorite_language = favorite_language.strip() # метод удаляет пробелы с обоих концов
print(favorite_language)

age = 23
message = "Happy " + str(age) + "rd Birthday!" #  функция str() преобразует значение в строковое значение
print(message)

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]  # copy list

print('My favorite foods are: ')
print(my_foods)
print('\nMy friends favorite faoods are:')
print(friend_foods)

my_foods.append('ice cream')
friend_foods.append('cannoli')

print('My favorite foods are: ')
print(my_foods)
print('\nMy friends favorite faoods are:')
print(friend_foods)

# !!! double list !!!
my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods   # This doesn't work

my_foods.append('ice cream')
friend_foods.append('cannoli')

print(my_foods)
print(friend_foods)
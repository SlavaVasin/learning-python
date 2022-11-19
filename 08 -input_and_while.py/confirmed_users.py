# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_users = unconfirmed_users.pop()
#     print("Verifying user: " + current_users.title())
#     confirmed_users.append(current_users)
    
# print("\nThe followingusers have been confirmed")
# for current in confirmed_users:
#     print(current.title())

# Очитстить список

pets = ['dog', 'cat', 'dog', 'goldfish', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


players = ['charles', 'martina', 'michale', 'florence', 'eli']
print(players[0:3])

print(players[2:])

print(players[::-1]) # Перевернуть строку

print(players[-3:])

# Перебор содержимого среза
players = ['charles', 'martina', 'michale', 'florence', 'eli']
print("\nHere are the firste three players in my team: ")
for player in players[:3]:
    print(player.title())

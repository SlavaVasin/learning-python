bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title()) # можно использ.строковые методы

print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

# с конкатенцации можно работать
message = "My first bicycles was a " + bicycles[0].title() + "."
print(message)


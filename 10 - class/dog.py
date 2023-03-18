class Dog():
    '''Простая модель собаки'''
    
    def __init__(self, name, age):
        '''Инициализируеь атрибуты name и age'''
        self.name = name
        self.age = age
        
    
    def sit(self):
        '''Собака садится по команде'''
        print(self.name.title() + ' is now sitting')
        
    
    def roll_over(self):
        '''Собака перекатывается по команде'''
        print(self.name.title() + ' rolled over!')
        
my_dog = Dog('wille', 6)
print('My dogs name is ' + my_dog.name.title())
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()


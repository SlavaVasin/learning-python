class Restauran():
    ''' Обычный ресторан '''
    def __init__(self, restuaran_name,cuisine_type):
        self.name = restuaran_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        '''Описание ресторана'''
        print('Ресторан называется: ' + self.name.title())
        print("Кухня очень " + self.type)
    
    def open_restaurant(self):
        print(self.name.title() + ' Open 24/7')
        
my_rest = Restauran('burger', 'cool')
# print(my_rest.name.title())
# print(my_rest.type)
my_rest.describe_restaurant()
my_rest.open_restaurant()
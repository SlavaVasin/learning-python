class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
    
    def read_odometr(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(" you can't rollback on odometer ")
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
# my_new_car = Car('bmw', 'z5', 2020)
# print(my_new_car.get_descriptive_name())
# # my_new_car.read_odometr() <--- 0 mile
# my_new_car.update_odometer(23) # <---- задаем 23 mile
# my_new_car.read_odometr() # <---- Вывод: 23 mile
# my_new_car.update_odometer(13) 
# my_new_car.read_odometr()

my_new_car = Car('subaru', 'outback', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23500)
my_new_car.read_odometr()
my_new_car.increment_odometer(300)
my_new_car.read_odometr()
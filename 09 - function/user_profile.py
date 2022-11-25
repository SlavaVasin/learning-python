# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for k, v in user_info.items():
#         profile[k] = v
#     return profile
# user_profile = build_profile('albert', 'enstein',
#                              location = 'pincetion',
#                              field = 'physics')
# print(user_profile)
#---------------------------test--------------------------------------
# component_sendvich = ['cheese', 'tomat', 'pepper', 'sosiges']

# def sendich(component, *type):
#     print(f"\nComponent {component}")
#     for i in type:
#         print(i)

# result = sendich(4, component_sendvich)
#---------------------------test--------------------------------------
# def profile(first, last, age, **user_info):
#     profile = {}
#     profile['First name'] = first
#     profile['Last name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
# user_profiles = profile('Slava','Vasin','34',
#                         country = 'Russia',
#                         city = 'Tumen')
# print(user_profiles)
#---------------------------test--------------------------------------
# def make_car(marka, model, **info_cars):
#     cars = {}
#     cars['marka'] = marka
#     cars['model'] = model
#     for key, value in info_cars.items():
#         cars[key] = value
#     return cars

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)
#---------------------------test--------------------------------------
cars = ['subaru', 'audi', 'bmw', 'honda']
new_cars = []


def make_car(old_cars, new_cars):
    while old_cars:
        name = old_cars.pop()
        new_cars.append(name)


def news_cars(value):
    for i in value:
        print(i, end=' ')


make_car(cars[:], new_cars)
news_cars(new_cars)

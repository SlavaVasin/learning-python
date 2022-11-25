def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza whith the following toppings:")
    for i in toppings:
        print("- " + i)
    
make_pizza(16, 'pepperoni')
make_pizza(12, 'extra cheese', 'moshrooms', 'green peppers')
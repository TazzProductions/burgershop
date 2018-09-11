


ready = input(' Are you ready to order?:  y/n')

while ready == 'y':
    if ready == 'y':
        print()
        print()
        randomToppings = ['ketchup', 'mustard', 'onions', 'lettuce', 'tomato', 'hot sauce', 'american cheese', 'cheddar cheese']
        print(randomToppings)
        break
    if ready == 'n':
        break


from menu_function import menu
import random
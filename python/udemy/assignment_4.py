toppings_list = {
    "1": "Onions",
    "2": "Lettuce",
    "3": "Tomato",
    "4": "Olives",
    "5": "Peppers",
    "6": "Tomatoes",
}
pizza_prize = 5
print('We are serving pizza with the following toppings:-')
for k, v in toppings_list.items(): print(f'{k}: {v}')
toppings = [x for x in input('Please pick any three from the above e.g. type '+k+' for '+v+' (separated by space): ').split()]
quantity = int(input('Please enter how many pizzas do you want: '))
total_amount = float(pizza_prize * quantity)
'''opted_toppings = []
for x in toppings: opted_toppings.append(toppings_list[x])'''
opted_toppings = [toppings_list[x] for x in toppings]
print(f'You\'ve selected {opted_toppings} as toppings. Total amount: ${total_amount}')
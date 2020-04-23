pizzas = ['olive', 'cheese', 'saucy']
for pizza in pizzas:
	print(f"\nI love {pizza} pizza.")
	print(f"Pizza is very nutritious.")

print("\nI really love pizza!")

#store information about a pizza being ordered
#were now storing a list inside a dictionary. 
#mushrooms and extra cheese is the list inside the dictionary "pizza"

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
    }

#summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")		
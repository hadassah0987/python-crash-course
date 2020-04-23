#!= determines whether two values are not equal
requested_topping = 'mushrooms'

if requested_topping != 'anchoives':
    print("Hold the anchoives!")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")

if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")

if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")           
#if u want one block of code to run  us an "f-elif-else" statemen
#if u wantmore than one block of code to run use a series of "if" statements
requested_toppings = []

if requested_toppings:
   for requested_topping in requested_toppings:
       print(f"Adding {requested_topping}.")
   print("\nFinished making your pizza!")        
else:  
    print("Are you sure you want plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")

	else:
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza! Enjoy your delicious pizza!")
#use a space in between ==, >= and <=.		




   
  
       

age = 2

if age < 4:
    print("Your admission is $2. Have fun on the rides!")
elif age < 18:
    print("Your admission is $25. Have fun on the rides!")
else:
    print("Your admission is $40. Have fun on the rides!")

age = 12
if age < 4:
   price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40        
else:
    price = 20

print(f"Your admission is ${price}. Enjoy your stay!")
#u cud use as many elif as u want
#u dont need to put an else

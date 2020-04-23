cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#sort puts the items in the list in alphabetical order permanantly
cars.sort(reverse=True)
print(cars)
#reverse=True puts the item in the list in opposite alphabetical order. for example the list starts with z instead of a.
#sorted puts the items in the list alphabetically but not permanantly.

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars) 

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
#reverse just changes the order randomly and permanately but not in alphabetical order.
car = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
#len finds the length of the list. for example for cars the len is 4.

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())    
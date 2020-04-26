#the modulo operator(%), divides one number by another number and returns the remainder. it just tells u what the remainder is.
#when one number is divisible by another number, the remainde is zero. use this to determine if the fact is even or odd.

number = input("Enter a number, and I'll tell you if it's even or oddd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
    
        
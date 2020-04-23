
julia = ("Julia", "Jones", 2000, "6 Mariner Way", "Monsey", "NY")
print(julia)

(name, surname, b_year, address, city, state) = julia
print(f"\nFirst Name: {name}\nLast Name: {surname}\nBorn: {b_year}\nAddress: {address}\nCity: {city}, {state}")

print(f"\nFirst Name: {julia[0]}\nLast Name: {surname}\nBorn: {b_year}\nAddress: {address}\nCity: {city}, {state}")



def ageToDesription(age):
    if age <= 2:
       return "You are a baby."

    elif age >= 2 and age <= 4:
	    return "You are a toddler."

    elif age >= 13 and age <= 20:
	    return "You are a teen."

    elif age <= 20 and age >= 65:
       return "You are an adult."

    elif age >= 65:
       return "You are an elder."


for a in range(70):
    print(f"age {a}: {ageToDesription(a)}")

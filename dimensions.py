dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#a tuple looks like a list but it can't change. put () by a tuple.
#you always need a comma by a tuple even if u have just one element in the list


def printTuple(text, tuple):
    print(text)
    for element in tuple:
        print(element)    



dimensions = (200, 50)
printTuple("\noriginal dimensions", dimensions)

dimensions = (200, 50, 1)
printTuple("\noriginal dimensions", dimensions)


old_dimensions = dimensions
dimensions = (400, 100)
printTuple("\nModified dimensions:", dimensions)    
printTuple("\nold dimensions:", old_dimensions)    


def concatenate(s1, s2):
    cs = s1 + s2
    return (cs, len(cs))

print(concatenate("hello ", "world"))

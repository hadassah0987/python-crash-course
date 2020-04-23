bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
#the first one in a list is always 0 and not 1. for example trek is 0 and connondale is 1. -1 is always the last one in the list. for example it is specialized.
bicycles = ['trek', 'connondale', 'redline', 'specialized']
print(bicycles[-1])
 
bicycles = ['trek', 'connondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)
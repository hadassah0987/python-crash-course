users = {
    'aeinstein':{
       'first':'albert',
       'last': 'einstein',
       'location': 'princeton',
       },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },   
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

#this is called a dictionary in a dictionary
#both structures of the dictionary are the same even though it's not required by Python. it makes the dictionaries easier to work with
    


   
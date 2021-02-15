# Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
alien_1['color'] = 'yellow'
print(f"The alien is now {alien_1['color']}.")

del alien_1['points']

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# Set
languages = {'python', 'ruby', 'python', 'c'}

# Вложения
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# Создание пустого списка для хранения пришельцев.
aliens = []
# Создание 30 зеленых пришельцев.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': alien_number, 'speed': 'slow'}
    aliens.append(new_alien)
# Вывод первых 5 пришельцев:
for alien in aliens[:5]:
    print(alien)
# Вывод количества созданных пришельцев.
print(f"Total number of aliens: {len(aliens)}")

# Сохранение информации о заказанной пицце.
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
# Описание заказа.
print(f"You ordered a {pizza['crust']}-crust pizza "
"with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

users = {
'aeinstein': {
'first': 'albert',
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
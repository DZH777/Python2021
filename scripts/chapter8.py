import functions8

functions8.greet_user1()
functions8.greet_user2('jesse')
functions8.describe_pet('hamster', 'harry')
functions8.describe_pet(pet_name='harry', animal_type='hamster')
functions8.describe_pet(pet_name='willie')

musician = functions8.get_formatted_name('jimi', 'hendrix')
print(musician)

usernames = ['hannah', 'ty', 'margot']
functions8.greet_users(usernames)

functions8.make_pizza('pepperoni')
functions8.make_pizza('mushrooms', 'green peppers', 'extra cheese')

user_profile = functions8.build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)
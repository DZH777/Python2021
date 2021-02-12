magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

magicians = []
for magician in magicians:
    print(magician)

for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

print(min(even_numbers), max(even_numbers), sum(even_numbers))

squares = [value**2 for value in range(1,11)]
print(squares)

print(squares[1:3])
print(squares[:3])
print(squares[1:])
print(squares[-4:])


players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Кортежи tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
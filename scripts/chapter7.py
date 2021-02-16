message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# оператор вычисления остатка
print(f"5 % 3 = {5 % 3}")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# Начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Вывод всех проверенных пользователей.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
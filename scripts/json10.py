import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
print(numbers)

username = input("What is your name? ")
age = input("how old are you? ")
personal_data = [username, age]
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(personal_data, f)
print(f"We'll remember you when you come back, {username}!")

filename = 'username.json'
with open(filename) as f:
    personal_data = json.load(f)
print(f"Welcome back, {personal_data[0]}!")
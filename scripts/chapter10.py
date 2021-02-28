with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

filename = 'pi_digits.txt'
with open(filename) as file_object:
    pi_string = ''
    for line in file_object:
        pi_string += line.rstrip()
    print('pi_string: '+pi_string)
    print(len(pi_string))

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
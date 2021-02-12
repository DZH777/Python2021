bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-4])
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
bicycles[0] = 'trek777'
print(bicycles[0])
bicycles.append('qwery')
print(bicycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(1, 'ducati')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
cars.reverse()
print(cars)
print(len(cars))
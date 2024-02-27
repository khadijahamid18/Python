cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)

#output
# {'Tokyo', 'Madrid', 'Kabul', 'Seoul', 'Berlin', 'Delhi'}


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities)

#output
# {'Berlin', 'Madrid', 'Tokyo', 'Delhi', 'Kabul', 'Seoul'}


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

#output
# {'Madrid', 'Tokyo'}


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)

#output
# {'Tokyo', 'Madrid'}


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

#output 
# {'Seoul', 'Kabul', 'Berlin', 'Delhi'}


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)

#output 
# {'Kabul', 'Delhi', 'Berlin', 'Seoul'}


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

#output
# {'Tokyo', 'Madrid', 'Berlin'}


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))

#output
# {'Tokyo', 'Berlin', 'Madrid'}


cities = {"Tokyo", "Lahore", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Lahore"}
print(cities.isdisjoint(cities2))

#output
# False


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y) 
print(z)

# output
# True


cities = {"Tokyo", "Lahore", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Lahore"}
print(cities.issuperset(cities2))

#output
# False


cities = {"Tokyo", "Lahore", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Delhi", "Lahore"}
print(cities2.issubset(cities))

# output
# True

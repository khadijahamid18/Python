info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)  
# output
# {'name': 'Karan', 'age': 19, 'eligible': True}


# Accessing single values
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))
#output
# Karan
# True


# Accessing multiple values
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())
# output
# dict_values(['Karan', 19, True])


# Accessing keys
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())
#output
# dict_keys(['name', 'age', 'eligible'])


# Accessing key-value pairs
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())
#output
# dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])


info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) 
print(info.keys())
print(info.values())

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 

#Creating Dictionary 
my_dict = dict()   
print(my_dict)
my_dict2 = {}
print(my_dict2)

eng_sp = dict(one = 'uno', two = 'dos', three = 'tres')
print(eng_sp)

eng_sp2 = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng_sp2)

eng_sp3 = [('one', 'uno'), ('two', 'dos'), ('three', 'tres')]
print(dict(eng_sp3))

#Update / add an element to the dictionary
my_dict = {'name': 'Jack', 'age': 26}
my_dict['age'] = 27
print(my_dict)
my_dict['address'] = 'Downtown'
print(my_dict)

#Traversal through a dictionary
my_dict = {'name': 'Jack', 'age': 26}
for key in my_dict:
    print(key, my_dict[key])

#Removing elements from a dictionary
my_dict = {'name': 'Jack', 'age': 26, 'address': 'Downtown'}
del my_dict['age'] 
print(my_dict)
my_dict().pop('address', None)
print(my_dict)
my_dict.clear()
print(my_dict)

#Dictionary Methods
my_dict = {'name': 'Jack', 'age': 26, 'address': 'Downtown', 'education': 'Engineering'}
dict = my_dict.copy() #returns a copy of the dictionary
my_dict.get('name', None) #returns the value of the specified key
my_dict.items() #returns a list of key-value pairs
my_dict.keys() #returns a list of keys
my_dict.values() #returns a list of values
my_dict.popitem() #removes the last key-value pair
my_dict.setdefault('address', None) #returns the value of the specified key. If the key does not exist: insert the key, with the specified value

new_dict = {'name': 'Jill', 'age': 23}
my_dict.update(new_dict)

sorted(new_dict)

#Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}
new_dict = {new_key: new_value for new_key, new_value in dict.items()}
new_dict = {new_key: new_value for new_key, new_value in dict.items() if new_key != 'age'}
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
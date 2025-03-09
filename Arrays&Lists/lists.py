#   Created by Elshad Karimov on 10/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Accessing/Traversing the list

shoppingList = ['Milk', 'Cheese', 'Butter']

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    # print(shoppingList[i])
empty = []
for i in empty:
    print("I am empty")


# Update/Insert - List 

myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(4,15)

myList.append(55)

newList = [11,12,13,14]
myList.extend(newList)
print(myList)


#  Searching for an element in the List
myList =  [10,20,30,40,50,60,70,80,90]

def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print(searchinList(myList, 100))


#  List operations / functions
a = [1,2,3]
b=[4,5]
c= a+b #concatination of two lists

a*4 # Repetition

len(a) # Length of the list

max(a) # returns the max value from the 
min(a) # returns the min value from the list
sum(a) # returns the sum of all elements in the list

total = 0 
count = 0
while (True):
    inp = input('Enter a number: ') 
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1 
    average = total / count
					
print('Average:', average)



numlist = list() 
while (True):
    inp = input('Enter a number: ') 
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
					
average = sum(numlist) / len(numlist) 
print('Average:', average)


# Strings and Lists
str = "spam"
print (list(a)) # ['s', 'p', 'a', 'm']

str2= "hello world"
print(str2.split()) # ['hello', 'world']

str3= "hello,world"
print(str3.split(',')) # ['hello', 'world']

delimiter = ','  # or any other character
print(delimiter.join(str3.split(','))) # hello-world

#List Comprehension
prev_list = [1,2,3,4,5]
new_list = [i*2 for i in prev_list]
print(new_list)

language='Python'
new_language = [i for i in language]
print(new_language)

# Conditional in List Comprehension
numbers = [1,2,3,4,5,6,7,8,9,10]
new_list = [i for i in numbers if i%2==0]
print(new_list)

sentence = "the quick brown fox jumps over the lazy dog"
def is_vowel(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() in vowels
vowels = [i for i in sentence if is_vowel(i)] # can use functions in items as well
print(vowels)
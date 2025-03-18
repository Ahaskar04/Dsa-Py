#Tuples are immutable and hashable
#Tuples are faster than lists

#Creating a tuple
t = (1,2,3,4,5)
t2 = ('a',) #Single element tuple
print(t)

#Accessing elements
print(t[0])

#slice
print(t[1:3])

#Traversal
for i in t:
    print(i)

#Search an element
print(1 in t)
print(t.index(1))

#Tuple operations
print(t+t2)
print(t*2)
print(t.count(1))
print(t.index(1))
#Initializer 
class Start:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
    
a = Start("John", 36)
print(a.__dict__)
print(a.name)
print(a.age)
a.myfunc()
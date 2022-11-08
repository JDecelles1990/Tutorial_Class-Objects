# (2:50} CLASSES & OBJECTS #3 - #INHERITENCE: #ATTRIBUTRES & #METHODS
#INHERITENCE: not copy under class (Dog) insted of [class cat(objectD=OG):]
#ATTRIBUTRES
#METHODS

class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hi I am", self.name, 'and I am', self.age, 'years old')

    def talk(self):
        print('Woof! Woof!')


class Cat(Dog):                                   #Object=Dog= CatINHERITENCEfromDog (Cat=ChildCLASS)
    def __init__(self, name, age, color):
        super().__init__(name, age)              #SUPERclass=Dog
        self.color = color

    def talk(self):
        print('Meoooooowwww!!!')





jim = Dog('Jim', 77)
jim.talk()


tim = Cat('tim', 5, 'blue')
tim.speak()















#     def __init__(selfself, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def speak(self):
#         print("Hi I am", self.name, 'and I am', self.age, 'years old')

#SUPPR.
   # def change_age(self, age):
    #     self.age = age
    # def add_weight(selfself, weight):
    #     self.weight = weight



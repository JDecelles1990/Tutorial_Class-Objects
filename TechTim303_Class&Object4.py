#Default Py **METHODS __Add__Sub__Mul Compare POINTS #inside class

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):                          #**(METHODS)
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def __len__(self):                     #METH:Lengh #call __len__(6e meth)
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, p):                         #greaterTHAN
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __lt__(self, p):
        return self.length() < p.length()

    def __le__(self, p):                          #lessORequal
        return self.length() <= p.length()

    def __eq__(self, p):                          #==COMPARISON
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) + ')'


p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)
>>>
print(p1 == p2)
print(p1 > p2)
print(p1 <= p3)





#p1 + p2                                            #p2 becomes p, p1 becomes self

# p5 = p1 + p2
# p6 = p4 - p1
# p7 = p2*p3
#
# print(p5, p6, p7)
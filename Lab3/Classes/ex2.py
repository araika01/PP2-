class Shape:
    def area(self):
        self.a = 0
        print(self.a)
class Square(Shape):
    def __init__(self):
        self.len = int(input())
    def area(self):
        self.a = self.len * self.len
        print(self.a)
x = Square()
x.area()
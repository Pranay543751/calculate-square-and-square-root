# calculate-square-and-square-root
how to calculate square and square root by using class in python


class calculator:
     def __init__(self,n):
         self.n =n
     def square(self):
         print(f"the square is {self.n*self.n}")
     def cube(self):
         print(f"the cube is {self.n*self.n*self.n}")
     def squareroot(self):
         print(f"the squareroot is {self.n**0.5}")
     @staticmethod
     def hello():
       print("hello friends")
 a = calculator(4)
 a.hello()
 a.square()
 a.cube()
 a.squareroot()

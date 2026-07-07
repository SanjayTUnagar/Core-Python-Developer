# Type of method => Static method 

class A: 
    @staticmethod
    def f1():
        print("Hello")
        
    @staticmethod
    def f2(a,b):
        print(a,b)

A.f1()
A.f2(5,6)

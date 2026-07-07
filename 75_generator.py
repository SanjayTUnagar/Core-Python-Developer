

def f1():
  yield 10
  yield 20
  yield 30 
g=f1()
a=next(g)
b=next(g)
c=next(g)
print(g)
print("a is :",a)
print("b is :",b)
print("c is :",c)



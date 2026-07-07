#Filter 

def f(x):
      if x>=3:
        return x
y=filter(f,(1,2,3,4))
l1=list(y)
print(l1)
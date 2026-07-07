# Local and Globle Variable 

x=20
def f1(): 
    x=10
print(globals()['x'],x)
f1()
print(x)
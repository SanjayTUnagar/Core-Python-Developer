# Map No need to pass many arguments

def square(a):
    return a*a
x=map(square,[1,2,3,4])
l1 = list(x)
print(l1)

# There a two diffence ways.
def square(a):
    return a*a
x=map(square,[1,2,3,4])
for e in x:
    print(e,end=',')
#print(l1)

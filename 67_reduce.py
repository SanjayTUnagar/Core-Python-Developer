# Reduce : reduce a sequence of values to a single value

from functools import reduce
x = reduce (lambda a,b:a+b,[1,2,3,4])
print(x)

from functools import reduce
x = reduce (lambda a,b:a*b,[1,2,3,4])
print(x)
# Define a generator to yield first n natural number. 

def f1(n):
    i=1
    while i<=n: 
     yield i
     i=i+1
     print(n)